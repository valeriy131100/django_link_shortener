import secrets
from itertools import count

from django.conf import settings
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers

from links.models import ShortenedLink


class ShortenedLinkSerializer(serializers.ModelSerializer):
    short_url = serializers.SerializerMethodField(read_only=True)

    def get_short_url(self, shortened_link: ShortenedLink):
        request = self.context.get('request')
        relative_url = reverse(
            go_link,
            kwargs={'short_name': shortened_link.short_name}
        )
        return request.build_absolute_uri(relative_url)

    class Meta:
        model = ShortenedLink
        fields = (
            'destination',
            'short_name',
            'short_url'
        )
        extra_kwargs = {
            'destination': {
                'style': {
                    'placeholder': 'https://example.com'
                }
            },
            'short_name': {
                'required': False,
                'style': {
                    'placeholder': 'Заполнять не обязательно'
                }
            }
        }


def index(request):
    return render(
        request,
        template_name='index.html',
        context={'link_serializer': ShortenedLinkSerializer}
    )


def go_link(request, short_name):
    shortened_link = get_object_or_404(ShortenedLink, short_name=short_name)
    return redirect(shortened_link.destination)


@api_view(['POST'])
def make_link(request):
    serializer = ShortenedLinkSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    link_description = serializer.validated_data

    short_name = link_description.get('short_name')
    destination = link_description.get('destination')

    if not short_name:
        existed_short_names = ShortenedLink.objects.values_list(
            'short_name',
            flat=True
        )
        for retry in count(start=1):
            if (retry % settings.GENERATE_SHORT_URL_MAX_RETRIES) == 0:
                settings.GENERATE_SHORT_URL_BYTES += 1

            short_name = secrets.token_urlsafe(
                nbytes=settings.GENERATE_SHORT_URL_BYTES
            )
            if short_name not in existed_short_names:
                break

    new_link = ShortenedLink.objects.create(
        destination=destination,
        short_name=short_name
    )

    return Response(
        ShortenedLinkSerializer(
            new_link,
            context={
                'request': request
            }
        ).data
    )

import secrets

from django.shortcuts import redirect, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers

from links.models import ShortenedLink


class ShortenedLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortenedLink
        fields = (
            'destination',
            'short_name'
        )
        extra_kwargs = {
            'short_name': {'required': False}
        }


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
        while True:
            short_name = secrets.token_urlsafe()
            if short_name not in existed_short_names:
                break

    new_link = ShortenedLink.objects.create(
        destination=destination,
        short_name=short_name
    )

    return Response(ShortenedLinkSerializer(new_link).data)

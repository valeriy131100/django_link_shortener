from django.contrib import admin

from .models import ShortenedLink


@admin.register(ShortenedLink)
class ShortenedLinkAdmin(admin.ModelAdmin):
    pass

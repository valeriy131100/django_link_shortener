from django.db import models

from links.validators import validate_url_exists


class ShortenedLink(models.Model):
    destination = models.URLField(
        verbose_name='Куда ведет',
        max_length=200,
        validators=[validate_url_exists]
    )
    short_name = models.CharField(
        verbose_name='Короткое имя',
        max_length=50,
        unique=True
    )

    class Meta:
        verbose_name = 'Сокращенная ссылка'
        verbose_name_plural = 'Сокращенные ссылки'

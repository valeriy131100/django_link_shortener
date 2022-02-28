from django.db import models


class ShortenedLink(models.Model):
    destination = models.URLField(verbose_name='Куда ведет')
    short_name = models.CharField(
        verbose_name='Короткое имя',
        max_length=50,
        unique=True
    )

    class Meta:
        verbose_name = 'Сокращенная ссылка'
        verbose_name_plural = 'Сокращенные ссылки'

# Generated by Django 4.0.2 on 2022-03-02 07:09

from django.db import migrations, models
import links.validators


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0002_alter_shortenedlink_destination'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortenedlink',
            name='destination',
            field=models.URLField(validators=[links.validators.validate_url_exists], verbose_name='Куда ведет'),
        ),
    ]
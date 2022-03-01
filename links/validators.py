import requests
from django.core.exceptions import ValidationError


def validate_url_exists(url):
    try:
        response = requests.head(url)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        raise ValidationError(f'Url "{url}" is not valid.')

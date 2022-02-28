from django.urls import path, include

from .views import make_link

urlpatterns = [
    path('makelink/', make_link)
]

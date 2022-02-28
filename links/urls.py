from django.urls import path

from .views import make_link, go_link

urlpatterns = [
    path('makelink/', make_link),
    path('<str:short_name>/', go_link)
]

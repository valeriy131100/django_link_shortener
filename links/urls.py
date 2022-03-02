from django.urls import path

from .views import make_link, go_link, index

urlpatterns = [
    path('', index, name='index'),
    path('makelink/', make_link, name='make_link'),
    path('<str:short_name>/', go_link, name='go_link')
]

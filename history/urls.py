from django.urls import path
from . import views_html

urlpatterns = [
    path('', views_html.list_history, name='list_history'),
]
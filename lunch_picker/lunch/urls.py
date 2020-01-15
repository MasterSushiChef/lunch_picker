from django.urls import path

from . import views

app_name = 'lunch'
urlpatterns = [
  path('', views.index, name='index'),
]

from django.urls import path
from . import views

app_name = '<app name>' # for namespacing
urlpatterns = [
    path('', views.index, name='index')
]
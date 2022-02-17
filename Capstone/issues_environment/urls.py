from unicodedata import name
from django.urls import path
from . import views

app_name = 'issues-environment' # for namespacing
urlpatterns = [
    path('', views.index, name='index'),
    path('get-info/', views.get_info, name='get_info'),
]
from django.urls import path
from . import views

app_name = 'issues-environment' # for namespacing
urlpatterns = [
    path('', views.index, name='index')
]
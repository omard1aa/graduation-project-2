from django.conf.urls import url, include
from django.urls import path
from . import views

app_name = 'Home'
urlpatterns = [
        path('',views.index, name='index'),
]


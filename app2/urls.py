from app2.views import *
from django.urls import path
app_name='app2'
urlpatterns=[
    path('kanna/',kanna,name='kanna'),
]
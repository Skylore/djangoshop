from django.urls import path, include
from .views import *

urlpatterns = [
    path('', post_list, name='post_list_url'),
    path('post/<str:slug>', post_details, name='post_details_url')
]

# from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home ,name="homepage"),
    path('test/',test,name="test"),
]

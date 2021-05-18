from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('' , home, name="home"),
    path('search', search, name="search"),
    path('<int:bookId>',bookDetails,name="bookDetail")
]
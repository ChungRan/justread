from django.urls import path, include
from . import views
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    path('', views.test, name="bookPost"),
    # path('book/', BookListAPIView.as_view(), name="bookAPI"),
]

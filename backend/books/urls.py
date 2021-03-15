from django.urls import path, include
from books.views import BookAPI
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    # path('', BookPost.as_view(), name="bookPost"),
    path('<int:id>', BookAPI.as_view(), name="bookAPI"),
    # path('<int:id>/simple', BookSimple.as_view(), name="bookSimple"),
]

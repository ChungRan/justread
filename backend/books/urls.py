from django.urls import path, include
from books.views import BookListAPIView, BookDetailAPIView
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    # path('', BookPost.as_view(), name="bookPost"),
    path('book/', BookListAPIView.as_view(), name="bookAPI"),
    path('book/<int:id>/', BookDetailAPIView.as_view(), name="bookAPIId"),
    # path('<int:id>/simple', BookSimple.as_view(), name="bookSimple"),
]

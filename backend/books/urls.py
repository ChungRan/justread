from django.urls import path, include
from books.views import BookListAPIView, BookDetailAPIView, AuthorListAPIView, AuthorDetailAPIView, AuthorSearchAPIView
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    # path('', BookPost.as_view(), name="bookPost"),
    path('book/', BookListAPIView.as_view(), name="bookAPI"),
    path('book/<int:id>/', BookDetailAPIView.as_view(), name="bookAPIId"),
    # path('<int:id>/simple', BookSimple.as_view(), name="bookSimple"),
    path('author/', AuthorListAPIView.as_view(), name="authorAPI"),
    path('author/<int:id>/', AuthorDetailAPIView.as_view(), name="authorAPIId"),
    path('author/search/', AuthorSearchAPIView.as_view(), name="authorAPIId"),

]

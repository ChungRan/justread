from django.urls import path, include
from books import views
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    # path('', BookPost.as_view(), name="bookPost"),
    path('book/', views.BookListAPIView.as_view(), name="bookAPI"),
    path('book/<int:id>/', views.BookDetailAPIView.as_view(), name="bookAPIId"),
    # path('<int:id>/simple', BookSimple.as_view(), name="bookSimple"),
    path('author/', views.AuthorListAPIView.as_view(), name="authorAPI"),
    path('author/<int:id>/', views.AuthorDetailAPIView.as_view(), name="authorAPIId"),
    path('author/search/', views.AuthorSearchAPIView.as_view(), name="authorAPIId"),

]

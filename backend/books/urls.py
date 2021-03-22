from django.urls import path, include
from books import views
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    # path('', BookPost.as_view(), name="bookPost"),
    path('book/', views.BookListAPIView.as_view(), name="bookAPI"),
    path('book/id/<int:id>/', views.BookDetailAPIView.as_view(), name="bookAPIId"),
    path('book/string/', views.BookStringListAPIView.as_view()),
    path('book/string/<int:id>', views.BookStringDetailAPIView.as_view()),
    # path('<int:id>/simple', BookSimple.as_view(), name="bookSimple"),

    path('author/', views.AuthorListAPIView.as_view(), name="authorAPI"),
    path('author/id/<int:id>/', views.AuthorDetailAPIView.as_view(), name="authorAPIId"),
    path('author/string/', views.AuthorStringListAPIView.as_view(), name="authorAPIString"),

]

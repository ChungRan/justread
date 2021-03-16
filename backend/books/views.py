from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from .models import Book
import json
from django.shortcuts import get_object_or_404
from django.http import Http404
from .serializers import BookSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

class BookDetailAPIView(APIView):
    def get(self, request, id):
        # book = Book.objects.get(book_number = id)
        book = get_object_or_404(Book, book_number = id)
        bookJson = BookSerializer(book).data
        returnJson = {
            'book' : bookJson
        }
        # return JsonResponse(returnJson)
        return Response(data = returnJson)

    def put(self, request, id):
        book = Book.objects.get(book_number = id)
        serializer = BookSerializer(book, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(data = serializer.errors, status = 400)

    def delete(self, request, id):
        # 작동안함
        book = Book.objects.get(book_number = id)
        book.delete()
        print("디버깅 삭제 확인", id)
        return Response(status = status.HTTP_204_NO_CONTENT)

class BookListAPIView(APIView):
    def get(self, request):
        return

    # def post(self, request):
        #post는 다른 url로 옮기기
        # if request.META['CONTENT_TYPE'] == "application/json":
        #     request = json.loads(request.body)
        #     newBook = Book(title = request['title'],
        #                    ISBN = request['ISBN'])
        # else:
        #     newBook = Book(title = request.POST['title'],
        #                    ISBN = request.POST['ISBN'])
        # newBook.save()
        # return HttpResponse(status=200)
    def post(self, request):
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data, status=201)
        # print("디버깅", serializer.data)
        return Response(data = serializer.errors, status = 400)
from rest_framework import serializers
from .models import Book, Author

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

# class BookStringSerializer(serializers.Serializer):
#     title = serializers.TextField(help_text = "책 제목")
#     author = serializers.TextField(help_text = "작가 이름")

    
        
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

# class AuthorStringSerializer(serializers.Serializer):
#     name = serializers.TextField(help_text = "작가 이름")
    
from rest_framework import serializers

from book.models import Book, Author


class AuthorCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('first_name', 'last_name')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'description', 'author', 'discount_price')

    author = serializers.StringRelatedField()
    discount_price = serializers.SerializerMethodField(method_name='discount')

    def discount(self, book: Book):
        return book.price * 25 / 100

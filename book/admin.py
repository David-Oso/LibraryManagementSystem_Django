from django.contrib import admin

from book.models import Author, BookInstance, Book

# Register your models here.

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookInstance)

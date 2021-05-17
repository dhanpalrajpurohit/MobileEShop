from django.contrib import admin
from .models import book_details,author_details
# Register your models here.
admin.site.register(book_details)
admin.site.register(author_details)
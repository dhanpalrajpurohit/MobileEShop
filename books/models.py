from django.db import models

# Create your models here.
class book_details(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length = 255)
    book_author = models.CharField(max_length = 255)
    book_detail = models.CharField(max_length = 255)
    book_price = models.IntegerField(max_length=255)
    book_image = models.ImageField(upload_to='media')
    book_type = models.CharField(max_length = 255)
    book_publish = models.IntegerField(max_length = 255)
    book_isbn = models.CharField(max_length = 255)
    book_category = models.CharField(max_length = 255)
    def __str__(self):
        return self.book_name;

class author_details(models.Model):
    author_id = models.AutoField(primary_key = True)
    author_name = models.CharField(max_length=255)
    author_image = models.ImageField(upload_to='media/author')

    def __str__(self):
        return self.author_name
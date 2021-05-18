from django.shortcuts import render
from .models import book_details,author_details
# Create your views here.
def search(request):
    return render(request,'searchResult.html')

#@login_required
def home(request):
    #if request.method == "POST":
    bookDetail = book_details.objects.all()
    authorDetail = author_details.objects.all()
    data = {
        'books':bookDetail,
        'authors':authorDetail
    }
    return render(request, 'index.html', data)
    #else:
    #   return render(request,'index.html')

def bookDetails(request,bookId):
    bookDetails = book_details.objects.all().filter(book_id=bookId)
    print(bookDetails)
    data = {
        'bookDetail':bookDetails
    }
    return render(request, 'bookdetail.html', data)
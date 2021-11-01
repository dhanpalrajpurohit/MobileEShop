from django.shortcuts import render
from .models import book_details,author_details
# Create your views here.
def search(request):
    return render(request,'base.html')

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
def temp(request):
    authorDetail = author_details.objects.all()
    data = {
        'authors':authorDetail
    }
    return render(request, 'home.html', data)
    

def bookDetails(request,bookId):
    bookDetails = book_details.objects.all().filter(book_id=bookId)
    allBook = book_details.objects.exclude(book_id=bookId)
    print(allBook)
    data = {
        'bookDetail':bookDetails,
        'allbooks':allBook
    }
    return render(request, 'bookdetail.html', data)
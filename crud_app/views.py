from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book
# Create your views here.
def home(request):
    if request.method == 'POST':
        form = BookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    books = Book.objects.all()
    form = BookForm()
    context = {
        'books':books,
        'form':form,
    }
    return render(request,'home.html',context)


def deletion(request,id):
    kitob = Book.objects.get(id=id)
    kitob.delete()
    return redirect('/')

def updation(request,id):
    kitob = Book.objects.get(id=id)
    context = {
        'kitob':kitob,
    }
    if request.method == 'POST':
        name = request.POST['name']
        author = request.POST['author']
        # year =  request.POST['year']
        pages = request.POST['pages']
        image = request.POST['image']

        kitob.name =name
        kitob.author = author
        kitob.pages = pages
        kitob.image = image
        kitob.save()
        return redirect('/')
    return render(request,'edit.html',context)
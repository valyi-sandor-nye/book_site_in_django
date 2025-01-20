from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from book_app.models import  Author, Book



def index(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    return HttpResponse(loader.get_template('index.html').render({
        'authors': authors,
        'female_authors': [author for author in authors if author.is_female],
        'books': books,
        'books_of_female_writers': [book for book in books if book.author.is_female],
    }, request))

def add_author(request):
    return HttpResponse(loader.get_template('author.html').render({}, request))

def add_author_record(request):
    Author(name=request.POST.get('name'), is_female=request.POST.get('is_female') == 'on').save()
    return HttpResponseRedirect(reverse('index'))


def update_author(request, id):
    return HttpResponse(loader.get_template('author.html').render({'author': Author.objects.get(id=id)}, request))


def update_author_record(request, id):
    author = Author.objects.get(id=id)
    author.name = request.POST.get('name')
    author.is_female = request.POST.get('is_female') == 'on'
    author.save()
    return HttpResponseRedirect(reverse('index'))

def delete_author(request, id):
    Author.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('index'))

def add_book(request):
    return HttpResponse(loader.get_template('book.html').render({
        'authors': Author.objects.all(),
    }, request))

def add_book_record(request):
    Book(
        title=request.POST.get('title'),
        is_available=request.POST.get('is_available') == 'on',
        author=Author.objects.get(id=request.POST.get('author_id'))
    ).save()
    return HttpResponseRedirect(reverse('index'))


def update_book(request, id):
    return HttpResponse(loader.get_template('book.html').render({
        'title': Book.objects.get(id=id).title,
        'book': Book.objects.get(id=id),
        'authors': Author.objects.all()
    }, request))


def update_book_record(request, id):
    book = Book.objects.get(id=id)
    book.name = request.POST.get('title')
    book.is_available = request.POST.get('is_available') == 'on'
    book.author = Author.objects.get(id=request.POST.get('author_id'))
    book.save()
    return HttpResponseRedirect(reverse('index'))

def delete_book(request, id):
    Book.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('index'))

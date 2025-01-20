from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('author/add/', views.add_author),
    path('author/add/addrecord', views.add_author_record),
    path('author/update/<int:id>', views.update_author),
    path('author/update/updaterecord/<int:id>', views.update_author_record),
    path('author/delete/<int:id>', views.delete_author),
    path('book/add/', views.add_book),
    path('book/add/addrecord', views.add_book_record),
    path('book/update/<int:id>', views.update_book),
    path('book/update/updaterecord/<int:id>', views.update_book_record),
    path('book/delete/<int:id>', views.delete_book)
]
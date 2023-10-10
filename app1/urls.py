from django.urls import path 
from app1.views import *

urlpatterns = [
    path('add_book/',add_book,name="add_book"),
    path('showbook',show_book,name="show_book"),
    path('loanBook',loanBook,name='loanBook'),
    path('returnBook',returnBook,name='returnBook'),
    path('wishlistbook',wishlistbook, name='wishlistbook')
]

from django import forms
from .models import books,loan,returnbook,wishlist

class BookForm(forms.ModelForm):
    class Meta:
        model = books
        fields = ['title','author','publication_date','genre','ISBN']
        widgets = {
            'genre': forms.RadioSelect
        }

class LoanForm(forms.ModelForm):
    class Meta:
        model = loan
        fields = ['book', 'user', 'due_date', 'returned_date']

class ReturnBookForm(forms.ModelForm):
    class Meta:
        model = returnbook
        fields = '__all__'

class wishlistForm(forms.ModelForm):
    class Meta:
        model = wishlist
        fields = '__all__'
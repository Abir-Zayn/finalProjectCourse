from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from .forms import *
from .models import *

def HomePage(request):
    return render(request, 'home.html')

def SignupPage(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        user_mail = request.POST.get('user_mail')
        user_password = request.POST.get('password1')
        user_confirm_password = request.POST.get('password2')
        
        if user_password != user_confirm_password:
            messages.error(request, 'Passwords do not match')
            return render(request, 'signup.html')
        else:
            my_user = User.objects.create_user(user_name, user_mail, user_password)
            my_user.save()
            return redirect('login')

    return render(request, 'signup.html')

def LoginPage(request):
    if request.method == "POST":
        user_name = request.POST.get('username')
        user_password = request.POST.get('pass')
        user = authenticate(request, username=user_name, password=user_password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('Username or password is invalid')
    return render(request, 'login.html')

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_book')
    else:
        form = BookForm()
    return render(request, 'add_books.html', {'form': form})

def show_book(request):
    if 'search' in request.GET:
        search_val = request.GET['search']
        data = books.objects.filter(title__icontains=search_val)
    else:
        data = books.objects.all()
    context ={
        'data': data
    }
    return render(request,'showbook.html',context)

def loanBook(request):  
    if request.method == 'POST':
        loan_form = LoanForm(request.POST)

        if loan_form.is_valid():
            loan = loan_form.save()

            book = books.objects.get(pk=loan.book.pk)
            if book.quantity>0:
                book.quantity -= 1
                book.save()
                return redirect('show_book')
    else:
        loan_form = LoanForm()


    return render(request, 'loanBook.html', {'loan_form':loan_form})

def returnBook(request):
    if request.method== 'POST':
        return_form = ReturnBookForm(request.POST)
        
        if return_form.is_valid():
            returnbook = return_form.save()
            
            book = books.objects.get(pk=returnbook.book.pk)
            if book.quantity <=10:
                book.quantity += 1
                book.save()
                return redirect('show_book')
    else:
        return_form = ReturnBookForm()
    
    return render(request, 'returnbook.html',{'return_form':return_form}) 
        
def wishlistbook(request):
    if request.method == 'POST':
        form = wishlistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('wishlistbook')
    else:
        form = wishlistForm()
    
    wishbook = wishlist.objects.all()
    return render(request, 'wishlist.html', {'req_form': form,'wish':wishbook})
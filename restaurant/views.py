from django.shortcuts import render, redirect
from django.http import HttpResponse
from restaurant.models import Bookings
from restaurant.forms import BookingForm
from django.contrib.auth import authenticate, login, logout 
from .forms import SignupForm, LoginForm



# Create your views here.
def my_restaurant(request):
    bookings = Bookings.objects.all()
    return render(request, "index.html", {'bookings': bookings})



def book_table(request):
    # Add logic to book table
    form = BookingForm()
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.save()
            return redirect('restaurant')

    return render(request, "booking.html", {"form": form})


def cancel_booking(request, id=3):
    
    details = {}
    # Add logic to cancel booking
    booking = Bookings.objects.get(id = id)
    if request.method == "POST":
        booking.delete()
        
        
        return redirect('restaurant')

    return render(request, "cancel_booking.html", details)
    
    

def amend_booking(request, id=2):
    # Add logic to amend booking
    details ={}
    # fetch the object related to passed id
    booking = Bookings.objects.get(id = id)
    booking.no_of_persons = 7
    
 
    # pass the object as instance in form
    form = BookingForm(request.POST or None, booking)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return redirect('restaurant')
 
    # add form dictionary to context
    details["form"] = form
    
    return render(request, "amend_booking.html", {'form': form})
    

def user_login(request):
    #Add a logic to login 
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('restaurant')
    
        
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

def user_signup(request):
    #Add a logic to signup
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'sign_up.html', {'form': form})


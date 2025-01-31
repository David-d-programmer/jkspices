from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Post
from django.contrib import messages
from django.http import HttpResponse
from restaurant.models import Bookings
from restaurant.forms import BookingForm
from django.http import Http404
from django.contrib.auth import authenticate, login, logout 
from .forms import SignupForm, LoginForm
import time


# Create your views here.

class Postlist(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "restaurant/index.html"

def restaurant_home(request):
    return render(request, 'restaurant/home.html')

def about(request):
    return render(request, 'restaurant/about.html')
    
def menu(request):
    return render(request, 'restaurant/menu.html')

def contact(request):
    return render(request, 'restaurant/contact.html')

def submit_form(request):
    return render(request, 'submit_form.html')

def my_restaurant(request):
    bookings = Bookings.objects.all()
    return render(request, "index.html", {'bookings': bookings})





def book_table(request):
    # Add logic to book table
    form = BookingForm
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            
            #user = form.cleaned_data['user']
            user_email = form.cleaned_data['user_email']
            #time = form.cleaned_data['time']
            booking_time = form.cleaned_data['booking_time']
            user = authenticate(request, user_email=user_email, time=time)
            if user:
                book_table(request, user)    
                return redirect('restaurant')

            #checking if the table is already booked
            if Bookings.objects.filter(user=user, booking_time=booking_time, user_email=user_email).exists():
                messages.error(request, 'This table is already booked for this time')
            else:
                form.save()
                messages.success(request, 'Your table has been booked successfully')
            

            return redirect('booking_confirmation')
        else:
            form = BookingForm
        

    return render(request, "restaurant/booking.html", {"form": form})

def booking_confirmation(request):
    # Assuming you have a way of getting the current booking (e.g., from the session or last saved booking)
    booking = Bookings.objects.last()  # Or use another method to fetch the correct booking
    
    if not booking:
        messages.error(request, "No booking found.")
        return redirect('restaurant')  # Or wherever you want to redirect if there's no booking
    
    return render(request, 'restaurant/booking_confirmation.html', {'booking': booking})


def cancel_booking(request, id):
    # Get the booking, or return a 404 if not found
    booking = get_object_or_404(Bookings, id=id)
    
    if request.method == "POST":
        # Cancel the booking by deleting it
        booking.delete()
        return redirect('restaurant')  # Make sure 'restaurant' URL pattern exists

    # Render the cancel booking page with optional context (if needed)
    return render(request, "restaurant/cancel_booking.html")
    
    

def amend(request, id):
    try:
        # Fetch the booking object by ID
        booking = Bookings.objects.get(id=id)
    except Bookings.DoesNotExist:
        # Handle the case where the booking doesn't exist (e.g., 404 error)
        raise Http404("Booking not found")
    
    # Initialize form with the booking instance
    form = BookingForm(request.POST or None, instance=booking)
    
    if form.is_valid():
        # Save the updated form
        form.save()
        # Redirect to the booking list or a confirmation page
        return redirect('restaurant')  # or redirect('restaurant:booking_detail', id=booking.id)
    
    # Add the form to context and render the template
    return render(request, "restaurant/amend_booking.html", {'form': form})


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
    
        
    return render(request, 'restaurant/login.html', {'form': form})

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
    return render(request, 'restaurant/sign_up.html', {'form': form})


def avoid_doublebooking(request):
        #add the request in the ModelForm
        form = BookingForm(request or None)
        #self.request = kwargs.pop('request', None)
        #call the default super
        #super(BookingForm, self).avoid_doublebooking(*args, **kwargs)
        if form.is_valid():

            cleaned_data = form.clean()
            name = cleaned_data.get('name')
            client = cleaned_data.get('client')

            return redirect('restaurant')
        
            try:
                Bookings.objects.get(name=name, author=author, borrower=borrower)

            except Bookings.DoesNotExist:
                return cleaned_data()

        else:
            raise avoid_doublebooking('The client already booked')

        return render(request, 'restaurant/avoid_doublebooking.html', {'form':form})
        
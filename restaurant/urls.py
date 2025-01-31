from django.urls import path
from . import views  # Use views instead of restaurant_views

urlpatterns = [
    path('', views.restaurant_home, name='restaurant'),  # A pattern for the restaurant home
    path('book_table/', views.book_table, name='book_table'),
    path('booking_confirmation/', views.booking_confirmation, name='booking_confirmation'),
    path('cancel_booking/<int:id>/', views.cancel_booking, name='cancel_booking'),
    path('restaurant/amend/<int:id>/', views.amend, name='amend'),
    path('about/', views.about, name='about'),  # Example About page
    path('menu/', views.menu, name='menu'),  # Example Menu page
    path('contact/', views.contact, name='contact'), 
    path('login/', views.user_login, name='login'),  # Ensure the user_login view exists in views.py
    path('signup/', views.user_signup, name='signup'),  # Ensure the user_signup view exists in views.py
    path('logout/', views.user_logout, name='logout'),  # Ensure the user_logout view exists in views.py
    path('submit/', views.submit_form, name='submit_form'),
]

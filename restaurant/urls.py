

from django.urls import path
from . import views

urlpatterns = [
    path('', views.restaurant_home, name='restaurant'),  # A pattern for the restaurant home
    path('book_table/', views.book_table, name='book_table'),
    path('booking_confirmation/', views.booking_confirmation, name='booking_confirmation'),
    path('cancel_booking/<id>', views.cancel_booking, name='cancel_booking'),
    path('amend/<id>', views.amend_booking, name='amend'),
]

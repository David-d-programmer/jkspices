"""
URL configuration for jkspices project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from restaurant import views as restaurant_views





urlpatterns = [
    path('restaurant/', include('restaurant.urls'), name='restaurant-urls'),
    path('book_table/', restaurant_views.book_table, name='book_table'),
    path('booking_confirmation/', restaurant_views.booking_confirmation, name='booking_confirmation'),
    path('cancel_booking/<id>', restaurant_views.cancel_booking, name='cancel_booking'),
    path('amend/<id>', restaurant_views.amend_booking, name='amend'),
    path('login/', restaurant_views.user_login, name='login'),
    path('signup/', restaurant_views.user_signup, name='signup'),
    path('logout/', restaurant_views.user_logout, name='logout'),
    path('admin/', admin.site.urls),
]

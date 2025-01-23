from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('', views.Postlist.as_view(), name='post-list'),
    
]
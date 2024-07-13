from django.db import models
from django.contrib.auth.models import User



# Create your models here.


class Bookings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    user_email = models.EmailField()
    
    group_size = models.PositiveIntegerField()
    booking_date = models.DateField()
    
    booking_time = models.TimeField(auto_now_add=False, blank=False)
    
    # comment = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)








    
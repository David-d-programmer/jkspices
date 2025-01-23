from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='posts/images/', blank=True, null=True)
    reservation = models.URLField(max_length=200, blank=True, null=True)
    contact = models.CharField(max_length=100)
    special_offers =models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=1)

    class Meta:
        ordering = ["created_on"]
    def __str__(self):
        return (self.title)     


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]
    def __str__(self):
        return (self.body)
    

class Bookings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    user_email = models.EmailField()
    
    group_size = models.PositiveIntegerField()
    booking_date = models.DateField()
    
    booking_time = models.TimeField(auto_now_add=False, blank=False, max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)








    
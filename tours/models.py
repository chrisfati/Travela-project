from django.db import models
from django.contrib.auth.models import User  # optional if you want user accounts

class Tour(models.Model):
    name = models.CharField(max_length=100)
    days = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField() 
    image = models.ImageField(upload_to='tours/', null=True, blank=True, db_column='image_url')  

    def __str__(self):
        return self.name


class Booking(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    people = models.PositiveIntegerField()  
    payment_method = models.CharField(max_length=50)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking for {self.tour.name} by {self.customer_name}"

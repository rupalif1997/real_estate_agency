from django.db import models
from django.contrib.auth.models import User
from listings.models import listings


class Msg(models.Model):
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact=models.BigIntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    apartment_size = models.CharField(max_length=50) 
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

#
#
#
#
#
#
#
#
#

class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    listing = models.ForeignKey(listings, on_delete=models.CASCADE)
    customer = models.ForeignKey(Msg, on_delete=models.CASCADE)

    def __str__(self):
        return f"Payment of {self.amount} for {self.listing.title} by {self.customer.first_name} {self.customer.last_name}"
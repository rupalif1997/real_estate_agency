from django.db import models

# Create your models here. username== rupaliM  password== agastya@0111


class listings(models.Model):
    contact=models.CharField(max_length=20)
    title=models.CharField(max_length=150)
    price=models.IntegerField()
    num_bedrooms=models.IntegerField()
    num_bathrooms=models.IntegerField()
    square_footage=models.IntegerField()
    address=models.CharField(max_length=150)
    image = models.ImageField()
   

    def __str__(self):
        return self.title
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

class Payment_tb(models.Model):
    listing = models.ForeignKey('listings', on_delete=models.CASCADE)
    amount = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    razorpay_payment_id = models.CharField(max_length=255)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.listing.title} - {self.amount} INR - {self.timestamp}"
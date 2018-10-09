
from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=256, )
    last_name = models.CharField(max_length=256, )
    street_address = models.CharField(max_length=256, )
    # this would in reality have choices filled in
    state = models.CharField(max_length=256, )
    zip = models.IntegerField()

class Product(models.Model):
    name = models.CharField(max_length=256, )
    # I'm assuming amount is a property of the product and not specific to the purchase
    amount = models.FloatField()

class Purchase(models.Model):
    purchase_time = models.DateTimeField()
    status = models.CharField(max_length=8, choices=(('new', 'new'), ('canceled', 'canceled'),))

    customer = models.ForeignKey(Customer, on_delete='cascade')
    product = models.ForeignKey(Product, on_delete='cascade')

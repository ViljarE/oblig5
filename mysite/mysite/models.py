from django.db import models
class Car(models.Model):
    make = models.CharField(max_length=50)
    carmodel = models.CharField(max_length=50)
    year = models.CharField(max_length=50, default="0")
    location = models.CharField(max_length=50, default= None)
    status = models.CharField(max_length=50, default= None)
    bookedBy = models.IntegerField(default= 0) # no user has 0 as id

    def __str__(self):
        return self.make + ' ' + self.carmodel + ' ' + self.year + ' ' + self.location + ' ' + self.status





class Customer(models.Model):
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    cars = models.IntegerField(default=0) # tells you if customer has booked a car, 0 = False, 1 = True
    bookedCar = models.IntegerField(default= 0) # no car has 0 as id


    def __str__(self):
        return self.name + ' ' + self.age + ' ' + self.address



class Employee(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)

    def __str__(self):
        return self.name + ' ' + self.address + ' ' + self.branch
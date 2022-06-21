from django.db import models

# Create your models here.


class Student(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    class Meta:
        db_table = "SOS_STUDENT"

class Employee(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    class Meta:
        db_table = "SOS_EMPLOYEE"

class Vehicle(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    class Meta:
        db_table = "VEHICLE"

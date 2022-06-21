from django.test import TestCase
from .models import Student

class TestModel(TestCase):
    form = Student(firstName = "Shyammm", lastName = "Sharma", email ="Shyam@gmail.com", password = "1234" )
    form.save()
    print("Data Saved")


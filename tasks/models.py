from select import select
from time import sleep
from django.db import models

# Create your models here.
class Student(models.Model):
    Student_ID = models.IntegerField()
    Student_fname = models.CharField(max_length=200)
    Student_lname = models.CharField(max_length=100)
    Birth_Date = models.DateField(auto_now_add=False)
    select_gender = (
    ('male','Male'),
    ('female', 'Female'),)
    Gender = models.CharField(max_length=50 ,choices=select_gender)
    description = models.TextField(max_length=500)
    def __str__(self):
        return self.Student_fname + " " + str(self.Birth_Date)


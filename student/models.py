from django.db import models

# Create your models here.

class Student(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    age = models.BigIntegerField()
    state = models.CharField(max_length=255)


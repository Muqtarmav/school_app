from django.db import models

# Create your models here.
class Teacher(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    state = models.CharField(max_length=255)





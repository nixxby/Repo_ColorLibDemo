from django.db import models

# Create your models here.
class User(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50,default="Shah")
    email = models.EmailField(max_length=50)
    pwd = models.CharField(max_length=10)
    def __str__(self):
        return self.fname + self.lname

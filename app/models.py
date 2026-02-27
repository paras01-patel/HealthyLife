from django.db import models

# Create your models here.


class cont(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.CharField(max_length=50)
    message=models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.name
    
class signn(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField()
    password1=models.CharField(max_length=50)
    password2=models.CharField(max_length=50)    
        
from django.db import models
from django.contrib.auth.models import User

   
class Master(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Courses(models.Model):
    master = models.ForeignKey(Master, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    lat = models.FloatField()
    long = models.FloatField()
    
 

    
    

class UserProfile(models.Model):
    OPTIONS = (
        ('O1', '3A Ecole'),
        ('O2', '3A M2 imbriques stage M2 et PFE'),
        ('O3', '3A M2 imbriques 3 cours supplementaires'),
        ('O4', '3A M2 imbriques 2 cours 1 projet'),
    )
    option = models.CharField(max_length=2, choices=OPTIONS)
    master = models.ForeignKey(Master, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

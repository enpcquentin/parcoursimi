from django.db import models
from django.contrib.auth.models import User

   
class Master(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField()
    def __str__(self):
        return self.name

        
class Courses(models.Model):
    OPTIONS = (
        ('Mo', 'Lundi'),
        ('Tu', 'Mardi'),
        ('We', 'Mercredi'),
        ('Th', 'Jeudi'),
        ('Fr', 'Vendredi'),
    )
    master = models.ForeignKey(Master, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    lat = models.FloatField()
    long = models.FloatField()
    ects = models.FloatField()
    semester = models.PositiveSmallIntegerField()
    days = models.CharField(max_length=2, choices=OPTIONS)
    duration = models.PositiveSmallIntegerField()
  
class Option(models.Model):
    name = models.CharField(max_length=300)
    def __str__(self):
        return self.name

class UserProfile(models.Model):
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    master = models.ForeignKey(Master, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Courses) 
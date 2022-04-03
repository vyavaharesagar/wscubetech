from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to='static/assets/img/team',default='')
    twitter = models.CharField(max_length=50)
    facebook = models.CharField(max_length=50)
    instagram = models.CharField(max_length=50)
    linkedin = models.CharField(max_length=50)


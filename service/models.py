from django.db import models


# Create your models here.

class Service(models.Model):
    service_icon = models.CharField(max_length=50)
    service_title = models.CharField(max_length=50)
    service_desc = models.TextField()
    service_img = models.ImageField(upload_to='static/assets/img/portfolio',default='')

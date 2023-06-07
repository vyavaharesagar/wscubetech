from django.db import models
from django.contrib.auth.models import User

class Break(models.Model):
    BREAK_TYPES = (
        ('Lunch', 'Lunch Break'),
        ('Tea', 'Tea Break'),
        ('Meeting', 'Meeting Break'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    break_type = models.CharField(max_length=10, choices=BREAK_TYPES)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

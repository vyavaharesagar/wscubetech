from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Lead(models.Model):
    name = models.CharField(max_length=50, null=True)
    mobile_number = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50,null=True)

    NO = "None"
    RNR = "RNR"
    HU = "HU"
    LD = "LD"
    CB = "CB"
    NC = "NC"
    CBWP = "CBWP"
    SW = "SW"
    NI = "NI"
    WN = "WN"
    PD = "PD"
    DND = "DND"

    __DEPOSITION_LIST = [
        ( RNR ,"RNR-Ringing"),
        ( HU , "HU-hangup"),
        ( LD , "LD-Live demo"),
        ( CB ,"CB-Call back"),
        ( NC , "NC-Not connected"),
        ( CBWP, "CBWP-Call back without presentation"),
        ( SW , "SW-Switch off"),
        ( NI , "NI-Not Intrested"),
        ( WN , "NI—wrong number"),
        ( PD , "PD-Paid"),
        ( DND ,"DND-Do not disturb"),
        ( NO ,"None"),
    ]

    diposition = models.CharField(max_length=50,choices=__DEPOSITION_LIST,default=NO)
    remark = models.CharField(max_length=50,null=True)
    status = models.CharField(max_length=50,null=True)
    agent = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    follow_up_date = models.DateField()


    def __str__(self):
        return self.name



class LeadHistory(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    disposition = models.CharField(max_length=50,null=True,default="None")
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE)
    modified_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.lead} - {self.status}"
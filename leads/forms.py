from django.forms import ModelForm
from leads.models import Lead


class LeadRegistrationForm(ModelForm):

    class Meta:
        model = Lead
        fields = ['name','mobile_number','email','diposition','remark','status','agent','follow_up_date']
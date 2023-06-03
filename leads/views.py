from django.shortcuts import render, redirect

# Create your views here.
from .forms import LeadRegistrationForm
from .models import Lead
from django.contrib import messages
from wscubetech.decorators import unauhenticated_user, allowed_users,admin_only

@admin_only
def lead_registration(request):
    # print(request.POST)
    form = LeadRegistrationForm()
    print(form)
    if request.method == "POST":
        form = LeadRegistrationForm(request.POST)
        if form.is_valid():
            lead = form.save()
            print(lead)
            messages.success(request, 'Lead has been registrated ')
            return redirect('lead_registration')

    context = {'form': form ,'classlr':'active'}
    return render(request,'lead_registration.html',context)

def update_lead(request,pk):
    print(pk)
    # print("hello")
    lead = Lead.objects.get(id=pk)
    form = LeadRegistrationForm(instance=lead)

    if request.method == "POST":
        form = LeadRegistrationForm(request.POST,instance=lead)
        if form.is_valid():
            lead = form.save()
            print(lead)
            messages.success(request, 'Lead has been Updated ')
            return redirect('follow_up')

    context = {'form': form }
    return render(request,'edit_customer_data.html',context)

def delete_lead(request,pk):
    print(pk)
    lead = Lead.objects.get(id=pk)
    lead.delete()
    messages.success(request, 'Lead has been Deleted ')
    return redirect('follow_up')
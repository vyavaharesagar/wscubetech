from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .forms import LeadRegistrationForm
from .models import Lead, LeadHistory
from django.contrib import messages
from wscubetech.decorators import unauhenticated_user, allowed_users,admin_only
from django.contrib.auth.decorators import login_required

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
            messages.success(request, 'Lead has been registrated')
            return redirect('lead_registration')

    context = {'form': form ,'classlr':'active'}
    return render(request,'lead_registration.html',context)

# def update_lead(request,pk):
#     print(pk)
#     # print("hello")
#     lead = Lead.objects.get(id=pk)
#     form = LeadRegistrationForm(instance=lead)

#     if request.method == "POST":
#         form = LeadRegistrationForm(request.POST,instance=lead)
#         if form.is_valid():
#             status = lead.status
#             lead = form.save()
#             LeadHistory.objects.create(
#                 lead=lead,
#                 status=status,
#                 modified_by=request.user
#             )            
#             print(lead)
#             messages.success(request, 'Lead has been Updated')
#             return redirect('follow_up')

    context = {'form': form }
    return render(request,'edit_customer_data.html',context)


@login_required
def delete_lead(request,pk):
    print(pk)
    lead = Lead.objects.get(id=pk)
    lead.delete()
    messages.success(request, 'Lead has been Deleted ')
    return redirect('follow_up')

@login_required
def update_lead(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    form = LeadRegistrationForm(instance=lead)
    if request.method == 'POST':
        form = LeadRegistrationForm(request.POST,instance=lead)
        status = request.POST.get('status')
        disposition = request.POST.get('diposition')
        lead.status = status
        lead.diposition = disposition
        lead.save()

        LeadHistory.objects.create(
            lead=lead,
            status=status,
            modified_by=request.user,
            disposition=disposition
        )

        print(lead)
        print(disposition)
        messages.success(request, 'Lead has been Updated')
        return redirect('follow_up')

    return render(request, 'edit_customer_data.html', {'form': form })

@login_required
def show_history(request, lead_id):
    lead = get_object_or_404(Lead, pk=lead_id)
    history = LeadHistory.objects.filter(lead_id=lead_id)
    return render(request, 'history.html', {'lead': lead, 'history': history})
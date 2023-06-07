from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Break
from django.contrib.auth.models import User
from django.contrib import messages

@login_required
def break_list(request):
        # return render(request, 'breaks/access_denied.html')
    users = User.objects.all()

    if not request.user.is_superuser:
        breaks = Break.objects.filter(user=request.user)
    else:
        breaks = Break.objects.all()

    context = {
        'users': users,
        'breaks': breaks,
        'classbreak':"active"
    }
    
    return render(request, 'breaks/break_list.html', context)

@login_required
def create_break(request):
    if request.method == 'POST':
        break_type = request.POST['break_type']
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        user = request.user
        Break.objects.create(user=user, break_type=break_type, start_time=start_time, end_time=end_time)
        messages.success(request, 'Break has been created for ', user)
        return redirect('breaks:break_list')
    return render(request, 'breaks/create_break.html')
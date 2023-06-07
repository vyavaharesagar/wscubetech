from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import UserForm
from service.models import Service
from news.models import News
from team.models import Team
from leads.models import Lead
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from .decorators import unauhenticated_user, allowed_users,admin_only

from .forms import CreateUserForm
from django.contrib import messages

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

@login_required
def paid_customers(request):
    leadData = Lead.objects.filter(status='Paid')
    data = { 'leadData': leadData,'classpc':'active' }
    print(data)
    return render(request,'paid_customers.html',data)

@login_required
def follow_up_leads(request):
    leadData = Lead.objects.all()
    if not request.user.is_superuser:
        leadData = Lead.objects.filter(agent=request.user)
    data = { 'leadData': leadData,'classfollow':'active' }
    print(data.get('name'))
    return render(request,'follow_up_leads.html',data)

def logout_user(request):
    logout(request)
    return redirect('login')

@unauhenticated_user
def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request, "Username OR Password is incorrect")

    return render(request, "login.html")

@login_required(login_url='login')
@admin_only
def signup(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='agent')
            user.groups.add(group)
            messages.success(request, 'Account was created for '+ username)
            return redirect('login')

    context = {'form':form }
    return render(request, "signup.html", context)

@login_required(login_url='login')
@admin_only
def homepage(request):
    # data ={
    #     'title':'Home Page',
    #     'bdata':'Jodhpur',
    #     'clist':['Java', 'Python', 'PHP'],

    #     'numbers' : [10,20,30,40,50],
    #     # 'numbers' : [10,20,30,40,50],
    #     'student_details' : [
    #         {'name':'pradeep','phone':9511832154},
    #         {'name':'rohan','phone':8482867016}
    #     ]
    # }
    # return render(request,"index.html",data)
    leadData = Lead.objects.all()
    data = { 'leadData': leadData, 'class':'active' }
    print(data.get('name'))
    return render(request,"index.html", data)

def index2(request):
    return render(request,"index-2.html")

def index3(request):
    return render(request,"index-3.html")

def index4(request):
    return render(request,"index-4.html")
    
def team(request):
    teamData = Team.objects.all()

    data = {'teamData': teamData}
    print("Team Page Called")

    return render(request,"team.html",data)

def blog(request):
    return render(request,"blog.html")

def contact(request):
    return render(request,"contact.html")

def about(request):
    if request.method == "GET":
        output = request.GET.get('output')
    return render(request,"about.html",{'output':output})
def portfolio(request):
    return render(request,"portfolio.html")
def submitform(request):
    # return render(request,"submitform.html")
    try:
        n1 = int(request.POST['value1'])
        n2 = int(request.POST['value2'])
        # print(n1+n2)
        
        finalans = n1+n2
        data = {
            'n1' : n1,
            'n2' :n2,
            'output':finalans
        }
        # url = "/about-us/?output={}".format(finalans)
        # return HttpResponseRedirect(url)
        # return redirect(url)
        return HttpResponse(finalans)
    except:
        pass
def services(request):

    # serviceData = Service.objects.all().order_by('service_title')
    serviceData = Service.objects.all()
    paginator = Paginator(serviceData,2)
    page_number = request.GET.get('page')
    serviceDataFinal = paginator.get_page(page_number)
    totalpage = serviceDataFinal.paginator.num_pages #3
    # if request.method == "GET":
    #     __icontains
    #     st = request.GET.get('searchtext')
    #     if st!=None:
    #         serviceData = Service.objects.filter(service_title__icontains = st)

    data = { 
            # 'serviceData' : serviceData,
            'lastpage':totalpage,
            'serviceDataFinal':serviceDataFinal,
            'totalpagelist': [n+1 for n in range(totalpage)]
            }
    # print("Services Page Called")
    return render(request,"services.html",data)
def blog_details(request):
    
    return render(request,"blog_details.html")

def userform(request):

    finalans = 0
    fn = UserForm()
    # get method
    # try:
    #     n1 = int(request.GET['value1'])
    #     n2 = int(request.GET['value2'])
    #     # print(n1+n2)
    #     finalans = n1+n2
    # except:
    #     print("no data")
    # return render(request,"userform.html",{'output':finalans})

    # post method
    data = {'form':fn }
    try:
        n1 = int(request.POST['value1'])
        n2 = int(request.POST['value2'])
        # print(n1+n2)
        
        finalans = n1+n2
        data = {
            'fn':fn,
            'output':finalans
        }
        url = "/about-us/?output={}".format(finalans)
        # return HttpResponseRedirect(url)
        return redirect(url)
    except:
        print("no data")
    return render(request,"userform.html",data)

def course(request):
    return HttpResponse("Hello this is course page")

# def courseDetail(request, course_id ):
#     return HttpResponse("This is course detail page " + str (course_id))

# def courseDetailWithStr(request, course_str ):
#     return HttpResponse("This is course detail page " + course_str)

def courseDetailWithAnyType(request, course_name ):
    return HttpResponse("This is course detail page " + course_name)


def calculator(request):
    return render(request,'calculator.html')

def newsDetail(request,slug):
    
    newsDetail = News.objects.get(news_slug=slug)
    # print(newsDetail)
    data = { 
    'newsDetail':newsDetail
    }
    return render(request,"newsdetails.html",data)


@login_required(login_url='login')
def button(request):
    return render(request, "follow_up_leads.html")


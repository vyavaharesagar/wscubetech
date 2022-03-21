from asyncio.windows_events import NULL
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import UserForm

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
    return render(request,"index.html")

def index2(request):
    return render(request,"index-2.html")

def index3(request):
    return render(request,"index-3.html")

def index4(request):
    return render(request,"index-4.html")
    
def team(request):
    return render(request,"team.html")

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
    # print("Services Page Called")
    return render(request,"services.html")
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
    data = {'form':fn}
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
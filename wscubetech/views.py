from django.http import HttpResponse
from django.shortcuts import render

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
    return render(request,"about.html")
def portfolio(request):
    return render(request,"portfolio.html")
def services(request):
    return render(request,"services.html")
def blog_details(request):
    return render(request,"blog_details.html")

def course(request):
    return HttpResponse("Hello this is course page")

# def courseDetail(request, course_id ):
#     return HttpResponse("This is course detail page " + str (course_id))

# def courseDetailWithStr(request, course_str ):
#     return HttpResponse("This is course detail page " + course_str)

def courseDetailWithAnyType(request, course_name ):
    return HttpResponse("This is course detail page " + course_name)
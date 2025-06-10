from django.http import HttpResponse
from django.shortcuts import render
import datetime


'''def home(request):
    print("test func is called from views")
    #return HttpResponse("<h1>Hello this is index page</h1>")
    return render(request, "home.html",{})'''


def home(request):
    isActive = True
    if request.method == 'POST':
        #check = request.POST['check']
        check = request.POST.get("check")
        print(check)
        if check is None: isActive = False
        else: isActive = True

    
    date = datetime.datetime.now()
    
    name = "Mohammad Ali"
    list_of_program = [
        'WAP to check even or odd',
        'WAP to check prime number',
        'WAP to print all prime number from 1 to 100',
        'WAP to print pascals triangle'
    ]
    student ={
        'student_name' :"Fatima Ali",
        'student_college':"ACN",
        'student_city':"Aligarh"
    }
    data={
        'date' :date,
        'isActive':isActive,
        'name':name,
        'list_of_program':list_of_program,
        'student_data':student
    }
    return render(request,"home.html", data)

def about(request):
    #return HttpResponse("<h1>Hello this is about page</h1>")
    return render(request, "about.html",{})

def services(request):
    #return HttpResponse("<h1>Hello this is services page</h1>")
    return render(request, "services.html",{})
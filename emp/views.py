from django.shortcuts import get_object_or_404,redirect
from django.shortcuts import render
from django.http import HttpResponse
from .models import Emp
from .models import Testimonial

# Create your views here.

def emp_home(request):
    emps = Emp.objects.all()
    return render (request, "emp/home.html", {'emps':emps})


def add_emp(request):
    if request.method == "POST":

       #data fetch from form
        emp_name = request.POST.get("emp_name")
        emp_id = request.POST.get("emp_id")
        emp_phone = request.POST.get("emp_phone")
        emp_address = request.POST.get("emp_address")
        #emp_working = request.POST.get("emp_working")
        emp_working = True if request.POST.get('emp_working') == 'on' else False
 
        emp_department = request.POST.get("emp_department")
        
        # create a model object and set the data
        e = Emp()
        e.name = emp_name
        e.emp_id = emp_id
        e.phone = emp_phone
        e.address = emp_address
        e.department = emp_department
        if e.working is not None:
            e.working = True
        else:
            e.working = False
        
        # save to the db
        e.save()

        print("it's working and data is coming")
        return redirect("/emp/home/")
    return render (request, "emp/add-emp.html", {})



def delete_emp(request, emp_id):
    #print(emp_id)
    emp = Emp.objects.get(pk= emp_id)
    emp.delete()
    return redirect("/emp/home/")

def update_emp(request, emp_id):
    emp = Emp.objects.get(pk = emp_id)
    return render(request, "emp/update_emp.html",{'emp':emp})


def do_update_emp(request, id):
    if request.method == 'POST':
        emp_name = request.POST.get("emp_name")
        emp_id_temp = request.POST.get("emp_id")
        emp_phone = request.POST.get("emp_phone")
        emp_address = request.POST.get("emp_address")
        emp_department = request.POST.get("emp_department")  
        emp_working = request.POST.get("emp_working")  # will be 'on' or None
        
        e = Emp.objects.get(pk=id)
        e.name = emp_name
        e.emp_id = emp_id_temp
        e.phone = emp_phone
        e.address = emp_address
        e.department = emp_department
        e.working = True if emp_working == 'on' else False  # ✅ Safe logic

        e.save()

    return redirect("/emp/home/")

def testimonials(request):
    testi=Testimonial.objects.all()

    return render(request, "emp/testimonials.html",{
        'testi':testi
    })
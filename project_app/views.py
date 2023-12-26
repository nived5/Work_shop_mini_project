from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from project_app.form import Login_Form, customer_Form, work_manager_Form


# Create your views here.
def homepage(request):
    return render(request,'page.html')

def dashboard(request):
    return render(request,'dash.html')

def Login12(request):
    return render(request,'login.html')

def customer_reg(request):
    form1 = Login_Form()
    form2 = customer_Form()
    if request.method == 'POST':
        form1 = Login_Form(request.POST)
        form2 = customer_Form(request.POST)

        if form1.is_valid() and form2.is_valid():
            user = form1.save(commit = False)
            user.is_customer = True
            user.save()
            user1 = form2.save(commit = False)
            user1.user = user
            user1.save()
            return redirect('test4')
    return render(request,'registration.html',{'form1':form1,'form2':form2})
#
#
# # Function for work manager
#
def work_manager_reg(request):
    form1 = Login_Form()
    form2 = work_manager_Form()
    if request.method == 'POST':
        form1 = Login_Form(request.POST)
        form2 = work_manager_Form(request.POST)

        if form1.is_valid() and form2.is_valid():
            user = form1.save(commit=False)
            user.is_workmanager = True
            user.save()
            user1 = form2.save(commit=False)
            user1.user = user
            user1.save()
            return redirect('log')
    return render(request, 'workmanager.html', {'form1': form1, 'form2': form2})


#fuction for comparing or checking is the entered user is customer,or work mananger.
def login_view(request):
    if request.method == 'POST':
         username = request.POST.get('uname')
         password = request.POST.get('pass')
         user = authenticate(request,username = username,password = password)
         print(user)
         if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('adm')
            elif user.is_workmanager:
                return redirect('custom')
            elif user.is_user:
                return redirect('manager')
         else:
            messages.info(request,'Invalid credentials')
    return render(request,'login.html')

# Function for admin page
def admin(request):
    return render(request,'admin_template/admin.html')

# function for customer
def custom(request):
    return render(request,'customer_template/customer.html')

# Function for manager
def manager(request):
    return render(request,'manager_template/manager.html')
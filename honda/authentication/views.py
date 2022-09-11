from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Two_wheeler,Four_wheeler,staff
from .forms import Booking_by_customer,staffregistration,AddTwoWheeler


# Create your views here.
def home(request):
    return render(request,'authentication/home.html')
def customerlogin(request):
     if request.method=="POST":
        username=request.POST['customername']
        password=request.POST['pass1']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            name=user.username
            return redirect('display')
        else:
            messages.error(request,"Bad credentials")
            return redirect('customerlogin')
     return render(request,"authentication/customer_login.html")
def customerlogout(request):
    logout(request)
    messages.success(request,"You are loggedout successfully")
    return redirect('home')
def customersignup(request):
     if request.method=="POST":
        customername=request.POST['customername']
        customerid=request.POST['customerid']
        aadharcardno=request.POST['aadharcardno']
        pancardno=request.POST['pancardno']
        phoneno=request.POST['phoneno']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        myuser=User.objects.create_user(customername,customerid,pass1)
        myuser.aadharcardno=aadharcardno
        myuser.pancardno=pancardno
        myuser.phoneno=phoneno
        myuser.pass2=pass2
        myuser.save()
        messages.success(request,"your account has been successfully created.")
        return redirect('customerlogin')

     return render(request,"authentication/customer_signup.html")
def adminsignup(request):
    return render(request,'authentication/admin_signup.html')
def admindisplay(request):
    return render(request,'authentication/admindisplay.html')
def adminlogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None and user.is_superuser:
            login(request,user)
            return redirect('admindisplay')

    return render(request,'authentication/admin_login.html')
def staffsignup(request):
    return render(request,'authentication/staff_signup.html')
def staffdetails(request):
    staffs=staff.objects.all()
    return render(request,'authentication/staffdetails.html',{'staffs':staffs})
def stafflogin(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        person=staff.objects.get(username=username)
        if person.password==password and person.username==username:
            return render(request,'authentication/staffdisplay.html',{'person':person.username})
        else:
            return redirect('stafflogin')

    return render(request,'authentication/staff_login.html')
def customerpage(request):
    return render(request,'authentication/customerpage.html')
def display(request):
    bike=Two_wheeler.objects.all()
    car=Four_wheeler.objects.all()
    name=request.user.username
    
    return render(request, 'authentication/display.html',{'bike':bike,'car':car,'name':name})
def staffdisplay(request):

    return render(request,"authentication/staffdisplay.html")

def staffregistrationform(request):
    if request.method == "POST":
        form=staffregistration(request.POST)
        if form.is_valid():
            user=form.save()
            return redirect('stafflogin')


    else:
         form=staffregistration()
         return render(request,'authentication/staffregistration.html',{'form':form})

def TwowheelerBookingbycustomer(request,pk):
    form=Booking_by_customer()
    context = {'form':form,'pk':pk}
    return render(request,'authentication/book.html',context)
def TwowheelerBookingbystaff(request,pk):
    form=Booking_by_customer()
    context = {'form':form,'pk':pk}
    return render(request,'authentication/staffbook.html',context)
def TwowheelerBookingbyadmin(request,pk):
    form=Booking_by_customer()
    context = {'form':form,'pk':pk}
    return render(request,'authentication/adminbook.html',context)
def FourwheelerBookingbystaff(request,pk):
    form=Booking_by_customer()
    context = {'form':form,'pk':pk}
    return render(request,'authentication/staffbookfourwheeler.html',context)


def FourwheelerBookingbycustomer(request,pk):
    form=Booking_by_customer()
    context = {'form':form,'pk':pk}
    return render(request,'authentication/bookfourwheeler.html',context)
def FourwheelerBookingbyadmin(request,pk):
    form=Booking_by_customer()
    context = {'form':form,'pk':pk}
    return render(request,'authentication/adminfourwheeler.html',context)
def TwowheelerVehiclestatus(request,pk):
    if request.method == 'POST':
        bike=Two_wheeler.objects.get(id=pk)
        bike.Available-=1
        bike.Booked+=1
        bike.save()
        messages.warning(request,"You have booked "+bike.title+" successfully")
        return redirect('twowheelerbook')
    
    return render(request,'display.html')
def staffTwowheelerVehiclestatus(request,pk):
    if request.method == 'POST':
        bikes=Two_wheeler.objects.all()
        bike=Two_wheeler.objects.get(id=pk)
        bike.Available-=1
        bike.Booked+=1
        bike.save()
        messages.warning(request,"You have booked "+bike.title+" successfully")
        return redirect('stafftwowheelerbook')
    
    return render(request,'display.html')
def adminTwowheelerVehiclestatus(request,pk):
    if request.method == 'POST':
        bikes=Two_wheeler.objects.all()
        bike=Two_wheeler.objects.get(id=pk)
        bike.Available-=1
        bike.Booked+=1
        bike.save()
        messages.warning(request,"You have booked "+bike.title+" successfully")
        return redirect('admintwowheelerbook')
    
    return render(request,'display.html')
def FourwheelerVehiclestatus(request,pk):
    if request.method == 'POST':
        car=Four_wheeler.objects.get(id=pk)
        car.Available-=1
        car.Booked+=1
        car.save()
        messages.warning(request,"You have booked "+car.title+" successfully")
        return redirect('fourwheelerbook')
    
    return render(request,'display.html')
def staffFourwheelerVehiclestatus(request,pk):
    if request.method == 'POST':
        car=Four_wheeler.objects.get(id=pk)
        car.Available-=1
        car.Booked+=1
        car.save()
        messages.warning(request,"You have booked "+car.title+" successfully")
        return redirect('stafffourwheelerbook')
    
    return render(request,'display.html')
def adminFourwheelerVehiclestatus(request,pk):
    if request.method == 'POST':
        car=Four_wheeler.objects.get(id=pk)
        car.Available-=1
        car.Booked+=1
        car.save()
        messages.warning(request,"You have booked "+car.title+" successfully")
        return redirect('adminfourwheelerbook')
    
    return render(request,'display.html')
def stafftwowheelerbook(request):
    bike=Two_wheeler.objects.all()
    return render(request,'authentication/stafftwowheelerbook.html',{'bike':bike})
def stafffourwheelerbook(request):
    car=Four_wheeler.objects.all()
    return render(request,'authentication/stafffourwheelerbook.html',{'car':car})
def admintwowheelerbook(request):
    bike=Two_wheeler.objects.all()
    return render(request,'authentication/admintwowheelerbook.html',{'bike':bike})
def adminfourwheelerbook(request):
    car=Four_wheeler.objects.all()
    return render(request,'authentication/adminfourwheelerbook.html',{'car':car})
def displaytable(request):
    bike=Two_wheeler.objects.all()
    car=Four_wheeler.objects.all()
    
    return render(request,'authentication/displaytable.html',{'bike':bike,'car':car})
def twowheelerbook(request):
    bike=Two_wheeler.objects.all()

    return render(request,'authentication/twowheelerbook.html',{'bike':bike})

def fourwheelerbook(request):
    car=Four_wheeler.objects.all()

    return render(request,'authentication/fourwheelerbook.html',{'car':car})
def addtwowheelerstock(request):
    if request.method == "POST":
        form=AddTwoWheeler(request.POST)
        if form.is_valid():
            user=form.save()
            return redirect('admintwowheelerbook')
    else:
        form=AddTwoWheeler()
        return render(request,'authentication/addtwowheelerstock.html',{'form':form})

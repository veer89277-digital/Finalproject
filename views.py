from django.shortcuts import render
from django.http import  HttpResponse
from .models import *

# Create your views here.
def index(request):
    cdata=lcategory.objects.all()
    d={"data":cdata}
    return render(request,"index.html",d)

def contact(request):
    d={}
    if request.method=="POST":
        a1=request.POST.get("name") #akhil
        a2=request.POST.get("email") #abc@gmail.com
        a3=request.POST.get("mob") #mobile
        a4=request.POST.get("msg") #message
        #d={"x1":a1,"x2":a2,"x3":a3,"x4":a4}
        contactus(name=a1,mobile=a3,email=a2,message=a4).save()
        return HttpResponse("<script>alert('data added succsessfully..');location.href='/contact/';</script>")
    return render(request,"contact.html",d) 

def gallery(request):
    data=igallery.objects.all()
    d={"gdata":data}
    return render(request,"gallery.html",d)

def wchoose(request):
    return render(request,"wchoose.html")

def team(request):
    mdata=mentor.objects.all()
    d={"data":mdata}

    return render(request,"team.html",d)

def video(request):
    cdata=lcategory.objects.all()
    md={"data":cdata}
    return render(request,"video.html",md)
def mycategory(request):
    x=lecture.objects.all()
    y=lcategory.objects.all()
    d={"data":x,"data1":y}
    
    return render(request,"category.html",d)
def aboutus(request):
    return render(request,"about.html")


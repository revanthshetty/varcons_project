from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import createuserform
from django.contrib import messages

def homepage(request):
   

    return render(request,'home_page.html')
def subscribe(request):
    return render(request,'subscribe.html')
def contactus(request):
    return render(request,'contactus.html')
def courses(request):
    return render(request,'classes_home.html')
def quiz(request):
    return render(request,'quiz_home.html')
def quizeng(request):
    return render(request,'quiz_eng.html')
def quizhin(request):
    return render(request,'quiz_hin.html')
def quizkan(request):
    return render(request,'quiz_kan.html')
def login1(request):
    context={}
    return render(request,'login.html',context)
def home(request):
    return render(request,'1.html')
def kannada(request):
    return render(request,'kannada.html')
def English(request):
    return render(request,'English.html')
def Hindi(request):
    return render(request,'Hindi.html')
def translate(request):
    return render(request,'translate.html')



def signup(request):
    form=createuserform()
    if request.method=='POST':
        form=createuserform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login1')
    context={'form':form}
    return render(request,'signup.html',context)



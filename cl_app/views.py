from django.shortcuts import render

# Create your views here.
def RegPage(request):
    return render(request,"cl_app/regpage.html")
def TempPage(request):
    return render(request,"cl_app/temp.html")
def FormPage(request):
    return render(request,"cl_app/form.html")
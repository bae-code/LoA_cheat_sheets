from django.shortcuts import render

# Create your views here.
def clearinfo(request):
    if request.method =="GET":
        return render(request,'clearinfo/clear.html')
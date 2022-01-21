from django.shortcuts import redirect, render

# Create your views here.
def main_view(request):
    return render(request, 'main.html')

def call_raid(request):
    if request.method =="GET":
        print('rara')
        return redirect('/')
    elif request.method == "POST":
        raid = request.POST.get('raid-name','')
        print(raid+'1')
        return render(request,'main.html',{'POST': raid })
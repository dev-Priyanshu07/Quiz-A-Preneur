from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
    return render (request, 'home.html')



def signup(request):
    if request.method =='POST':
            name = request.POST["name"]
            standard= request.POST["class"]
            school = request.POST["school"]
            # city_of_residence = request.POST['']

    else:
        return render(request, 'profile.html')       


    



from django.http import HttpResponse
from django.shortcuts import render
from app1.models import MyappRegistermodel
# Create your views here.


def home(request):
    return render(request, 'home.html')


def register(request):
    return render(request, 'register.html')


def about(request):
    return render(request, 'about.html')


def login(request):
    data = MyappRegistermodel.objects.all()
    if request.method == "POST":
        user = request.POST['username']
        passw = request.POST['password']
        print(user, passw)
        res = MyappRegistermodel.objects.all()
        for i in res:
            print(i)
            if i.username == user:
                if i.password == passw:
                    return render(request, 'db.html', {'res': res})
                else:
                    return HttpResponse('<h1> Incorrect Password </h1>')
            else:
                return HttpResponse('<h1> Incorrect user </h1>')
    return render(request, 'login.html', {'form': data})




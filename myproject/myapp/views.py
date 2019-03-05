from django.shortcuts import render
from .models import user
from .forms import addUser
# Create your views here.
def home(request):
	data=user.objects.all();
	return render(request,"myapp/home.html",{"data":data})

def login(request):
	form = addUser();
	return render(request,"myapp/login.html",{'form':form})

def index(request):
	name=request.GET.get("name")
	password=request.GET.get("password")

	data=user.objects.all();

	for d in data:
		if d.name==name:
			if d.password==password:
				return render(request,"myapp/index.html",{'uname':name})
		else:
			return render(request,"myapp/index.html",{'uname':'error'})

	
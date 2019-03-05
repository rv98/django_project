from django.shortcuts import render
from .models import user
# Create your views here.
def home(request):
	data=user.objects.all();
	return render(request,"myapp/home.html",{"data":data})
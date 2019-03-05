from django.forms import ModelForm
from .models import user

class addUser(ModelForm):
	class Meta:
		model=user
		fields=['name','password']
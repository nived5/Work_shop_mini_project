from django import forms
from django.contrib.auth.forms import UserCreationForm

from project_app.models import Login, customer, workmanager


# Customer login
class Login_Form(UserCreationForm):
    class Meta:
        model = Login
        fields =('username','password1','password2')





class customer_Form(forms.ModelForm):
    class Meta:
            model = customer
            fields = ('name','contact_no','email','address','vehicle_no')
#
# # form for workmanager
#
class work_manager_Form(forms.ModelForm):
    class Meta:
        model = workmanager
        fields = ('name','contact_no','email','address')
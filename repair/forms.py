from dataclasses import field
from shutil import ReadError
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Repair
from emp.models import EmpUser

class NewUserForm(UserCreationForm):
  #ทำให้ inputที่ใส่ต้องถูกต้องตามformatของ email
    #email = forms.EmailField(required=True)
    
  #เลือกว่าต้องการให้กรอกอะไรบ้าง
    
    class Meta:
        model = User
        #เพิ่มได้ตามที่user modelตั้งต้นของ djangoมีให้
        fields = ("username","first_name", "last_name","password1", "password2")

    
       
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        #user.email = self.cleaned_data["email"]
        
        if commit:
            user.save() 
        return user



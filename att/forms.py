# from rest_framework import serializers
from django import forms
# from form_utils.fields import ClearableFileField
from .models import user,attendance,geolog

class userForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ['id','name','father_name','cnic','designation','district','mobile','imei','joining_date','date']
class attendanceForm(forms.ModelForm):
    class Meta:
        model = attendance
        fields = ['id','user_id','cnic','imei','date','lat','long','type','date1']
class geologForm(forms.ModelForm):
    class Meta:
        model = geolog
        fields = ['id','user_id','cnic','imei','lat','long','date','date1']
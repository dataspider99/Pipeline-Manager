from django import forms
from .models import AcquireData
from django.shortcuts import get_object_or_404

class JobRunForm(forms.Form):
    
    id = forms.IntegerField()
    username = forms.CharField(label='User Name', max_length=10)
    password = forms.CharField(widget=forms.PasswordInput())
    
    def runjob(self):
        job = get_object_or_404(AcquireData,pk=self.cleaned_data.get("id"))
        print(job)
    
    
from django import forms
from .models import DataJob
from django.shortcuts import get_object_or_404

class JobRunForm(forms.Form):
    
    id = forms.IntegerField()
    
    def runjob(self):
        job = get_object_or_404(DataJob,pk=self.cleaned_data.get("id"))
        print(job)
    
class PipelineForm(forms.Form):
    
    id = forms.IntegerField()
    
    def runpipeline(self):
        pass
from django.contrib import admin
from .models import DataStore,CodeRunner,LoginMeta,AcquireData
from django import forms
import json, socket

admin.site.register(CodeRunner)
admin.site.register(LoginMeta)
admin.site.register(AcquireData)

class DataStoreForm(forms.ModelForm):
    class Meta:
        model = DataStore
        fields = "__all__"
        
    def clean(self):
        try:
            json.loads(self.cleaned_data.get('json_info'))
        except ValueError:
            raise forms.ValidationError("json info: Not a valid json")
        self.isopen()
        return self.cleaned_data
    
    def isopen(self):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                s.connect((self.cleaned_data.get('host'),self.cleaned_data.get('port')))
                s.shutdown(2)
                return True
            except:        
                raise forms.ValidationError("Can not reach to DataStore host:{} and port:{}".format(self.cleaned_data.get('host'),self.cleaned_data.get('port')))

@admin.register(DataStore)
class DataStoreAdmin(admin.ModelAdmin):
    list_display  = ('name','json_info')
    form = DataStoreForm

class CodeRunnerAdmin(admin.ModelAdmin):
    list_display = ('name','api_url')
    
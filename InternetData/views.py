from .models import AcquireData
from django.views.generic import ListView
from django.views.generic import DetailView
from .forms import JobRunForm
from django.views.generic.edit import FormView
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
import jenkins
class DataJobList(ListView):
    model = AcquireData
    template_name="acquirelist.html"
    
class JobDetail(DetailView):

    model = AcquireData
    template_name="acquiredetail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
def runjob(request,id):
    job = get_object_or_404(AcquireData,id=id)
    server = jenkins.Jenkins('http://localhost:8080', username='myuser', password='mypassword')
    user = server.get_whoami()
    version = server.get_version()
    print('Hello %s from Jenkins %s' % (user['fullName'], version))
    return JsonResponse({'some': 'data'})

    
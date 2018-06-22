from .models import DataJob,Project
from django.views.generic import ListView,CreateView,DetailView
from django.views.generic.edit import FormView
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
import jenkins
from jenkins import NotFoundException
from .forms import PipelineForm

class ProjectList(ListView):
    model = Project
    template_name = "list.html"

class ProjectDetail(DetailView):
    model = Project
    template_name = "projectdetail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class DataJobList(ListView):
    model = DataJob
    template_name="acquirelist.html"
    
class JobDetail(DetailView):

    model = DataJob
    template_name="acquiredetail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
def runjob(request,id):
    job = get_object_or_404(DataJob,id=id)
    server = jenkins.Jenkins(job.scraper.api_url, 
                             username=job.scraper.login.token_key, 
                             password=job.scraper.login.token_secret)
    parameters = {
        "TOKEN":job.loginmeta.token_key,
        "TOKEN_SECRET": job.loginmeta.token_secret,
        "APP": job.loginmeta.consumer_key,
        "APP_SECRET": job.loginmeta.consumer_secret,
        "KEYWORDS": job.keywords.replace("\n",","),
        "HOST":  job.data_pool.host,         
        "PORT": job.data_pool.port,
        "DATASTORE": job.data_pool.name,
        "JSON_INFO" : job.data_pool.json_info,   
        "USERNAME" : job.data_pool.username,
        "PASSWORD" : job.data_pool.password,
        }
    try:
        queueid = server.build_job(job.scraper.jobname,parameters=parameters)
        return redirect("{}/job/{}".format(job.scraper.api_url,job.scraper.jobname))
    except NotFoundException:
        return JsonResponse({"error":job.scraper.jobname})

class PipelineView(FormView):
    template_name = 'pipeline.html'
    form_class = PipelineForm

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)

    
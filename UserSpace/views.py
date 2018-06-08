from UserSpace.forms import LoginForm
from django.views.generic.edit import FormView
from django.shortcuts import render
from django.contrib.auth import login

class LoginView(FormView):
    form_class = LoginForm
    success_url = "/"
    template_name = "login.html"    
    
    def form_valid(self,form):
        login(self.request, form.get_user())
        return super(LoginView,self).form_valid(form)
    
    
    
def index(request):
    return render(request, 'index.html')



    
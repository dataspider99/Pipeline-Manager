from django.urls import path
from InternetData import views
urlpatterns = [
    path('jobs/',views.DataJobList.as_view()),
    path('jobs/<int:id>/',views.JobDetail.as_view()),
    path('run/<int:id>',views.runjob)
    ]
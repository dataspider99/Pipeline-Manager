from django.urls import path
from InternetData import views
urlpatterns = [
    path('projects/',views.ProjectList.as_view(),name="projects"),
    path('projects/<int:pk>',views.ProjectDetail.as_view(),name="project"),
    path('jobs/',views.DataJobList.as_view()),
    path('jobs/<int:pk>/',views.JobDetail.as_view()),
    path('run/<int:id>',views.runjob,name="run"),
    path('pipeline',views.PipelineView.as_view())
    ]
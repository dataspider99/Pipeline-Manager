from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from Taxonomy import views

urlpatterns = [
    url(r'^keyword/(?P<pk>[0-9]+)/$', views.DetailKeyword.as_view()),
    url(r'^keyword/$', views.ListKeywords.as_view()),
    url(r'^taxonomy/(?P<pk>[0-9]+)/$', views.DetailTaxonomy.as_view()),
    url(r'^taxonomy/$', views.ListTaxonomy.as_view()),
    ]
urlpatterns = format_suffix_patterns(urlpatterns)
from django.urls import path, re_path
from simplemooc.courses import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^(?P<pk>\d+)/$', views.details, name='details'),
]

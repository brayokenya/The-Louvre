from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.art_of_day,name='artToday'),
    url(r'^search/', views.search_results, name='search_results'), 

]
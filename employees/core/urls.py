from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.employees_list),
    url(r'^$', views.employees_details),
]

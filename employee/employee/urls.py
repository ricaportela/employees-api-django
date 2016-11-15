from django.conf.urls import url
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework.urlpatterns import format_suffix_patterns
from employeeapp import views


urlpatterns = (
    url(r'^admin/', admin.site.urls),
    url(r'^employee/$', views.EmployeeList.as_view(), name='employee_list'),
    url(r'^employee/(?P<pk>[0-9]+)/$', views.EmployeeDetails.as_view()),
    url(r'^$', RedirectView.as_view(url='/employee/'), name='redirect_to_employee'),
)

urlpatterns = format_suffix_patterns(urlpatterns)

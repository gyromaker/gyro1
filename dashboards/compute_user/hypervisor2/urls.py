from django.conf.urls import url
from openstack_dashboard.dashboards.compute_user.hypervisor2 import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
]
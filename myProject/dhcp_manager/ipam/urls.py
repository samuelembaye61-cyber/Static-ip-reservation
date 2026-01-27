
from django.urls import path
from .views import dhcp_list

urlpatterns = [
    path('', dhcp_list, name='dhcp_list'),
]
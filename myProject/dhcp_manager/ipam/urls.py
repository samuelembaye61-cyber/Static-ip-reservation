
from django.urls import path
from .views import dhcp_list, reserve_ip

urlpatterns = [
    path('', dhcp_list, name='dhcp_list'),
    path("reserve/<int:ip_address_id>/", reserve_ip, name="reserve_ip"),

]
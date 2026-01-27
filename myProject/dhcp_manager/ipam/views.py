
from django.shortcuts import render

# .models file
from .models import IPAddress 

# Create your views here.

def dhcp_list(request):
    dhcp_addresses = IPAddress.objects.filter(status='dhcp')
    available_static = IPAddress.objects.filter(status='available')
    reserved_static = IPAddress.objects.filter(status='reserved')
    return render(request, 'ipam/dhcp_list.html', {
        'dhcp_addresses': dhcp_addresses,
        'available_static': available_static,
        'reserved_static': reserved_static,
    })

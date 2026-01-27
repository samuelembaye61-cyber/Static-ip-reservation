
from django.shortcuts import render

# .models file
from .models import IPAddress 

# Create your views here.

def dhcp_list(request):
    dhcp_addresses = IPAddress.objects.filter(status='dhcp')
    return render(request, 'ipam/dhcp_list.html', {
        'dhcp_addresses': dhcp_addresses
    })

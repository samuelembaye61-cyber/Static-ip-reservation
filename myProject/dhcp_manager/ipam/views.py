
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

        # Summary carts

        "dhcp_count": dhcp_addresses.count(),
        "available_count": available_static.count(),
        "reserved_count": reserved_static.count(),
    })


from django.shortcuts import redirect, get_object_or_404


def reserve_ip(request, ip_address_id):
    ip_address = get_object_or_404(IPAddress, id=ip_address_id)

    if request.method == "POST" and ip_address.status == "available":
        ip_address.status = "reserved"
        ip_address.save()

    return redirect("dhcp_list")


def release_ip(request, ip_address_id):
    ip_address = get_object_or_404(IPAddress, id=ip_address_id)

    if request.method == "POST" and ip_address.status == "reserved":
        ip_address.status = "available"
        ip_address.save()

    return redirect("dhcp_list")
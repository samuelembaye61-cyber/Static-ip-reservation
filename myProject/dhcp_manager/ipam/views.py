
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
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


def reserve_ip(request, ip_address_id):
    ip_address = get_object_or_404(IPAddress, id=ip_address_id)

    if request.method == "POST" and ip_address.status == "available":
        ip_address.status = "reserved"
        ip_address.save()

        next_section = request.POST.get("next_section", "")
        response = redirect("dhcp_list")
        if next_section:
            response["Location"] += f"#{next_section}"
        return response


def release_ip(request, ip_address_id):
    ip_address = get_object_or_404(IPAddress, id=ip_address_id)

    if request.method == "POST" and ip_address.status == "reserved":
        ip_address.status = "available"
        ip_address.save()

        next_section = request.POST.get("next_section", "")
        response = redirect("dhcp_list")
        if next_section:
            response["Location"] += f"#{next_section}"
        return response




def signup(request):

    # show page if GET request
    if request.method == "GET":
        return render(request, "ipam/signup.html")

    # POST request (form submitted)
    username = (request.POST.get("username") or "").strip()
    password = request.POST.get("password") or ""

    # validation
    if not username or not password:
        messages.error(request, "Username and password are required.")
        return redirect("signup")

    if User.objects.filter(username=username).exists():
        messages.error(request, "Username already exists.")
        return redirect("signup")

    # create user
    User.objects.create_user(username=username, password=password)
    messages.success(request, "User created successfully.")

    # redirect after success
    return redirect("dhcp_list")
    

    
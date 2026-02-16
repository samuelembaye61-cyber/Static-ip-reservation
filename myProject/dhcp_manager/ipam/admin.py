from django.contrib import admin

# import models from IPAddress
from .models import IPAddress

from django.contrib import admin
# Login page and admin page title
admin.site.site_header = "IP Management Admin"
admin.site.site_title = "IP Admin Login"

# Register your models here.

@admin.register(IPAddress)
class IPAddressAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'hostname', 'status', 'updated_at')
    list_filter = ('status',)
    search_fields = ('ip_address', 'hostname')
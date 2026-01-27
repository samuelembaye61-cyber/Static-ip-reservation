from django.db import models

# Create your models here.

class IPAddress(models.Model):
    ip_address = models.GenericIPAddressField(unique=True)
    hostname = models.CharField(max_length=100, blank=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('dhcp', 'DHCP'),
            ('static', 'Static'),
        ],
        default='dhcp'
    )
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "DHCP Address"
        verbose_name_plural = "DHCP Addresses"

def __str__(self):
    return self.ip_address
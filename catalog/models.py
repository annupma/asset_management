from pickle import FROZENSET

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse

from .manufacturers import trusted_manufacturers

# Create your models here.


class Device(models.Model):
    """
    Model representing a devices (details).
    """
    serialn = models.CharField(max_length=100, null=False,  verbose_name="S/N", blank=True, help_text="Device's Serial Number")
    # datacenter = models.CharField(max_length=50, null=False,  verbose_name="DataCenter", default='sec-62 Noida', blank=False, help_text="Data Center")
    location = models.CharField(max_length=50, null=False,  verbose_name="Location", default='default rack', blank=False, help_text="Device Location")
    # location = models.ForeignKey('Location', null=False, help_text="Device Location", on_delete=models.PROTECT)
    datacenter_location = models.ForeignKey('Location', null=False, help_text="DataCenter Location", on_delete=models.PROTECT, default=1)
    # oem = models.ForeignKey('Manufacturer', null=False, verbose_name="OEM", help_text="Device Manufacturer", on_delete=models.PROTECT)
    oem = models.CharField(max_length=20, choices=trusted_manufacturers, blank=True, default='0',
                              help_text='Manufacturer', verbose_name="OEM")
    model = models.ForeignKey('Model', null=False, help_text="Device Model", on_delete=models.PROTECT)
    asset_type = models.ForeignKey('AssetType', null=False, help_text="Device Asset Type", on_delete=models.PROTECT)
    hostname = models.CharField(max_length=100, null=True, blank=False, verbose_name="Hostname")
    rack = models.CharField(max_length=50, null=True, blank=False, verbose_name="Rack")
    # lob = models.CharField(max_length=50, null=True, blank=False, verbose_name="LOB")
    lob = models.ForeignKey('LOB', on_delete=models.SET_NULL, null=True)
    ip = models.CharField(max_length=20, null=True, blank=False, verbose_name="IP Address")
    mgmt_ilo_ip = models.CharField(max_length=20, null=True, blank=False, verbose_name="Management ILO IP")
    assigned_spoc = models.ForeignKey('Customer', null=True, on_delete=models.SET_NULL)
    assigned_to = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True)
    managed_by = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True)
    
    # Purchase related information
    po_number = models.CharField(max_length=50, null=True, blank=False, verbose_name="Purchase Number")
    po_date = models.DateField(null=True, blank=True, verbose_name="Purchase date")
    invoice_number = models.CharField(max_length=50, null=True, blank=False, verbose_name="Invoice Number")
    invoice_date = models.DateField(null=True, blank=True, verbose_name="Invoice date")
    mih_number = models.CharField(max_length=50, null=True, blank=False, verbose_name="MIH Number", help_text="Manfucturer Identification Number")
    project_name =  models.TextField(max_length=1000, null=True, blank=True, help_text="MIH Project Number")
    warranty_start_date = models.DateField(null=True, blank=False, verbose_name="Warranty Start Date")
    warranty_expiration_date = models.DateField(null=True, blank=True, verbose_name="Warranty End Date")
    amc_expiration_date = models.DateField(null=True, blank=True, verbose_name="AMC Expiration Date")
    tracking_number = models.CharField(max_length=50, null=True, blank=False, verbose_name="IR/MO  Number")
    
    # Statuses
    HW_STATUS = (
        ('0', 'Received'),
        ('1', 'Deployed'),
        ('2', 'Inactive'),
        ('3', 'In Stock'),
        ('4', 'Decommission'),
        ('5', 'Disposed'),
    )
    status = models.CharField(max_length=1, choices=HW_STATUS, blank=True, default='0',
                                 help_text='Asset Status', verbose_name="Asset Status")
    HW_SUBSTATUS = (
        ('0', 'Completed Shipment'),
        ('1', 'Functional'),
        ('2', 'Not In use'),
        ('3', 'In Inventory'),
        ('4', 'Decommissioned'),
        ('5', 'Disposed'),
    )

    substatus = models.CharField(max_length=1, choices=HW_SUBSTATUS, blank=True, default='0',
                                 help_text='Asset Sub Status', verbose_name="Asset Sub Status")
    eos = models.CharField(max_length=20, null=True, blank=False, verbose_name="EOS", help_text="End of Service")
    eol = models.CharField(max_length=20, null=True, blank=False, verbose_name="EOL", help_text="End of Life")
    support_status = models.CharField(max_length=20, null=True, blank=False, verbose_name="Support Status", help_text="Under warranty or AMC")

    # Audit fields
    # created = models.DateTimeField(auto_now_add=True, editable=True)
    # modified = models.DateTimeField(auto_now=True)
    notes = models.TextField(max_length=1000, null=True, blank=True, verbose_name="Remarks or Ticket Number", help_text="Enter a job description of the Device")

    def __str__(self):
        """
        String for representing the Model object.
        """
        if self.hostname:
            return self.hostname
        else:
            return self.serialn

    def display_customer(self):
        """
        Creates a string for the Customer. This is required to display model in Admin.
        """
        return ', '.join([model.name for model in self.model.all()[:3]])

    display_customer.short_description = 'Customer'

    def display_model(self):
        """
        Creates a string for the Model. This is required to display model in Admin.
        """
        return ', '.join([model.name for model in self.model.all()[:3]])

    display_model.short_description = 'Model'

    def status_verbose(self):
        return dict(Device.LOAN_STATUS)[self.status]

    def substatus_verbose(self):
        return dict(Device.LOAN_SUBSTATUS)[self.substatus]


    def get_absolute_url(self):
        """
        Returns the url to access a particular device.
        """
        return reverse('catalog:device-detail', args=[str(self.id)])

    # class Meta:
    #     ordering = ['-modified']
  

class AssetType(models.Model):
    """
    Model representing a devices type
    """

    assettype = models.CharField(max_length=200, help_text="Laptop / desktop etc")

    def __str__(self):

        return self.assettype


class Model(models.Model):
    """
    Model representing a devices model
    """
    name = models.CharField(max_length=200, help_text="Enter a hw Model")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name
    
class Customer(models.Model):
    """
    Model representing a Customer.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True)
    location = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True)


    def get_absolute_url(self):
        """
        Returns the url to access a particular Customer.
        """
        return reverse('catalog:customer_detail', args=[str(self.id)])


    def __str__(self):
        """
        String for representing the Customer object.
        """
        return '%s, %s' % (self.last_name, self.first_name)

    class Meta:
        ordering = ['last_name']


class Location(models.Model):
    """
      Model representing set location/site for customer or device
    """

    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        """
        String for representing the Location object (in Admin site etc.)
        """
        return self.name

class Department(models.Model): 
    """
        Model representing set department for customer or Tracker
        # todo : Add : ESXI, Linux etc
    """
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        """
        String for representing the Department object (in Admin site etc.)
        """
        return self.name
    

class LOB(models.Model): 
    """
        Model representing set LOB for customer or Tracker
        # todo : Add : Telemedia, CloudOps etc
    """
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        """
        String for representing the LOB object (in Admin site etc.)
        """
        return self.name
    

# class Manufacturer(models.Model):
#     """
#         Model representing the manufacturers
#     """
#     name = models.CharField(max_length=50, blank=False, null=False)
#     description = models.CharField(max_length=50, blank=True, null=True)
#
#     class Meta:
#         ordering = ['id']
#
#     def __str__(self):
#         """
#         String for representing the Manufacturer object (in Admin site etc.)
#         """
#         return self.name
#
class Company(models.Model):
    """
        Model representing the Company. Eg Airtel, Accenture
    """
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        """
        String for representing the Company object (in Admin site etc.)
        """
        return self.name
    

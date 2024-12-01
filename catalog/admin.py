from datetime import date
from django.contrib import admin
from import_export import resources
from .resources import DevicelistResource
from import_export.admin import ImportExportModelAdmin
# from .models import Customer, Model, Device, AssetType, Tracker, Inventory, Location, Department
from .models import Customer, Model, Device, AssetType, Location, Department, Company, LOB

# Register your models here.

admin.site.register(Model)
admin.site.register(AssetType)

# Define the admin class
class Devicelist(resources.ModelResource):
    class Meta:
        model = Device

# class Assettag(resources.ModelResource):
#     class Meta:
#         model = Inventory


#@admin.register(Tracker)
# class TrackerAdmin(admin.ModelAdmin):
#     list_display = ('name', 'notes', 'customer', 'cus2', 'equip', 'credate', 'deptout', 'deptin')
#     fields = [('name', 'notes'), ('deptout', 'deptin'),  ('equip', 'equip1'), 'credate', ('customer', 'cus2')]
#     search_fields = ['name', 'credate']
#     class Meta:
#         model = Tracker

# admin.site.register(Tracker, TrackerAdmin)

#@admin.register(Customer)
class CustomerAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'department', 'location')
    fields = ['first_name', 'last_name', 'department', 'location']
    search_fields = ['first_name', 'last_name', 'department']


admin.site.register(Customer, CustomerAdmin)

#@admin.register(Device)

class DeviceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("serialn", "datacenter_location", "location", "oem", "model", "asset_type", "hostname", "rack", "lob", "ip", "mgmt_ilo_ip", "assigned_spoc", "assigned_to", "managed_by", "po_number", "po_date", "invoice_number", "invoice_date", "mih_number", "project_name", "warranty_start_date", "warranty_expiration_date", "amc_expiration_date", "tracking_number", "status", "substatus", "eos", "eol", "support_status",  "notes")
    # list_display = ('hostname', 'model', 'customer', 'serialn', 'assettype', 'tag', 'buydate', 'warranty', 'status', 'substatus', 'modified')
    # fields = ['hostname', ('model',  'serialn'), ('assettype', 'buydate',), ('customer', 'location'), ('tag', 'warranty'), ('status', 'substatus'), 'cost', 'notes']

    fields = ["serialn", "datacenter_location", "location", "oem", "model", "asset_type", "hostname", "rack", "lob", "ip", "mgmt_ilo_ip", "assigned_spoc", "assigned_to", "managed_by", "po_number", "po_date", "invoice_number", "invoice_date", "mih_number", "project_name", "warranty_start_date", "warranty_expiration_date", "amc_expiration_date", "tracking_number", "status", "substatus", "eos", "eol", "support_status", "notes"]

    search_fields = ['hostname', 'model__name', 'customer__last_name', 'serialn', 'assettype__assettype', 'substatus']

    resource_class = DevicelistResource


admin.site.register(Device, DeviceAdmin)

# class ArchiveAdmin(ImportExportModelAdmin, admin.ModelAdmin):
#     list_display = ('hostname', 'model', 'customer', 'serialn', 'type', 'tag', 'buydate', 'warranty', 'status', 'substatus', 'modified')
#     fields = ['hostname', ('model',  'serialn'), ('type', 'buydate',), ('customer', 'location'), ('tag', 'warranty'), ('status', 'substatus'), 'cost', 'notes']
#     search_fields = ['hostname', 'model__name', 'customer__last_name', 'serialn', 'tag', 'type__type', 'substatus']
#     resource_class = DevicelistResource


# admin.site.register(Archive, ArchiveAdmin)

# class InventoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
#     list_display = ('num', 'snum')
#     resource_class = AssettagResource

# admin.site.register(Inventory, InventoryAdmin)

class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.register(Location, LocationAdmin)

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.register(Department, DepartmentAdmin)

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.register(Company, CompanyAdmin)


class LOBAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.register(LOB, LOBAdmin)
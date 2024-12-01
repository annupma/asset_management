from import_export import resources
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget, DateWidget

from .models import Device, Customer, Location, Model, AssetType, Department, Company, LOB


class DevicelistResource(resources.ModelResource):
    """
    Import Device based on the updated model structure.
    """

    # Device information
    serialn = Field(attribute='serialn', column_name='Serial Number')
    location = Field(attribute='location', column_name='Location')
    datacenter_location = Field(attribute='datacenter_location', column_name='Data Center Location', widget=ForeignKeyWidget(Location, 'name'))
    # oem = Field(attribute='oem', column_name='OEM', widget=ForeignKeyWidget(Manufacturer, 'name'))
    oem = Field(attribute='oem', column_name='OEM')
    model = Field(attribute='model', column_name='Model', widget=ForeignKeyWidget(Model, 'name'))
    asset_type = Field(attribute='asset_type', column_name='Asset Type', widget=ForeignKeyWidget(AssetType, 'assettype'))
    hostname = Field(attribute='hostname', column_name='Host Name')
    rack = Field(attribute='rack', column_name='Rack')
    lob = Field(attribute='lob', column_name='LOB',
                widget=ForeignKeyWidget(LOB, 'name'))
    ip = Field(attribute='ip', column_name='IP Address')
    mgmt_ilo_ip = Field(attribute='mgmt_ilo_ip', column_name='Management ILO IP')
    assigned_spoc = Field(attribute='assigned_spoc', column_name='Assigned Customer',
                      widget=ForeignKeyWidget(Customer, 'first_name'))
    assigned_to = Field(attribute='assigned_to', column_name='Assigned Department',
                        widget=ForeignKeyWidget(Department, 'name'))
    managed_by = Field(attribute='managed_by', column_name='Managed By', widget=ForeignKeyWidget(Company, 'name'))

    # Purchase information
    po_number = Field(attribute='po_number', column_name='Purchase Order Number')
    po_date = Field(attribute='po_date', column_name='Purchase Date', widget=DateWidget('%m/%d/%y'))
    invoice_number = Field(attribute='invoice_number', column_name='Invoice Number')
    invoice_date = Field(attribute='invoice_date', column_name='Invoice Date', widget=DateWidget('%m/%d/%y'))
    mih_number = Field(attribute='mih_number', column_name='MIH Number')
    project_name = Field(attribute='project_name', column_name='Project Name')
    warranty_start_date = Field(attribute='warranty_start_date', column_name='Warranty Start Date',
                                widget=DateWidget('%m/%d/%y'))
    warranty_expiration_date = Field(attribute='warranty_expiration_date', column_name='Warranty Expiration Date',
                                     widget=DateWidget('%m/%d/%y'))
    amc_expiration_date = Field(attribute='amc_expiration_date', column_name='AMC Expiration Date',
                                widget=DateWidget('%m/%d/%y'))
    tracking_number = Field(attribute='tracking_number', column_name='Tracking Number')

    # Statuses
    status = Field(attribute='status', column_name='Hardware Status')
    substatus = Field(attribute='substatus', column_name='Sub Status')
    eos = Field(attribute='eos', column_name='End of Service')
    eol = Field(attribute='eol', column_name='End of Life')
    support_status = Field(attribute='support_status', column_name='Support Status')

    # Audit fields
    created = Field(attribute='created', column_name='Created', widget=DateWidget('%d/%m/%y %H:%M:%S'))
    modified = Field(attribute='modified', column_name='Modified', widget=DateWidget('%d/%m/%y %H:%M:%S'))
    notes = Field(attribute='notes', column_name='Notes')

    class Meta:
        model = Device
        # fields = '__all__'
        # exclude = ("created", "modified")

        # list_display = ("serialn", "datacenter", "location", "oem", "model", "asset_type", "hostname", "rack", "lob", "ip", "mgmt_ilo_ip", "assigned_spoc", "assigned_to", "managed_by", "po_number", "po_date", "invoice_number", "invoice_date", "mih_number", "project_name", "warranty_start_date", "warranty_expiration_date", "amc_expiration_date", "tracking_number", "status", "substatus", "eos", "eol", "support_status", "created","modified", "notes")
        # # list_display = ('hostname', 'model', 'customer', 'serialn', 'assettype', 'tag', 'buydate', 'warranty', 'status', 'substatus', 'modified')
        # fields = ['hostname', ('model',  'serialn'), ('assettype', 'buydate',), ('customer', 'location'), ('tag', 'warranty'), ('status', 'substatus'), 'cost', 'notes']
        # search_fields = ['hostname', 'model__name', 'customer__last_name', 'serialn', 'assettype__assettype', 'substatus']
        fields = (
            "serialn", "datacenter_location", "location", "oem", "model", "asset_type", "hostname", "rack", "lob", "ip",
            "mgmt_ilo_ip", "assigned_spoc", "assigned_to", "managed_by", "po_number", "po_date", "invoice_number",
            "invoice_date", "mih_number", "project_name", "warranty_start_date", "warranty_expiration_date",
            "amc_expiration_date", "tracking_number", "status", "substatus", "eos", "eol", "support_status", "notes"
        )
        exclude = ("created","modified")

        import_id_fields = (
            "serialn", "datacenter_location", "location", "oem", "model", "asset_type", "hostname", "rack", "lob", "ip",
            "mgmt_ilo_ip", "assigned_spoc", "assigned_to", "managed_by", "po_number", "po_date", "invoice_number",
            "invoice_date", "mih_number", "project_name", "warranty_start_date", "warranty_expiration_date",
            "amc_expiration_date", "tracking_number", "status", "substatus", "eos", "eol", "support_status", "notes"
        )

        # fields = ('hostname', 'customer', 'model', 'serialn', 'tag', 'assettype', 'location', 'buydate', 'status', 'substatus', 'warranty', 'cost')
        # exclude = ('id', )
        # import_id_fields = ('hostname', 'customer', 'model', 'serialn', 'tag', 'assettype', 'location', 'buydate', 'status', 'substatus', 'warranty', 'cost')

    def dehydrate_customer(self, device):
        return '%s' % (device.serialn)

# class AssettagResource(resources.ModelResource):
#     """
#        Import Asset tag and Serial Number
#     """

#     num = Field(attribute='num', column_name='AssetTag')
#     snum = Field(attribute='snum', column_name='SN')

#     class Meta:
#         model = Inventory
#         exclude = ('id', )
#         import_id_fields = ('num', 'snum', )

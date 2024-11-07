from django.urls import path, re_path
from . import views
from .views import SearchResultsView, InventoryListView, DeviceListView, DeviceDetailView, CustomerListView, CustomerDetailView, TrackerListView, TrackerDetailView, BulkImportDevices

app_name = 'catalog'


urlpatterns = [
    path('index/', views.index, name='index1'),
    path('search/', SearchResultsView.as_view(), name='search_result'),
    path('inventory/', InventoryListView.as_view(), name='inventory'),
    path('bulk_import_devices/', BulkImportDevices.as_view(), name='bulk_import_devices'),
    path('devices/', DeviceListView.as_view(), name='devices'),
    path('device/<int:pk>/', DeviceDetailView.as_view(), name='device-detail'),
    path('customers/', CustomerListView.as_view(), name='customers'),
    path('customer/<int:pk>/', CustomerDetailView.as_view(), name='customer_detail'),
    path('trackers/', TrackerListView.as_view(), name='trackers'),
    path('tracker/<int:pk>/', TrackerDetailView.as_view(), name='tracker_detail'),
    
]

from django.urls import path
from .views import PropertyListView, PropertyDetailView

app_name = 'properties'

urlpatterns = [
    path('', PropertyListView.as_view(), name='property_list'),
    path('properties/<uuid:id>/', PropertyDetailView.as_view(), name='property_detail'),
]
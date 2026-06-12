from django.views.generic import ListView, DetailView
from .models import Property


class PropertyListView(ListView):
    model = Property
    template_name = 'properties/property_list.html'
    context_object_name = 'properties'
    paginate_by = 12

    def get_queryset(self):
        return Property.objects.filter(is_available=True)


class PropertyDetailView(DetailView):
    model = Property
    template_name = 'properties/property_detail.html'
    context_object_name = 'property'
    pk_url_kwarg = 'id'

    def get_queryset(self):
        return Property.objects.filter(is_available=True)
from django.views.generic import ListView, DetailView
from .models import Property


class PropertyListView(ListView):
    model = Property
    template_name = 'properties/property_list.html'
    context_object_name = 'properties'
    paginate_by = 12

    def get_queryset(self):
        qs = Property.objects.filter(
            status__in=[Property.Status.ON_RENT, Property.Status.ON_SALE]
        )
        status_filter = self.request.GET.get('status')
        if status_filter in [Property.Status.ON_RENT, Property.Status.ON_SALE]:
            qs = qs.filter(status=status_filter)

        bedrooms = self.request.GET.get('bedrooms')
        if bedrooms and bedrooms.isdigit():
            qs = qs.filter(bedrooms__gte=bedrooms)

        bathrooms = self.request.GET.get('bathrooms')
        if bathrooms and bathrooms.isdigit():
            qs = qs.filter(bathrooms__gte=bathrooms)

        price_min = self.request.GET.get('price_min')
        if price_min and price_min.replace('.', '', 1).isdigit():
            qs = qs.filter(price__gte=price_min)

        price_max = self.request.GET.get('price_max')
        if price_max and price_max.replace('.', '', 1).isdigit():
            qs = qs.filter(price__lte=price_max)

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_status'] = self.request.GET.get('status', '')
        context['filter_bedrooms'] = self.request.GET.get('bedrooms', '')
        context['filter_bathrooms'] = self.request.GET.get('bathrooms', '')
        context['filter_price_min'] = self.request.GET.get('price_min', '')
        context['filter_price_max'] = self.request.GET.get('price_max', '')

        query = self.request.GET.copy()
        if 'page' in query:
            del query['page']
        context['query_params'] = query.urlencode()
        return context


class PropertyDetailView(DetailView):
    model = Property
    template_name = 'properties/property_detail.html'
    context_object_name = 'property'
    pk_url_kwarg = 'id'

    def get_queryset(self):
        return Property.objects.filter(
            status__in=[Property.Status.ON_RENT, Property.Status.ON_SALE]
        )
from django.urls import reverse
from properties.models import Property


class TestPropertyListView:
    def test_list_returns_available_properties(self, client, property_instance):
        Property.objects.create(
            title='Unavailable Property',
            description='Not available',
            price=2000.00,
            location='Suburbs',
            bedrooms=3,
            bathrooms=2,
            is_available=False,
            main_image=property_instance.main_image,
        )
        url = reverse('properties:property_list')
        response = client.get(url)
        assert response.status_code == 200
        assert 'Test Property' in str(response.content)
        assert 'Unavailable Property' not in str(response.content)

    def test_list_empty_when_no_available(self, client, property_data):
        property_data['is_available'] = False
        Property.objects.create(**property_data)
        url = reverse('properties:property_list')
        response = client.get(url)
        assert response.status_code == 200
        assert 'No properties available' in str(response.content)

    def test_list_uses_correct_template(self, client, db):
        url = reverse('properties:property_list')
        response = client.get(url)
        assert 'properties/property_list.html' in [t.name for t in response.templates]


class TestPropertyDetailView:
    def test_detail_returns_available_property(self, client, property_instance):
        url = reverse('properties:property_detail', args=[property_instance.id])
        response = client.get(url)
        assert response.status_code == 200
        assert 'Test Property' in str(response.content)

    def test_detail_returns_404_for_unavailable(self, client, property_data):
        property_data['is_available'] = False
        prop = Property.objects.create(**property_data)
        url = reverse('properties:property_detail', args=[prop.id])
        response = client.get(url)
        assert response.status_code == 404

    def test_detail_returns_404_for_nonexistent(self, client, db):
        url = reverse('properties:property_detail', args=['00000000-0000-0000-0000-000000000000'])
        response = client.get(url)
        assert response.status_code == 404

    def test_detail_uses_correct_template(self, client, property_instance):
        url = reverse('properties:property_detail', args=[property_instance.id])
        response = client.get(url)
        assert 'properties/property_detail.html' in [t.name for t in response.templates]

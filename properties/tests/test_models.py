import pytest
from django.core.exceptions import ValidationError
from properties.models import Property


class TestPropertyModel:
    def test_create_property(self, property_data):
        prop = Property(**property_data)
        prop.full_clean()
        prop.save()
        assert prop.title == 'Test Property'
        assert prop.price == 1500.00
        assert prop.status == Property.Status.ON_RENT

    def test_price_must_be_positive(self, property_data):
        property_data['price'] = 0
        with pytest.raises(ValidationError):
            prop = Property(**property_data)
            prop.full_clean()

    def test_price_must_be_greater_than_zero(self, property_data):
        property_data['price'] = -100
        with pytest.raises(ValidationError):
            prop = Property(**property_data)
            prop.full_clean()

    def test_str_returns_title(self, property_instance):
        assert str(property_instance) == 'Test Property'

    def test_default_ordering(self, property_data):
        Property.objects.create(**property_data)
        Property.objects.create(**{**property_data, 'title': 'Older Property'})
        properties = Property.objects.all()
        assert properties[0].title == 'Older Property'
        assert properties[1].title == 'Test Property'

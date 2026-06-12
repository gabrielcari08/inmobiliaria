import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from properties.models import Property


@pytest.fixture
def property_data(db):
    return {
        'title': 'Test Property',
        'description': 'A nice place to live',
        'price': 1500.00,
        'location': 'Downtown',
        'bedrooms': 2,
        'bathrooms': 1,
        'status': Property.Status.AVAILABLE,
        'main_image': SimpleUploadedFile(
            name='test.jpg',
            content=b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\xff\xff\xff\x00\x00\x00\x21\xf9\x04\x00\x00\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x44\x01\x00\x3b',
            content_type='image/jpeg'
        ),
    }


@pytest.fixture
def property_instance(db, property_data):
    return Property.objects.create(**property_data)

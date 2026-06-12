import uuid
from django.db import models
from django.core.validators import MinValueValidator


class Property(models.Model):

    class Status(models.TextChoices):
        ON_RENT = 'ON_RENT', 'On Rent'
        ON_SALE = 'ON_SALE', 'On Sale'
        RENTED = 'RENTED', 'Rented'
        SALE = 'SALE', 'Sale'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
    )
    location = models.CharField(max_length=255)
    bedrooms = models.PositiveIntegerField(default=1)
    bathrooms = models.PositiveIntegerField(default=1)
    status = models.CharField(
        max_length=10,
        choices=Status,
        default=Status.ON_RENT,
    )
    main_image = models.ImageField(upload_to='properties/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at', 'title']

    def __str__(self):
        return self.title


class PropertyImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='properties/')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.property.title} - Image {self.order}"
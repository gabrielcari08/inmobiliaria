from django.contrib import admin
from django.core.exceptions import ValidationError
from .models import Property


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'location', 'bedrooms', 'bathrooms', 'is_available', 'created_at']
    list_filter = ['is_available', 'bedrooms', 'bathrooms', 'created_at']
    search_fields = ['title', 'location', 'description']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'price', 'location')
        }),
        ('Features', {
            'fields': ('bedrooms', 'bathrooms', 'is_available')
        }),
        ('Media', {
            'fields': ('main_image',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price <= 0:
            raise ValidationError('Price must be greater than zero.')
        return price
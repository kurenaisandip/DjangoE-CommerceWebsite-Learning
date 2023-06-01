from django.contrib import admin
from .models import Products



admin.site.site_header = "Buy and Sell Website"
admin.site.site_title = "Sandip Buying"
admin.site.index_title = "Manage Sandip Buying"

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'desc')
    search_fields = ('name',) # this always has to be tuples

    def set_price_to_zero(self, request, queryset):
        queryset.update(price=0)

    actions = ('set_price_to_zero',)  # this always has to be tuples
    list_editable = ('price', 'desc')

# Register your models here.
admin.site.register(Products, ProductAdmin)
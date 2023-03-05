from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from apps.ecommerce.models import Category, Shop, Product, Cart, Wishlist, Order


@admin.register(Category)
class CategoryMPTTModelAdmin(DraggableMPTTAdmin):
    mptt_level_indent = 20


admin.site.register(Shop)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Wishlist)
admin.site.register(Order)

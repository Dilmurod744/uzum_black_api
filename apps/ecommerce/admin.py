from django.contrib import admin
from django.contrib.admin import ModelAdmin
from mptt.admin import DraggableMPTTAdmin

from apps.ecommerce.models import Category, Shop, Product, Cart, Wishlist, Order


@admin.register(Category)
class CategoryMPTTModelAdmin(DraggableMPTTAdmin):
    mptt_level_indent = 20


admin.site.register(Shop)
admin.site.register(Cart)
admin.site.register(Wishlist)
admin.site.register(Order)


class ProductAdmin(ModelAdmin):
    def get_queryset(self, request):
        # if request.user.is_superuser:
        #     return super(ProductAdmin, self).get_queryset(request)
        # else:
            qs = super(ProductAdmin, self).get_queryset(request)
            return qs.filter(owner=request.user)


admin.site.register(Product, ProductAdmin)

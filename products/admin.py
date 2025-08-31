from django.contrib import admin
from .models import (
    Category,
    Product,
    ColorVariant,
    SizeVariant,
    ProductImage,
    Coupon,
    ProductReview,
    Wishlist
)

class ProductImageAdmin(admin.StackedInline):
    model = ProductImage
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]
    list_display = ['product_name', 'category', 'price', 'newest_product']
    prepopulated_fields = {'slug': ('product_name',)}

class SizeVariantAdmin(admin.ModelAdmin):
    list_display = ['uid', 'size_name', 'price']

class ColorVariantAdmin(admin.ModelAdmin):
    list_display = ['uid', 'color_name', 'price']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'slug']

class CouponAdmin(admin.ModelAdmin):
    list_display = ['coupon_code', 'discount_amount', 'minimum_amount', 'is_expired']

class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'stars', 'date_added']

class WishlistAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'size_variant', 'added_on']

#Register all models
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ColorVariant, ColorVariantAdmin)
admin.site.register(SizeVariant, SizeVariantAdmin)
admin.site.register(Coupon, CouponAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(Wishlist, WishlistAdmin)




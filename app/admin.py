from django.contrib import admin
from app.models import Product, Category, Image, Banner

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1
        
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = ('name', 'price')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')

class ImageAdmin(admin.ModelAdmin):
    search_fields = ['product__name']
    list_display = ('product_name', 'image')

    def product_name(self, obj):
        return obj.product.name
    
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'banner')

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Banner, BannerAdmin)



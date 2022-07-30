from django.contrib import admin

# Register your models here.
from .models import Category, Product, ProductImage, BannerImage
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['category_name', 'slug']
	prepopulated_fields = {'slug': ('category_name',)}
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 
	'description', 'pub_date', 'year']
	list_filter = ['year', 'pub_date', 'size']
	prepopulated_fields = {'slug': ('name',)}


admin.site.register(BannerImage)
from django.contrib import admin
from models import Category, Product, Message
# Register your models here.


class SlugAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Category, SlugAdmin)
admin.site.register(Product, SlugAdmin)
admin.site.register(Message)
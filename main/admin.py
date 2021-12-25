from django.contrib import admin

from main.models import buyer, seller

# Register your models here.

class sellerAdmin(admin.ModelAdmin):
    list_display = ['name','phone','email','nid','address']

class buyerAdmin(admin.ModelAdmin):
    list_display=['name','phone','email','nid','address']


admin.site.register(seller,sellerAdmin)
admin.site.register(buyer,buyerAdmin)
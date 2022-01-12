from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import  *

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active','is_buyer','is_seller')
    list_filter = ('email', 'is_staff', 'is_active','is_buyer','is_seller')
    fieldsets = (
        (None, {'fields': ('full_name','email', 'password','address')}),
        ('Permissions', {'fields': ('is_staff', 'is_active','is_buyer','is_seller')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('full_name','email', 'password1', 'password2','address' ,'is_staff', 'is_active','is_buyer','is_seller')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(ExtraInformation)
admin.site.register(Buyer)
admin.site.register(LandInformation)
admin.site.register(Seller)
admin.site.register(SellerLands)
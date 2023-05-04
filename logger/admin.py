from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Customer, Mkubwa

# class CustomUserAdmin(UserAdmin):
#     # Define the columns that will be displayed in the user list view
#     list_display = ('username', 'email', 'first_name', 'last_name')

#     # Define the fields that will be displayed in the user edit view
#     fieldsets = (
#         (None, {'fields': ('username', 'email', 'password')}),
#         ('Personal info', {'fields': ('first_name', 'last_name', 'phone_number', 'loyalty_points')}),
#         ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
#     )

# class CustomerAdmin(CustomUserAdmin):
#     model= Customer

# class MkubwaAdmin(CustomUserAdmin):
#     model= Mkubwa
#     fieldsets = (
#         (None, {'fields': ('username', 'email', 'password')}),
#         ('Personal info', {'fields': ('first_name', 'last_name')}),
#         ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
#         ('Mkubwa info', {'fields': ('is_admin',)}),
#     )

#     # Override the queryset to only show Mkubwa users
#     def get_queryset(self, request):
#         qs = super().get_queryset(request)
#         return qs.filter(is_admin=True)

# # Register the models with the admin site
# admin.site.register(Customer, CustomerAdmin)
# admin.site.register(Mkubwa, MkubwaAdmin)

admin.site.register(Customer)
admin.site.register(Mkubwa)
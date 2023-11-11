from django.contrib import admin
from .models import*
# Register your models here.
@admin.register(companyapi)


class companyadmin(admin.ModelAdmin):
    list_display=('name','location')
    search_fields=('name',)
    
@admin.register(employee)

class employeeadmin(admin.ModelAdmin):
    list_display=('name','age','phone_number','address' ,'position','company')
    search_fields=('name','company__name'),
    list_filter=('name','company')
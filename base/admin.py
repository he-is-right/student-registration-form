from django.contrib import admin
from base.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'email', 'payment_status', 'location')
    search_fields = ('first_name', 'email')

admin.site.register(Student, StudentAdmin)


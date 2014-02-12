from django.contrib import admin
from Attendance.models import Organization, Meeting, AttendanceRecord

# Register your models here.

class MeetingInline(admin.TabularInline):
    model = Meeting

class OrganizationAdmin(admin.ModelAdmin):
    inlines = [MeetingInline]


admin.site.register(Organization, OrganizationAdmin)
admin.site.register(AttendanceRecord)

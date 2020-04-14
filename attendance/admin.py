from django.contrib import admin
from .models import *


# Register your models here.

class StudentInline(admin.StackedInline):
    model = Student


class TeacherInline(admin.TabularInline):
    model = Teacher


class StudentAdmin(admin.ModelAdmin):
    #inlines = [StudentInline, TeacherInline]
    list_display = ['er_no', 'name', 'gender']
    search_fields = ['er_no', 'name']


admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Attendance)
admin.site.register(Student, StudentAdmin)

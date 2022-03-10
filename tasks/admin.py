from django.contrib import admin
from django.contrib import admin
from tasks.models import Student
# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('Student_ID', 'Student_fname', 'Student_lname', 'Birth_Date')
admin.site.register(Student,TaskAdmin)

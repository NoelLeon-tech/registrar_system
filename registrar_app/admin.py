from django.contrib import admin
from .models import *
from .forms import *
# Register your models here.
admin.site.site_header = "Registrar Queuing Database"


class QueueAdmin(admin.ModelAdmin):
    list_display = ('id','number', 'student', 'date_created', 'time_created', 'time_finished', 'status') 
    form = QueueForm

admin.site.register(Queue, QueueAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'first_name', 'middle_name', 'last_name')

admin.site.register(Student, StudentAdmin) 
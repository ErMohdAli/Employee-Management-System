from django.contrib import admin
from .models import Emp,Testimonial
# Register your models here
# .



class modelEMP(admin.ModelAdmin):
    list_display = ['name','emp_id','working','department',] 
    list_editable=('working','emp_id')
    search_fields=('name','phone')
    list_filter=('working',)

admin.site.register(Emp, modelEMP)
admin.site.register(Testimonial)
from django.contrib import admin

# Register your models here.
from studentapp.models import City, Course, Student

admin.site.register(City)
admin.site.register(Course)
admin.site.register(Student)


from django.contrib import admin

# aca se importan todos los modelos con las tablas 
from django_pjt.app.targetas.models import *

# Register your models here.



admin.site.register(Alumno)
admin.site.register(curso)
admin.site.register(matricula)



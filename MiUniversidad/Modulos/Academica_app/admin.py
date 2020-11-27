from django.contrib import admin
from .models import Carrera, Estudiante, Matricula, Curso

# Register your models here.
admin.site.register(Carrera)
admin.site.register(Estudiante)
admin.site.register(Matricula)
admin.site.register(Curso)

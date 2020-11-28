from django.db import models

# Create your models here.


class Carrera(models.Model):
    codigo = models.CharField(max_length=3, primary_key=True)
    nombre = models.CharField(max_length=50)
    duracion = models.PositiveSmallIntegerField(default=5)

   # Se debe dar formato al objeto, sobre escribo el str
   # Los objetos se van a mostrar con el siguiente formato
   # al llamr a todo el objeto Carrera ...tengo acceso a todo el metodo de abajo, él cual ya tiene FORMATO

    def __str__(self):
        txt = "{0} (Duración:{1} años)"
        return txt.format(self.nombre, self.duracion)


class Estudiante(models.Model):
    dni = models.CharField(max_length=8, primary_key=True)
    apellidoPaterno = models.CharField(max_length=35)
    apellidoMaterno = models.CharField(max_length=35)
    nombres = models.CharField(max_length=35)
    fechaNacimiento = models.DateField()
    sexos = [('F', 'Femenino'), ('M', 'Masculino')]
    sexo = models.CharField(max_length=1, choices=sexos, default='F')
    carrera = models.ForeignKey(
        Carrera, null=False, blank=False, on_delete=models.CASCADE)
    vigencia = models.BooleanField(default=True)

    def nombreCompleto(self):  # metodo
        txt = "{0} {1} {2} "
        return txt.format(self.apellidoPaterno, self.apellidoMaterno, self.nombres)

    def __str__(self):  # se da formato al objeto para visulalizar en la interface
        txt = "{0}| Carrera: {1} | {2}"
        if self.vigencia:
            estadoEstudiante = "Vigente"
        else:
            estadoEstudiante = "De baja"
        return txt.format(self.nombreCompleto(), self.carrera, estadoEstudiante)


class Curso(models.Model):
    codigo = models.CharField(max_length=6, primary_key=True)
    nombre = models.CharField(max_length=30)
    creditos = models.PositiveSmallIntegerField()
    docente = models.CharField(max_length=100)

    def __str__(self):
        txt = "código: {0} | materia: {1} | Profesor: {2}"
        return txt.format(self.codigo, self.nombre, self.docente)


class Matricula(models.Model):
    idMatricula = models.AutoField(primary_key=True)
    fechaMatricula = models.DateTimeField(auto_now_add=True)
    estudiante = models.ForeignKey(
        Estudiante, null=False, blank=False, on_delete=models.CASCADE)
    curso = models.ForeignKey(
        Curso, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):

        txt = "{0} | {1} "

        return txt.format(self.curso, self.fechaMatricula)

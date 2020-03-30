from django.db import models

# Create your models here.

class Alumno (models.Model):
    Apellidopaterno = models.CharField(max_length=40)
    Apellimaterno = models.CharField(max_length=40)
    nombres = models.CharField(max_length=40)
    dni = models.CharField(max_length=8)
    fecha_nacimiento = models.DateField()
    sexos =(('F','Femenino'),('M','Masculino'))
    sexo = models.CharField(max_length=1,choices=sexos,default='M')


    def nombrecompleto(self):
        cadena = "{0} {1}, {2}"
        return cadena.format(self.Apellidopaterno, self.Apellimaterno, self.nombres)

    
    def __str__(self):
        return self.nombrecompleto()



class curso (models.Model):
    nombre = models.CharField(max_length=50)
    creditos = models.PositiveSmallIntegerField()
    estado = models.BooleanField(default=True)


    def __str__(self):
        return "{0} ({1})".format(self.nombre, self.creditos)



class matricula (models.Model):
    alumno = models.ForeignKey(Alumno, null=False, blank=False, on_delete=models.CASCADE)
    cursos = models.ForeignKey(curso, null=False, blank=False, on_delete=models.CASCADE)
    fechamatricula = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        cadena = "{0} => {1}"
        return cadena.format(self.alumno, self.cursos.nombre)


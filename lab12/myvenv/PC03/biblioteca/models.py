from django.db import models

# Create your models here.

class Autor(models.Model):
    IdAutor = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=200)
    Nacionalidad = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.IdAutor}{self.Nombre}{self.Nacionalidad}"

class Usuario(models.Model):
    IdUsuario = models.IntegerField(primary_key=True)
    numUsuario= models.IntegerField()
    nif= models.CharField(max_length=20)
    Nombre= models.CharField(max_length=100)
    Direccion= models.CharField(max_length=255)
    Telefono= models.CharField(max_length=20)

    def _str_(self):
        return f"{self.IdUsuario}{self.numUsuario} {self.nif} {self.nombre} {self.direccion} {self.telefono}"
    
class Libro(models.Model):
    IdLibro = models.IntegerField(primary_key=True)
    codigo= models.IntegerField()
    titulo = models.CharField(max_length=100)
    isbn = models.CharField(max_length=30)
    editorial = models.CharField(max_length=60)
    numPags = models.IntegerField()
    autor= models.ForeignKey(Autor,on_delete=models.CASCADE)

    def _str_(self):
        return f"{self.codigo} {self.titulo} {self.isbn} {self.editorial} {self.numPags} {self.autor}"
    
class Prestamos(models.Model):
    IdPrestamo = models.IntegerField(primary_key=True)
    IdLibro = models.ForeignKey(Libro,on_delete=models.CASCADE)
    IdUsuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    fecPrestamo = models.DateTimeField(null=True,blank=True,)
    fecDevolucion = models.DateTimeField(null=True,blank=True)

    def _str_(self):
        return f"{self.IdPrestamo}{self.IdLibro}{self.IdUsuario}{self.fecPrestamo}{self.fecDevolucion}"
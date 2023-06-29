from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length= 200, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen",upload_to="projects")
    link = models.URLField(verbose_name="Dirección web", null=True, blank = True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación") #fecha y hora, se añadira la hora de creacion
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Edición") #se actualizara  esta fecha y hora cuando lo modifiquemos
    
    
    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "poryectos"
        ordering = ["-created"]
    
    def __str__(self):
        return self.title
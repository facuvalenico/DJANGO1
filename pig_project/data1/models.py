#from distutils.command.upload import upload
from django.db import models

#Create your models here.
class Actualizacion(models.Model):
    valor1 = models.CharField(max_length=100,verbose_name='$CBT')
    valor2 = models.CharField(max_length=100,verbose_name='$m2')
    valor3 = models.CharField(max_length=100,verbose_name='$Auto')
    # title = models.CharField(max_length=100,verbose_name='Título')
    # description = models.TextField(verbose_name='Descripción')
    # image = models.ImageField(verbose_name='Imagen',upload_to = "imagenes")
    # link = models.URLField(verbose_name='Dirección web', null = True, blank= True)
    created = models.DateTimeField(auto_now_add = True, verbose_name = 'fecha de creación')
    updated = models.DateTimeField(auto_now = True, verbose_name = 'fecha de modificación')
    
    
    class Meta:
        verbose_name = 'actualización'   
        verbose_name_plural = 'actualizaciones'    
        ordering = ["-created"]
        
    def __str__(self):
        return self.valor1
    

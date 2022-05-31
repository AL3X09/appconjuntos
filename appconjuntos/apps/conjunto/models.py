from django.db import models

#from simple_history.models import HistoricalRecords


class ConjuntoModel(models.Model):
    name = models.CharField('Nombre', max_length = 255, blank = True, null = False)
    email = models.EmailField('Correo Electrónico',max_length = 255, unique = False)
    telephone = models.CharField('Telefono', max_length = 10, blank = True, null = False)
    logo = models.ImageField('Logo del conjunto', upload_to ='img/conjunto/', max_length = 255, blank = True, null = True)
    Imagen = models.ImageField('Imagen del conjunto', upload_to ='img/conjunto/', max_length = 255, blank = True, null = True)
    adress = models.CharField('Dirección', max_length = 255, blank = True, null = False)
    is_active = models.BooleanField(default = True)
    #historical = HistoricalRecords()
    
    class Meta:
        verbose_name = 'Conjunto'
        verbose_name_plural = 'Conjuntos'

    REQUIRED_FIELDS = ['name', 'email', 'telephone', 'adress']

    #contructor
    def __str__(self):
       return f'{self.name}'


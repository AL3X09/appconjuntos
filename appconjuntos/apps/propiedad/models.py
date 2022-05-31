from django.db import models
from ..conjunto.models import ConjuntoModel

#from simple_history.models import HistoricalRecords
class PropiedadModel(models.Model):
    interior = models.CharField('interior',max_length = 255, unique = True),
    n_casa_o_apto = models.CharField('Número o Letra de Interior',max_length = 255, unique = True),
    t_integrantes = models.IntegerField('Total Integrantes', blank=False, null=False, default=0),
    is_ninos = models.BooleanField(default = False),
    c_ninos = models.IntegerField('Cantidad de niños', blank=False, null=False, default=0),
    is_abuelos = models.BooleanField(default = False),
    c_abuelos = models.IntegerField('Cantidad de abuelos', blank=False, null=False, default=0),
    fk_conjunto = models.ForeignKey(ConjuntoModel, on_delete=models.CASCADE),
    is_habitada = models.BooleanField(default = True),
    is_arriendo = models.BooleanField(default = False),
    is_active = models.BooleanField(default = True)
    #historical = HistoricalRecords()
    
    class Meta:
        verbose_name = 'Propiedad'
        verbose_name_plural = 'Propiedades'


    #contructor
    def __str__(self):
       return f'{self.interior} {self.n_casa_o_apto}'

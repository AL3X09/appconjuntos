from django.db import models
from ..conjunto.models import ConjuntoModel

class CasilleroModel(models.Model):
    is_vacio = models.BooleanField('Esta vacio?', default = False)
    fk_propiedad = models.ForeignKey(ConjuntoModel, on_delete=models.CASCADE, default=1)
    is_active = models.BooleanField(default = True)
    #historical = HistoricalRecords()
    
    class Meta:
        verbose_name = 'Propiedad'
        verbose_name_plural = 'Propiedades'

    #contructor
    def __str__(self):
       return f'{self.interior} {self.n_casa_o_apto}'

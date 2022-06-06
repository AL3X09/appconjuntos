from email.policy import default
from django.db import models


class ParqueaderoModel(models.Model):
    total = models.IntegerField('Total de Espacios', default = False)
    is_active = models.BooleanField(default = True)
    #historical = HistoricalRecords()
    
    class Meta:
        verbose_name = 'AuditoriaPedido'
        verbose_name_plural = 'AuditoriaPedidos'

    #contructor
    def __str__(self):
       return f'{self.comentarios}'

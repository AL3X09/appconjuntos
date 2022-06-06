from django.db import models
from ..conjunto.models import User

class AuditoriaPedidoModel(models.Model):
    code = models.BooleanField('Código', default = False)
    comentarios = models.CharField('Nombre', max_length = 255, null = False, unique = True)
    fecha = models.CharField('Nombre', max_length = 255, null = False, default=now())
    is_esperapedido = models.BooleanField('Pedido Recogido', default = True)
    is_validcode = models.BooleanField('Pedido Recogido', default = False)
    is_recogio = models.BooleanField('Pedido Recogido', default = False)
    fk_casillero = models.ForeignKey(CasilleroModel, on_delete=models.CASCADE, default=1)
    fk_persona = models.ForeignKey(PersonModel, on_delete=models.CASCADE, default=1)
    fk_usuario_recibe = models.ForeignKey(UserModel, on_delete=models.CASCADE, default=1)
    fk_usuario_entrega = models.ForeignKey(UserModel, on_delete=models.CASCADE, default=1)
    is_active = models.BooleanField(default = True)
    #historical = HistoricalRecords()
    
    class Meta:
        verbose_name = 'Propiedad'
        verbose_name_plural = 'Propiedades'

    #contructor
    def __str__(self):
       return f'{self.interior} {self.n_casa_o_apto}'

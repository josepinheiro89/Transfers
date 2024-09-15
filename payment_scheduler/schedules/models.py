from django.db import models
from decimal import Decimal

class PaymentSchedule(models.Model):
    data_pagamento = models.DateField()
    permite_recorrencia = models.BooleanField(default=False)
    quantidade_recorrencia = models.IntegerField(default=0)
    intervalo_recorrencia = models.IntegerField(default=0)
    status_recorrencia = models.CharField(max_length=20)
    agencia = models.IntegerField()
    conta = models.IntegerField()
    valor_pagamento = models.FloatField()  # Salvo como inteiro


    def save(self, *args, **kwargs):
        # Verifica se o valor é decimal e converte para inteiro
        if isinstance(self.valor_pagamento, float) or isinstance(self.valor_pagamento, Decimal):
            self.valor_pagamento = int(self.valor_pagamento)
        super().save(*args, **kwargs)


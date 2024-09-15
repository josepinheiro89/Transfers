from django.db import models

class PaymentSchedule(models.Model):
    data_pagamento = models.DateField()
    permite_recorrencia = models.BooleanField(default=False)
    quantidade_recorrencia = models.IntegerField()
    intervalo_recorrencia = models.IntegerField()
    status_recorrencia = models.CharField(max_length=20)
    agencia = models.IntegerField()
    conta = models.IntegerField()
    valor_pagamento = models.IntegerField()  # Salvo como inteiro

    def save(self, *args, **kwargs):
        # Converte o valor de decimal para inteiro
        self.valor_pagamento = int(self.valor_pagamento)
        super().save(*args, **kwargs)

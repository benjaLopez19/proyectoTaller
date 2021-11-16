from django.db import models

class Data(models.Model):
    mensaje_usuario=models.CharField(max_length=5000, null=True)
    respuesta_bot=models.CharField(max_length=5000, null=True)
    fecha=models.DateTimeField(null=True)
    direccion_ip=models.CharField(max_length=2000, null=True)
    conversation_id=models.CharField(max_length=2000, null=True)
    dialog_stack=models.CharField(max_length=2000, null=True)
    dialog_turn_counter=models.CharField(max_length=2000, null=True)
    dialog_request_counter=models.CharField(max_length=2000, null=True)
    intent=models.CharField(max_length=2000, null=True)
    confidence=models.FloatField(max_length=2000, null=True)
    session_id=models.CharField(max_length=2000, null=True)
    evaluacion=models.CharField(max_length=2000, null=True)
    navegador=models.CharField(max_length=2000, null=True)
    clasificacion=models.CharField(max_length=2000, null=True)
    codigo_respuesta=models.CharField(max_length=2000, null=True)
    sub_clasificacion=models.CharField(max_length=2000, null=True)
    context=models.CharField(max_length=10000, null=True)
    id_button=models.CharField(max_length=2000, null=True)
    canal=models.CharField(max_length=2000, null=True)
    current_url=models.CharField(max_length=2000, null=True)
    feedback_offering=models.BooleanField(null=True)
    feedback_given=models.BooleanField(null=True)

    class Meta:
        verbose_name="Conversación"
        verbose_name_plural="Conversaciones"


# Create your models here.

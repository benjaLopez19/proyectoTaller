# Generated by Django 3.2.9 on 2021-11-15 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensaje_usuario', models.CharField(max_length=1000)),
                ('respuesta_bot', models.CharField(max_length=1000)),
                ('fecha', models.DateTimeField()),
                ('direccion_ip', models.CharField(max_length=1000)),
                ('conversation_id', models.CharField(max_length=1000)),
                ('dialog_stack', models.CharField(max_length=1000)),
                ('dialog_turn_counter', models.CharField(max_length=1000)),
                ('dialog_request_counter', models.CharField(max_length=1000)),
                ('intent', models.CharField(max_length=1000)),
                ('confidence', models.FloatField(max_length=1000)),
                ('session_id', models.CharField(max_length=1000)),
                ('evaluacion', models.CharField(max_length=1000)),
                ('navegador', models.CharField(max_length=1000)),
                ('clasificacion', models.CharField(max_length=1000)),
                ('codigo_respuesta', models.CharField(max_length=1000)),
                ('sub_clasificacion', models.CharField(max_length=1000)),
                ('context', models.CharField(max_length=1000)),
                ('id_button', models.CharField(max_length=1000)),
                ('canal', models.CharField(max_length=1000)),
                ('current_url', models.CharField(max_length=1000)),
                ('feedback_offering', models.BooleanField()),
                ('feedback_given', models.BooleanField()),
            ],
        ),
    ]

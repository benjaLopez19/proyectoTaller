# Generated by Django 3.2.9 on 2021-11-15 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_alter_data_context'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='canal',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='clasificacion',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='codigo_respuesta',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='confidence',
            field=models.FloatField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='context',
            field=models.CharField(max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='conversation_id',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='current_url',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='dialog_request_counter',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='dialog_stack',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='dialog_turn_counter',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='direccion_ip',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='evaluacion',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='fecha',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='feedback_given',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='feedback_offering',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='id_button',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='intent',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='mensaje_usuario',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='navegador',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='respuesta_bot',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='session_id',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='sub_clasificacion',
            field=models.CharField(max_length=2000, null=True),
        ),
    ]

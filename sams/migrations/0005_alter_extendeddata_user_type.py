# Generated by Django 4.2.4 on 2023-09-20 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sams', '0004_extendeddata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extendeddata',
            name='user_type',
            field=models.CharField(choices=[('B', 'Comprador'), ('R', 'Resurtidor')], max_length=1),
        ),
    ]

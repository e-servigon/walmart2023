# Generated by Django 4.2.4 on 2023-09-26 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sams', '0005_alter_extendeddata_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]

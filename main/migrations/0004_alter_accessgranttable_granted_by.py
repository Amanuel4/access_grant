# Generated by Django 4.2 on 2024-06-26 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_accessgranttable_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessgranttable',
            name='granted_by',
            field=models.CharField(max_length=64),
        ),
    ]

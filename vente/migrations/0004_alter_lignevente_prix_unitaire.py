# Generated by Django 5.1.7 on 2025-04-01 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vente', '0003_alter_lignevente_prix_unitaire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lignevente',
            name='prix_unitaire',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]

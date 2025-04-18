# Generated by Django 5.1.7 on 2025-04-01 02:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stock', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_vente', models.DateTimeField(auto_now_add=True)),
                ('client', models.CharField(blank=True, max_length=255, null=True)),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ventes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LigneVente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.PositiveIntegerField()),
                ('prix_unitaire', models.DecimalField(decimal_places=2, max_digits=10)),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lignes_vente', to='stock.produit')),
                ('vente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lignes', to='vente.vente')),
            ],
        ),
    ]

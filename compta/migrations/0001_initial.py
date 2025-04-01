# Generated by Django 5.1.7 on 2025-04-01 04:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vente', '0004_alter_lignevente_prix_unitaire'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_emission', models.DateTimeField(auto_now_add=True)),
                ('montant_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('est_payee', models.BooleanField(default=False)),
                ('vente', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='facture', to='vente.vente')),
            ],
        ),
        migrations.CreateModel(
            name='Paiement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_paiement', models.DateTimeField(auto_now_add=True)),
                ('montant', models.DecimalField(decimal_places=2, max_digits=10)),
                ('mode_paiement', models.CharField(choices=[('CASH', 'Espèces'), ('CARD', 'Carte bancaire'), ('TRANSFER', 'Virement bancaire')], max_length=50)),
                ('facture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paiements', to='compta.facture')),
            ],
        ),
    ]

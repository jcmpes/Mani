# Generated by Django 4.2.14 on 2024-08-05 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debts', '0002_debt_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debt',
            name='type',
            field=models.CharField(choices=[('LEND', 'Prestar dinero'), ('LOAN', 'Préstamo recibido')], max_length=4),
        ),
    ]

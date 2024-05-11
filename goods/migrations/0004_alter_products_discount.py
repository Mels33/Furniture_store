# Generated by Django 5.0.6 on 2024-05-11 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4),
        ),
    ]

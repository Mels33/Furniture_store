# Generated by Django 5.0.6 on 2024-05-14 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_alter_products_discount'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ('id',)},
        ),
    ]
# Generated by Django 4.0.3 on 2022-03-27 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='payment_moethod',
            new_name='payment_method',
        ),
    ]
# Generated by Django 3.1.3 on 2020-11-21 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_auto_20201121_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aliment',
            name='nutriscore',
            field=models.CharField(max_length=100),
        ),
    ]

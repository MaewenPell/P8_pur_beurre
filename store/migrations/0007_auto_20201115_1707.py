# Generated by Django 3.1.3 on 2020-11-15 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20201115_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aliment',
            name='nutriscore',
            field=models.CharField(max_length=10),
        ),
    ]

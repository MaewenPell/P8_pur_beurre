# Generated by Django 3.1.3 on 2020-11-15 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20201114_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aliment',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='store.category'),
        ),
    ]

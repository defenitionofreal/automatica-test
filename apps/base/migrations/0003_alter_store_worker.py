# Generated by Django 3.2.7 on 2022-01-10 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20220110_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='worker',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.worker'),
        ),
    ]

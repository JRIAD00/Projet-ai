# Generated by Django 4.2.5 on 2023-09-11 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='image',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

# Generated by Django 2.2 on 2020-09-21 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_auto_20200919_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_height',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_width',
            field=models.IntegerField(blank=True),
        ),
    ]

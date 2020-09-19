# Generated by Django 3.1.1 on 2020-09-19 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_height',
            field=models.IntegerField(default=300),
        ),
        migrations.AddField(
            model_name='product',
            name='image_width',
            field=models.IntegerField(default=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, height_field='image_height', upload_to='media/products/%Y/%m/%d', width_field='image_width'),
        ),
    ]

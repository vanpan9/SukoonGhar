# Generated by Django 4.2.7 on 2024-01-21 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_shop_now_image_alter_shop_now_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop_now',
            name='description',
            field=models.CharField(max_length=2000),
        ),
    ]

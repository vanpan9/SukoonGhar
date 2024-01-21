# Generated by Django 4.2.5 on 2023-11-11 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop_now',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('description', models.CharField(max_length=225)),
                ('image', models.ImageField(upload_to='media/shop_now_home/%Y%m%d/')),
                ('button_text', models.CharField(max_length=225)),
            ],
        ),
    ]

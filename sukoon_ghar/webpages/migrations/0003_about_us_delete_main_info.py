# Generated by Django 4.2.5 on 2023-11-10 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0002_main_info_delete_aboutus'),
    ]

    operations = [
        migrations.CreateModel(
            name='About_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.DeleteModel(
            name='Main_info',
        ),
    ]

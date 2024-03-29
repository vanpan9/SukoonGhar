# Generated by Django 4.2.5 on 2023-11-10 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0003_about_us_delete_main_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aboutus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_title', models.CharField(max_length=225)),
                ('main_description', models.CharField(max_length=225)),
                ('image', models.ImageField(upload_to='media/aboutus/%Y%m%d/')),
                ('sub_title', models.CharField(max_length=225)),
                ('sub_description', models.CharField(max_length=225)),
            ],
        ),
        migrations.DeleteModel(
            name='About_us',
        ),
    ]

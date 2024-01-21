# Generated by Django 4.2.7 on 2023-11-16 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0013_member_delete_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('role', models.CharField(max_length=225)),
                ('description', models.CharField(max_length=225)),
                ('image', models.ImageField(upload_to='media/team/%Y%m%d/')),
                ('fb_link', models.CharField(max_length=225)),
                ('insta_link', models.CharField(max_length=225)),
            ],
        ),
        migrations.DeleteModel(
            name='Member',
        ),
    ]

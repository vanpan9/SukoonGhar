# Generated by Django 4.2.7 on 2023-11-16 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0014_team_delete_member'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecentPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('description', models.CharField(max_length=225)),
                ('post_link', models.CharField(max_length=225)),
            ],
        ),
    ]
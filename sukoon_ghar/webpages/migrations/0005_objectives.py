# Generated by Django 4.2.5 on 2023-11-11 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0004_aboutus_delete_about_us'),
    ]

    operations = [
        migrations.CreateModel(
            name='Objectives',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('Skill Diversification', 'Skill Diversification'), ('Mental Health Support', 'Mental Health Support'), ('Digital Literacy', 'Digital Literacy'), ('Parenting Workshops', 'Parenting Workshops'), ('Financial Literacy', 'Financial Literacy'), ('Health and Nutrition', 'Health and Nutrition'), ('Community Engagement', 'Community Engagement'), ('Art and Expression', 'Art and Expression'), ('Education Empowerment', 'Education Empowerment')], max_length=225)),
                ('description', models.CharField(max_length=225)),
                ('icon', models.CharField(choices=[('bi bi-puzzle', 'Skill Diversification'), ('bi bi-emoji-smile', 'Mental Health Support'), ('bi bi-laptop', 'Digital Literacy'), ('bi bi-people', 'Parenting Workshops'), ('bi bi-cash', 'Financial Literacy'), ('bi bi-heart', 'Health and Nutrition'), ('bi bi-chat-square', 'Community Engagement'), ('bi bi-palette', 'Art and Expression'), ('bi bi-book', 'Education Empowerment')], max_length=225)),
            ],
        ),
    ]
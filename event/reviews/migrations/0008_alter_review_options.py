# Generated by Django 5.1.2 on 2024-11-17 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0007_alter_review_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['is_published', '-created_at', '-rating'], 'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
    ]

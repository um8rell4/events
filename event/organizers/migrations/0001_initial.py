# Generated by Django 4.2.16 on 2024-11-08 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0015_remove_event_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventOrganizer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_status', models.IntegerField(choices=[(1, 'Подготовка'), (2, 'В процессе'), (3, 'Завершен'), (4, 'Отменен')], default=1, verbose_name='Статус мероприятия')),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
            ],
            options={
                'verbose_name': 'Статус мероприятия',
                'verbose_name_plural': 'Статусы мероприятий',
            },
        ),
    ]
# Generated by Django 3.2.8 on 2021-11-07 21:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('public_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=1023)),
                ('description', models.TextField(blank=True, default='')),
                ('status', models.CharField(choices=[('active', 'Активна'), ('closed', 'Закрыта')], default='active', max_length=255)),
                ('fee', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('reward', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'task',
                'verbose_name_plural': 'tasks',
                'db_table': 'task',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddIndex(
            model_name='task',
            index=models.Index(fields=['status'], name='task_status_e9a322_idx'),
        ),
    ]

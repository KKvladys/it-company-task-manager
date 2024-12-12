# Generated by Django 5.1.3 on 2024-12-06 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[(0, 'Urgent'), (1, 'High'), (2, 'Medium'), (3, 'Low')], max_length=6),
        ),
    ]

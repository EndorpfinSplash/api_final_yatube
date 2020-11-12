# Generated by Django 3.1.3 on 2020-11-11 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20201110_1551'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='slug',
        ),
        migrations.AddField(
            model_name='post',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='api.group'),
        ),
    ]

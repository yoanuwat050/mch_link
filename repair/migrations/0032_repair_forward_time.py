# Generated by Django 4.1 on 2022-09-22 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0031_repair_repairstaffforward'),
    ]

    operations = [
        migrations.AddField(
            model_name='repair',
            name='forward_time',
            field=models.DateTimeField(blank=True, default='1992-11-03 23:09:42'),
        ),
    ]
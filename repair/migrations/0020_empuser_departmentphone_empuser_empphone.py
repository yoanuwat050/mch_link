# Generated by Django 4.1 on 2022-09-22 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0019_alter_repair_done_time_alter_repair_recieve_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='empuser',
            name='departmentPhone',
            field=models.CharField(default='-', max_length=10),
        ),
        migrations.AddField(
            model_name='empuser',
            name='empPhone',
            field=models.CharField(default='-', max_length=10),
        ),
    ]

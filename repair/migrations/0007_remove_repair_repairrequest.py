# Generated by Django 4.1 on 2022-09-16 23:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0006_repair_repairrequest_alter_repair_repairreviewdetail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='repair',
            name='repairRequest',
        ),
    ]
# Generated by Django 4.1 on 2022-09-17 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0013_alter_repair_repairdesc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repair',
            name='repairReviewDetail',
            field=models.TextField(default='รอการรีวิว', max_length=500),
        ),
    ]

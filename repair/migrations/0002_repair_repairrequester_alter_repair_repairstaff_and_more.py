# Generated by Django 4.1 on 2022-09-15 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='repair',
            name='repairRequester',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='repair.empuser'),
        ),
        migrations.AlterField(
            model_name='repair',
            name='repairStaff',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='repair.repairstaff'),
        ),
        migrations.AlterField(
            model_name='repair',
            name='repairStatus',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='repair.repairstatus'),
        ),
    ]

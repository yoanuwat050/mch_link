# Generated by Django 4.1 on 2022-09-15 23:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0003_repairreview_alter_repair_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='repair',
            name='repairReview',
            field=models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, to='repair.repairreview'),
        ),
        migrations.AddField(
            model_name='repair',
            name='repairReviewDetail',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]

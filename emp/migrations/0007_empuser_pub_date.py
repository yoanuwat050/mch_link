# Generated by Django 4.1 on 2022-09-29 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0006_remove_empuser_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='empuser',
            name='pub_date',
            field=models.DateTimeField(default=12, verbose_name='date published'),
            preserve_default=False,
        ),
    ]

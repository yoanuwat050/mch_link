# Generated by Django 4.1 on 2022-09-22 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0023_empuser_empslug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empuser',
            name='empslug',
            field=models.SlugField(blank=True, max_length=5),
        ),
    ]
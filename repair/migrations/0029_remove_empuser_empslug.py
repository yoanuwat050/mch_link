# Generated by Django 4.1 on 2022-09-22 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0028_alter_empuser_empslug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empuser',
            name='empSlug',
        ),
    ]

# Generated by Django 2.1.5 on 2020-06-18 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_todoitem_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='is_completed',
            field=models.BooleanField(default=False, verbose_name='выполнено'),
        ),
    ]
# Generated by Django 2.1.5 on 2020-06-03 07:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todoitem',
            options={'ordering': ('-created',)},
        ),
        migrations.AddField(
            model_name='todoitem',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todoitem',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
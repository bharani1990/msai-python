# Generated by Django 4.0 on 2021-12-22 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='comment',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
    ]

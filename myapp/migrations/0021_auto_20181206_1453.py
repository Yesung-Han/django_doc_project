# Generated by Django 2.1.3 on 2018-12-06 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_auto_20181206_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='parent_post',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 2.1.3 on 2018-12-07 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0023_auto_20181207_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='g_order',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='parent_post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Post'),
        ),
    ]

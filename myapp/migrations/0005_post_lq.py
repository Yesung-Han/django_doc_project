# Generated by Django 2.1.3 on 2018-12-05 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_post_linked_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='lq',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.Post'),
        ),
    ]

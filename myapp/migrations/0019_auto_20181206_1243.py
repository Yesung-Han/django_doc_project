# Generated by Django 2.1.3 on 2018-12-06 03:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_auto_20181205_2256'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('modify_date',), 'verbose_name': 'post', 'verbose_name_plural': 'posts'},
        ),
        migrations.RemoveField(
            model_name='post',
            name='group_no',
        ),
        migrations.RemoveField(
            model_name='post',
            name='group_order',
        ),
        migrations.RemoveField(
            model_name='post',
            name='group_order_2',
        ),
        migrations.AddField(
            model_name='post',
            name='parent_post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Post'),
        ),
    ]

# Generated by Django 2.1.3 on 2018-12-05 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20181205_2007'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-parent_post__id', '-id', 'parent_post_id'), 'verbose_name': 'post', 'verbose_name_plural': 'posts'},
        ),
    ]

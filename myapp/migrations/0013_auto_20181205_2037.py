# Generated by Django 2.1.3 on 2018-12-05 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_auto_20181205_2035'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('parent_post', '-id', '-modify_date'), 'verbose_name': 'post', 'verbose_name_plural': 'posts'},
        ),
    ]

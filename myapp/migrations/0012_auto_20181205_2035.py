# Generated by Django 2.1.3 on 2018-12-05 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_auto_20181205_2033'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('parent_post', '-id', '-parent_post'), 'verbose_name': 'post', 'verbose_name_plural': 'posts'},
        ),
    ]

# Generated by Django 2.1.3 on 2018-12-05 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20181205_2027'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-parent_post', '-id', 'parent_post'), 'verbose_name': 'post', 'verbose_name_plural': 'posts'},
        ),
        migrations.AlterField(
            model_name='post',
            name='parent_post',
            field=models.IntegerField(default=0),
        ),
    ]

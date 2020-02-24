# Generated by Django 2.2 on 2020-02-24 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0011_auto_20200224_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='list_parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lists.List'),
        ),
        migrations.AlterField(
            model_name='list',
            name='name',
            field=models.TextField(default='', null=True),
        ),
    ]

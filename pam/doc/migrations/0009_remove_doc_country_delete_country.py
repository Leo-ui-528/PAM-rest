# Generated by Django 4.0.6 on 2022-07-20 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0008_remove_country_name_country_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doc',
            name='country',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
    ]

# Generated by Django 3.2.8 on 2021-12-10 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratemylandlord', '0003_alter_rating_rating'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='landlord',
            table='ratemylandlord_landlord',
        ),
        migrations.AlterModelTable(
            name='property',
            table='ratemylandlord_property',
        ),
        migrations.AlterModelTable(
            name='rating',
            table='ratemylandlord_rating',
        ),
        migrations.AlterModelTable(
            name='user',
            table='ratemylandlord_user',
        ),
    ]

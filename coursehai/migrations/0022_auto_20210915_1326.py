# Generated by Django 3.2.6 on 2021-09-15 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coursehai', '0021_ownshop'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ownshop',
            old_name='desc',
            new_name='desc1',
        ),
        migrations.RenameField(
            model_name='ownshop',
            old_name='image',
            new_name='image1',
        ),
        migrations.RenameField(
            model_name='ownshop',
            old_name='price',
            new_name='price1',
        ),
        migrations.RenameField(
            model_name='ownshop',
            old_name='pub_date',
            new_name='pub_date1',
        ),
        migrations.RenameField(
            model_name='ownshop',
            old_name='name',
            new_name='title',
        ),
    ]

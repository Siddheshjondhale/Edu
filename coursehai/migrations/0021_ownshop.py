# Generated by Django 3.2.6 on 2021-09-14 09:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('coursehai', '0020_auto_20210914_0224'),
    ]

    operations = [
        migrations.CreateModel(
            name='ownshop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('desc', models.CharField(max_length=500)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(default='courseapp\\images\\shoe.jpg', upload_to='courseapp\\images')),
                ('pub_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]

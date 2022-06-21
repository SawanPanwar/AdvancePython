# Generated by Django 2.2.5 on 2022-06-10 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ORS', '0002_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'VEHICLE',
            },
        ),
    ]

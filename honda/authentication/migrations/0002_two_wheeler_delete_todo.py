# Generated by Django 4.1 on 2022-09-06 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Two_wheeler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bike_title', models.CharField(max_length=100)),
                ('status', models.CharField(default='available', max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Todo',
        ),
    ]
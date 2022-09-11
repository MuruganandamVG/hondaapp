# Generated by Django 4.1 on 2022-09-06 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_alter_four_wheeler_available_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='four_wheeler',
            name='Available',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='four_wheeler',
            name='Booked',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='four_wheeler',
            name='Totalstock',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='two_wheeler',
            name='Available',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='two_wheeler',
            name='Booked',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='two_wheeler',
            name='Totalstock',
            field=models.IntegerField(default=5),
        ),
    ]

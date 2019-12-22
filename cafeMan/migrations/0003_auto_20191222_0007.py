# Generated by Django 2.2.5 on 2019-12-21 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafeMan', '0002_auto_20191221_1624'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='dish',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=4.0, max_digits=2),
        ),
    ]

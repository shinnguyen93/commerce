# Generated by Django 3.1.5 on 2021-02-05 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_auctionlisting_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.CharField(max_length=64, null=True),
        ),
    ]

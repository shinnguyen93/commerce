# Generated by Django 3.1.5 on 2021-02-05 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_auto_20210205_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionlisting',
            name='price',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='listing_price', to='auctions.item'),
        ),
    ]

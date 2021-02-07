# Generated by Django 3.1.5 on 2021-02-07 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_auctionlisting_createtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bidding',
            name='listedBy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bid_listed_by', to='auctions.auctionlisting'),
        ),
    ]
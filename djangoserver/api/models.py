from django.db import models

# Create your models here.
class MarketFeed(models.Model):
    id = models.IntegerField(max_length=10, primary_key=True)
    symbol = models.CharField(max_length=200)
    price = models.CharField(max_length=100)
    onehrper = models.CharField(max_length=10)
    twentyfourhrper = models.CharField(max_length=10)
    sevendayper = models.CharField(max_length=10)
    marketcap = models.CharField(max_length=100)
    volume24h = models.CharField(max_length=100)
    volume24h1 = models.CharField(max_length=100)
    circulatingsupply = models.CharField(max_length=100)

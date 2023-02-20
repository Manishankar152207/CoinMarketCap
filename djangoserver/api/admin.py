from django.contrib import admin
from .models import MarketFeed

# Register your models here.
@admin.register(MarketFeed)
class MarketFeedAdmin(admin.ModelAdmin):
    list_display = ['id','symbol','price', 'onehrper','twentyfourhrper','sevendayper','marketcap','volume24h','volume24h1','circulatingsupply']

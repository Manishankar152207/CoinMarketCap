from rest_framework import serializers
from api.models import MarketFeed

class MarketFeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketFeed
        fields = ['id','symbol','price', 'onehrper','twentyfourhrper','sevendayper','marketcap','volume24h','volume24h1','circulatingsupply']

    def create(self, validated_data):
        return super().create(validated_data)
    
    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)


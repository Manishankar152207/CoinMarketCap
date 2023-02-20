from .models import MarketFeed
from .serializers import MarketFeedSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
import json

class market_feed(viewsets.ModelViewSet):
    queryset = MarketFeed.objects.all()
    serializer_class = MarketFeedSerializer

    
    def create(self, request, *args, **kwargs):
        data = json.loads(request.body.decode())
        many = isinstance(data, list)
        if not self.queryset:
            serializer = self.get_serializer(data=data, many=many)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED,
                    headers=headers
            )
        else:
            for item in data:
                # import ipdb;ipdb.set_trace()
                id = item.pop("id")
                if id:
                    ins = MarketFeed.objects.filter(id=id).last()
                    if ins:
                        update(ins, item)
                    else:
                        # import ipdb;ipdb.set_trace()
                        item.update({"id":id})
                        serializer = self.get_serializer(data=item)
                        serializer.is_valid(raise_exception=True)
                        self.perform_create(serializer)
            return Response({"success":True})


def update(instance, validated_data):
    instance.price = validated_data.get('price',instance.price)
    instance.onehrper = validated_data.get('onehrper', instance.onehrper)
    instance.twentyfourhrper = validated_data.get('twentyfourhrper', instance.twentyfourhrper)
    instance.sevendayper = validated_data.get('sevendayper',instance.sevendayper)
    instance.marketcap = validated_data.get('marketcap', instance.marketcap)
    instance.volume24h = validated_data.get('volume24h', instance.volume24h)
    instance.volume24h1 = validated_data.get('volume24h1',instance.volume24h1)
    instance.circulatingsupply = validated_data.get('circulatingsupply', instance.circulatingsupply)
    instance.save()
    return instance







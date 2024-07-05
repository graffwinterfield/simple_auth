from .models import Maps, User
from rest_framework.serializers import ModelSerializer


class MapsSerializer(ModelSerializer):

    class Meta:
        model = Maps
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.get(id=validated_data['user'])
        validated_data['user'] = user
        maps = Maps.objects.create(**validated_data)
        maps.save()

    def update(self, instance, validated_data):
        instance.maps = validated_data.get('maps', instance.maps)
        instance.save()

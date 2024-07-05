from rest_framework.serializers import ModelSerializer
from accounts.models import User, Maps


class MapSerializer(ModelSerializer):
    class Meta:
        model = Maps
        fields = ['maps', 'user']

    def create(self, validated_data):
        user = User.objects.get(id=validated_data['user'])
        validated_data['user'] = user
        maps = Maps.objects.create(**validated_data)
        maps.save()

    def update(self, instance, validated_data):
        instance.maps = validated_data.get('maps', instance.maps)
        instance.save()


class UserSerializer(ModelSerializer):
    maps = MapSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['username', 'id', 'maps']

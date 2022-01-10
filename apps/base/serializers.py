from rest_framework import serializers
from apps.base.models import Worker, Store, Visit


class WorkerSerializer(serializers.ModelSerializer):
    """ Worker Serializer """

    class Meta:
        model = Worker
        fields = ('id', 'name', 'phone')


class StoreSerializer(serializers.ModelSerializer):
    """ Store Serializer """

    class Meta:
        model = Store
        fields = ('id', 'worker', 'title')


class VisitSerializer(serializers.ModelSerializer):
    """ Visit Serializer """
    store = serializers.ReadOnlyField(source='store.title')

    class Meta:
        model = Visit
        fields = ('id', 'store', 'date', 'latitude', 'longitude')

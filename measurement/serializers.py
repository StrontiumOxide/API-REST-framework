from rest_framework import serializers
from .models import Measurement, Sensor


class MeasurementsSerialier(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'date']


class SensorSerializer(serializers.ModelSerializer):
    measurements = MeasurementsSerialier(many=True)
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']

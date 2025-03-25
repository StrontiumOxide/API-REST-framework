# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

import json
from django.http import HttpRequest
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .models import Sensor, Measurement
from .serializers import SensorSerializer


class SensorView(APIView):
    def get(self, request: HttpRequest) -> Response:
        """Метод по получению датчиков и их измерениях"""

        sensors = Sensor.objects.all()
        res_sensors = SensorSerializer(sensors, many=True)

        return Response(data=res_sensors.data)
    
    def post(self, request: HttpRequest) -> Response:
        """Метод для добавления датчика"""

        data = json.loads(request.body)

        name = data.get('name')
        description = data.get('description')

        sensor = Sensor(name=name, description=description)
        sensor.save()

        return Response(data={'message': f'Датчику {sensor.name} присвоен номер {sensor.pk}'})
    
    def patch(self, request: HttpRequest) -> Response:
        """Метод для обновления информации о датчике"""

        data = json.loads(request.body)

        sensor_id = data.get('id')
        name = data.get('name')
        description = data.get('description')

        sensor = Sensor.objects.get(id=sensor_id)
        
        if name:
            sensor.name = name

        if description:
            sensor.description = description

        sensor.save()

        return Response(data={'message': 'Данные были успешно обновлены!'})
    

class MeasurementView(APIView):
    def post(self, request: HttpRequest) -> Response:
        """Метод для добавления измерением определённым датчиком"""

        data = json.loads(request.body)

        sensor_id = data.get('id')
        temperature = data.get('temperature')

        sensor = Sensor.objects.get(id=sensor_id)
        measurement = Measurement(sensor_id=sensor, temperature=temperature)
        measurement.save()

        return Response(data={'message': f'Датчик №{sensor_id} добавил новое измерение температуры в {temperature} гр. Цельсия'})
    
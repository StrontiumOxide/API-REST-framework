from django.contrib import admin
from .models import Sensor, Measurement


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):

    list_display = ('name', 'description')
    search_fields = ('name',)


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):

    list_display = ('sensor_id', 'temperature', 'date')
    list_filter = ('sensor_id', 'date')
    search_fields = ('sensor_id__name',)

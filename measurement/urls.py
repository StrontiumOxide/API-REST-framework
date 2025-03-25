from django.urls import path
from .views import SensorView, MeasurementView

urlpatterns = [
    path(route='sensors/', view=SensorView.as_view()),
    path(route='measurement/', view=MeasurementView.as_view())
]   

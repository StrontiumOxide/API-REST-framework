from django.db import models


class Sensor(models.Model):

    name = models.CharField(max_length=50, verbose_name='Название датчика')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'

    def __str__(self):
        return self.name


class Measurement(models.Model):

    sensor_id = models.ForeignKey(to=Sensor, on_delete=models.CASCADE, verbose_name='id датчика', related_name='measurements')
    temperature = models.DecimalField(verbose_name='Температура', max_digits=5, decimal_places=2)
    date = models.DateField(verbose_name='Дата и время', auto_now_add=True)

    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'
        ordering = ['-date']

    def __str__(self):
        return f"{self.temperature}°C ({self.date})"
    
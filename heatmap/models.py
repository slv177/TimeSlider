from django.db import models

class Point(models.Model):
    name = models.CharField(max_length=25, verbose_name='Point')
    lat = models.DecimalField(verbose_name='Latitude', decimal_places=6, max_digits=8)
    lon = models.DecimalField(verbose_name='Longitude', decimal_places=6, max_digits=8)
    event = models.CharField(max_length=4, verbose_name='Event', default='2048')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

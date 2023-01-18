from django.db import models


class Station(models.Model):
    """model to station object"""
    RUNNING = 'running'
    BROKEN = 'broken'
    STATUS = [
        (RUNNING, 'в работе'),
        (BROKEN, 'сломана'),

    ]
    name = models.CharField(max_length=50, unique=True, null=False)
    condition = models.CharField(max_length=7, choices=STATUS, default='running')
    date_created = models.DateField(auto_now_add=True, )
    date_broken = models.DateField(blank=True, null=True)
    x = models.IntegerField(default=100)
    y = models.IntegerField(default=100)
    z = models.IntegerField(default=100)

    class Meta:
        verbose_name = 'Станция'
        verbose_name_plural = 'Станции'

    def __str__(self):
        return self.name

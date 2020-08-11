from django.db import models


class City(models.Model):
    name = models.CharField("Город", max_length=255)

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"

    def __str__(self):
        return self.name

from django.db import models
from django.conf import settings


# Create your models here.
class Plot(models.Model):
    area = models.FloatField()  # Area in square units
    location = models.CharField(max_length=255)
    price = models.DecimalField(
        max_digits=10, decimal_places=2
    )  # Price in currency units
    is_available = models.BooleanField(default=True)
    owner = models.CharField(max_length=255, null=True, default="Avihs Builders")
    booked_for = models.CharField(max_length=255, null=True, default="Not Booked")
    booked_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="booked_plots",
    )

    def __str__(self):
        return self.name

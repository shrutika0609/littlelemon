from django.db import models

class Reservation(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.IntegerField()
    booking_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
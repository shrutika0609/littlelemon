from django.test import TestCase
from .models import Reservation
from datetime import datetime

class ReservationModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up test data for the Reservation model
        cls.reservation = Reservation.objects.create(
            first_name="John",
            last_name="Doe"
        )

    def test_fields(self):
        # Test if the first_name and last_name fields are strings
        self.assertIsInstance(self.reservation.first_name, str)
        self.assertIsInstance(self.reservation.last_name, str)

    def test_timestamps(self):
        # Test if the booking_time field is a datetime object
        self.assertIsInstance(self.reservation.booking_time, datetime)
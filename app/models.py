from django.db import models
from django.contrib.auth.models import User


class Plate(models.Model):
    plate_number = models.CharField(max_length=10, unique=True)
    description = models.TextField()
    deadline = models.DateTimeField()
    created_by = models.ForeignKey(User, related_name="created", limit_choices_to={'is_staff': True}, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.plate_number} by {self.created_by}"


class Bid(models.Model):
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    user = models.ForeignKey(User, related_name="bids", limit_choices_to={'is_staff':False}, on_delete=models.CASCADE)
    plate = models.ForeignKey(Plate, related_name="bids", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.plate} - {self.amount}"





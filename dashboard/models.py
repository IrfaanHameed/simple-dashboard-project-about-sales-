# dashboard/models.py

from django.db import models

class Sale(models.Model):
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    STATUS_CHOICES = [
        ('done', 'Done'),
        ('pending', 'Pending'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Sale on {self.date} - ${self.amount} - {self.status}"

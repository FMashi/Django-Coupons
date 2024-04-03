from django.db import models
from company.models import Company


class Coupon(models.Model):
    code = models.CharField(max_length=20, unique=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    description = models.TextField()
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    max_usage = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.company.name} - {self.code}"
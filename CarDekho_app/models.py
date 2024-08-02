from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.


def alphanumberic(value):
    if not str(value).isalnum():
        raise ValidationError(
            "Only alphanumeric characters are allowed")


class showroomList(models.Model):
    name = models.CharField(max_length=30)
    locaton = models.CharField(max_length=100)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name


class Carlist(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    active = models.BooleanField(default=False)
    chassisnumber = models.CharField(
        max_length=100, blank=True, null=True, validators=[alphanumberic])
    price = models.DecimalField(
        max_digits=9, decimal_places=2, blank=True, null=True)

    def _str__(self):
        return self.name

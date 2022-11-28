from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.


class Make(models.Model):
    name = models.CharField(
        max_length=200,
        help_text="Enter the make of the car (e.g. Honda)",
        validators=[MinLengthValidator(2, "La longitud debe ser mayor a 2")],
    )

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name


class Auto(models.Model):
    nickname = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(1, "La longitud debe ser mayor a 1")],
    )
    mileage = models.PositiveIntegerField()
    comments = models.CharField(max_length=300)
    make = models.ForeignKey(Make, on_delete=models.CASCADE, null=False)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.nickname

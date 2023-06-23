from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.



class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Car(models.Model):
    COLOR_CHOICES = (
        ('white', 'White'),
        ('red', 'Red'),
        ('blue','Blue'),
        ('black','Black'),
        ('yellow','Yellow'),
        ('gray','Gray'),
    )


    model = models.CharField(max_length=50)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    color = models.CharField(max_length=50, choices=COLOR_CHOICES)
    value = models.IntegerField(validators=[MinValueValidator(0)])
    production_cost = models.IntegerField(validators=[MinValueValidator(0)])
    transportation_cost = models.IntegerField(validators=[MinValueValidator(0)])


    def __str__(self):
        return f"{self.model} {self.id}"

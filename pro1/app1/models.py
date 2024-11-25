from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import validators
from django.core.validators import MaxLengthValidator,MinLengthValidator,MaxValueValidator,MinValueValidator,EmailValidator
# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField(unique=True,validators=[EmailValidator])
    age=models.PositiveSmallIntegerField()
    marks=models.PositiveSmallIntegerField(validators=[MaxValueValidator(100),MinValueValidator(0)])
    address=models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name



from django.db import models
from django.contrib import admin
class car(models.Model):
    carid=models.CharField(max_length=20,help_text="CAR ID")
    carname=models.CharField(max_length=100)
    price=models.IntegerField()
    model=models.CharField()

class caradmin(admin.ModelAdmin):
    list_display=('carid','carname','price','model')

# Create your models here.

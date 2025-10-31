# Ex02 Django ORM Web Application
## Date: 26-10-2025

## AIM
To develop a Django application to store and retrieve data from Car Inventory Database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
admin.py
```
from django.contrib import admin
from .models import car,caradmin
admin.site.register(car,caradmin)

```
models.py
```
from django.db import models
from django.contrib import admin
class car(models.Model):
    carid=models.CharField(max_length=20,help_text="CAR ID")
    carname=models.CharField(max_length=100)
    price=models.IntegerField()
    model=models.CharField()

class caradmin(admin.ModelAdmin):
    list_display=('carid','carname','price','model')


```
## ENTITY RELATIONSHIP DIAGRAM
<img width="1076" height="583" alt="er exp 2" src="https://github.com/user-attachments/assets/d39c9b7a-5784-44e7-a6f3-1d040fc8e6ea" />



## OUTPUT
<img width="1920" height="1140" alt="exp2 ss1" src="https://github.com/user-attachments/assets/6c2746ba-92c6-4273-8c98-f056bd22dddc" />
<img width="1920" height="1200" alt="exp2 ss" src="https://github.com/user-attachments/assets/b575b7c2-e5db-4e4d-b6e6-5eedbbb57cf7" />

## RESULT
Thus the program for creating a database using ORM hass been executed successfully


from email import message
from turtle import up, update
from venv import create
from django.db import models

# Create your models here.

class Informationn(models.Model):
    username = models.CharField(max_length=255)
    messagee = models.CharField(max_length=255)

    
    
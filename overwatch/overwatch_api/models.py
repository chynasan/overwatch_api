from django.db import models

# Create your models here.

class Hero(models.Model):
    Name = models.CharField(max_length=30)
    Role = models.ForeignKey('Role', 
                             on_delete=models.DO_NOTHING,
                            )
    Description = models.CharField(max_length=500)
    Abilities = models.CharField(max_length=500)
    Health = models.IntegerField()
    Birthday = models.DateField()

class Role(models.Model):
    Name = models.CharField(max_length=10)
    PassiveAbility = models.CharField(max_length=250)

class Maps(models.Model):
    Name = models.CharField(max_length=25)
    Description = models.CharField(max_length=500)

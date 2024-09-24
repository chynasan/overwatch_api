from django.db import models


# Create your models here.

class Role(models.Model):
    Name = models.CharField(max_length=10, primary_key=True)
    PassiveAbility = models.CharField(max_length=250)

class Hero(models.Model):
    Name = models.CharField(max_length=30, primary_key=True)
    Role = models.ForeignKey(
        Role, 
        related_name="Role",
        on_delete=models.DO_NOTHING,
    )
    Description = models.CharField(max_length=500)
    Abilities = models.CharField(max_length=500)
    Health = models.IntegerField()
    Birthday = models.DateField()

#TODO: Update this to include a field that has preset selectable options for hybrid, control, etc as a type field
#list for map choices
MAP_MODES =[('clash', ('Clash')),
            ('control', ('Control')),
            ('escort', ('Escort')),
            ('flashpoint', ('Flashpoint')),
            ('hybrid', ('Hybrid')),
            ('push', ('Push'))
        ]

class Maps(models.Model):
    Name = models.CharField(max_length=25)
    Description = models.CharField(max_length=500)
    Mode = models.CharField(
        max_length=32,
        choices=MAP_MODES,
        blank=False,
        default=None
    )
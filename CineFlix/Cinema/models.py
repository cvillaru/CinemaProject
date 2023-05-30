from django.db import models

class Film(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    age_rating = models.CharField(max_length=5,default="...")
    duration = models.DecimalField(default=0,max_digits=5, decimal_places=2)
    is_active = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return f"{self.title}"
    

class Screen(models.Model):
    screen_number = models.PositiveIntegerField(default=0)
    capacity = models.SmallIntegerField(default=0)
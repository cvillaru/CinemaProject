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
    
class Showing(models.Models):
    screen = models.ForeignKey(Screen, on_delete=models.PROTECT,related_name="showing")
    film = models.ForeignKey(Film, on_delete=models.PROTECT, related_name="showing")
    showing_date = models.DateField(auto_now_add=False, null=True)
    showing_time = models.TimeField(auto_now_add=False)
    tickets_sold = models.SmallIntegerField(default=0)
    
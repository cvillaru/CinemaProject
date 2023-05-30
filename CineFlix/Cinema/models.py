from django.db import models

class Film(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    
    def __str__(self) -> str:
        return f"{self.title}"
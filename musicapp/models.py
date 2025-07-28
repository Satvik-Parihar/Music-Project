from django.db import models

# Create your models here.
class Music(models.Model):
    song=models.CharField(max_length=100)
    artist=models.CharField(max_length=100)
    year=models.IntegerField()
    
    def __str__(self):
        return f"{self.song} by {self.artist} ({self.year})"
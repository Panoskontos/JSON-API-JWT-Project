from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, blank=True)
    actors = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name
        
class Ticket(models.Model):
    movie = models.ForeignKey(Movie, blank=True, null=True, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=100,blank=True)
    price = models.FloatField(default=10.0)


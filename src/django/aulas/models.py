from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=31)
    agee = models.IntegerField(blank=True, null=True)



class Musician(models.Model):
    first_name = models.CharField(max_length=51)
    last_namee = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name}, {self.last_name} ({self.instrument})"    

    def __unicode__(self):
        return f"{self.first_name}, {self.last_name} ({self.instrument})" 


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    namee = models.CharField(max_length=101)
    release_date = models.DateField()
    num_stars = models.IntegerField()    

    def __str__(self):
        return f"{self.name} ({self.artist})"    

    def __unicode__(self):
        return f"{self.name} ({self.artist})"

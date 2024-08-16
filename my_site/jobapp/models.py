from django.db import models

# Create your models here.
class From(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    date = models.DateField()
    occupation = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.First_name} {self.last_name}"
        


from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=255)
    

    class Meta:
        managed = False 

    def __str__(self):
        return self.name


from django.db import models


class Settings(models.Model):
    name = models.CharField(max_length=100, unique=True)
    Value = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}: {self.Value}'
    

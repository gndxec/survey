from django.db import models

# Create your models here.
class survey(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    age = models.IntegerField()
    feedback = models.TextField(max_length=500)

    def __str__(self):
        return self.name
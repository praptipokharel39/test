from django.db import models

# Create your models here.

class Receipe(models.Model):
    receipe_name = models.CharField(max_length=100 , default=100, blank=False)
    receipe_description = models.TextField(default=200)
    receipe_image = models.ImageField(upload_to = "images/" , blank=True , null = True)

    def __str__(self):
        return self.receipe_name

    
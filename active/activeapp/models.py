from django.db import models

# Create your models here.
class Navbar(models.Model):
    Name=models.CharField(max_length=20)

    def __str__(self):
        return self.Name

class Sliders(models.Model):
    title=models.CharField(max_length=50)
    image=models.ImageField(upload_to='sliders/')
    description=models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class Homedata(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
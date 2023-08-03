from django.db import models

# Create your models here.
class CheckModel(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(null=True)
    modified = models.DateField(auto_now_add=True)
    img = models.ImageField(upload_to='images/')
    
    
    def __str__(self):
        return self.name
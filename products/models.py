from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=50)
    Image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=500)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a particular book instance."""
        return reverse('product-detail', args=[str(self.id)])
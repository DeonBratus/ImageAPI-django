from django.db import models


class Image(models.Model):
    name = models.CharField(max_length=255)
    image_path = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    resolution = models.CharField(max_length=50, blank=True)
    size = models.PositiveIntegerField(null=True, blank=True)


    def __str__(self):
        return self.name
    
    
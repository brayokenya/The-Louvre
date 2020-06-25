from django.db import models
from pyuploadcare.dj.models import ImageField
# Create your models here.
class Paparazzo(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name
    class Meta:
        ordering = ['first_name']


class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Location(models.Model):
    loc = models.CharField(max_length =30)

    def __str__(self):
        return self.name


class Pic(models.Model):
    name = models.CharField(max_length =60)
    pic = ImageField(blank=True, null=True, manual_crop='1920x1080')  # ImageField does not require any arguments but you can place them.
    editor = models.ForeignKey(Location, on_delete=models.CASCADE)
    tag = models.ManyToManyField(tag)
    pub_date = models.DateTimeField(auto_now_add=True)
    article_image = models.ImageField(upload_to = 'articles/')
 
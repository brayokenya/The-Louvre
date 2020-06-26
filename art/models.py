from django.db import models
import datetime as dt

# Create your models here.
class Paparazzo(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)


    def __str__(self):
        return self.first_name

    def save_paparazzo(self):
        self.save()


    class Meta:
        ordering = ['first_name']
   


class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Location(models.Model):
    loc = models.CharField(max_length =30)

    def __str__(self):
        return self.loc

class Category(models.Model):
    cat = models.CharField(max_length = 30)
    def __str__(self):
        return self.cat


class Pic(models.Model):
    photo = models.ImageField(upload_to = 'pictures/')
    caption = models.CharField(max_length =60)
    paparazzo = models.ForeignKey(Paparazzo, on_delete=models.CASCADE)
    tags = models.ManyToManyField(tags)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption

    @classmethod
    def todays_art(cls):
        today = dt.date.today()
        art = cls.objects.filter(pub_date__date = today)
        return art

    @classmethod
    def days_art(cls,date):
        art = cls.objects.filter(pub_date__date = date)
        return art
    
    @classmethod
    def search_by_category(cls,search_term):
        art = cls.objects.filter(category__icontains=search_term)
        return art
 
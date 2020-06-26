from django.test import TestCase
from .models import Paparazzo,Location, Category,Pic, tags
import datetime as dt
# Create your tests here.
class PaparazzoTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.brayo= Paparazzo(first_name = 'Brayo', last_name ='Kiiru', email ='kiirubrian21@gmail.com')
        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.brayo,Paparazzo))

    # Testing Save Method
    def test_save_method(self):
        self.brayo.save_paparazzo()
        paparazzo = Paparazzo.objects.all()
        self.assertTrue(len(paparazzo) > 0)

class PicTestClass(TestCase):

    def setUp(self):
        # Creating a new paparazzo and saving it
        self.brian= Paparazzo(first_name = 'brian', last_name ='kiiru', email ='kiirubrian21@gmail.com')
        self.brian.save_paparazzo()

        # Creating a new tag and saving it
        self.new_tags = tags(name = 'testing')
        self.new_tags.save()

        self.new_photo= Pic(photo = 'pictures/6_1_of_1.jpg',caption = 'This is a random test Caption',paparazzo = self.brian)
        self.new_photo.save()

        self.new_photo.tag.add(self.new_tags)

    def test_get_news_today(self):
        today_art = Pic.todays_art()
        self.assertTrue(len(today_art)>0)

  

    def test_get_art_by_date(self):
        test_date = '2020-06-24'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        art_by_date = Pic.days_news(date)
        self.assertTrue(len(art_by_date) > 0)

    def tearDown(self):
        Paparazzo.objects.all().delete()
        tags.objects.all().delete()
        Pic.objects.all().delete()
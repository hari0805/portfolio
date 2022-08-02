from django.db import models
from django.core.validators import RegexValidator

summ_str = '''
            A small river named Duden flows by their place and 
            supplies it with the necessary regelialia. 
            It is a paradisematic country, in which roasted parts 
            of sentences fly into your mouth.
'''

class Aboutmodel(models.Model):
    Name = models.CharField(max_length=50, default = 'Revan')
    Bio1 = models.CharField(max_length=100, default='Data Scientist')
    Bio2 = models.CharField(max_length=100, default='Tableau Developer')
    Experiance = models.IntegerField(default = 2)
    Resume = models.FileField(upload_to='media', null = True)
    DOB = models.DateField(auto_now_add=True, blank=True)
    Address = models.CharField(max_length=100, default = 'Chennai')
    Pin_code = models.CharField(max_length=50, default = '639 120')
    Email = models.EmailField(max_length=50, default = 'sample@yourdomain.com')
    Phone_number = models.CharField(max_length=10, default = '9988776655')
    Profile_photo = models.ImageField(upload_to='media', default = 'default_profile.jpg')
    Home_bg1 = models.ImageField(upload_to='media', blank=True)
    Home_bg2 = models.ImageField(upload_to='media', blank=True)
    Summary = models.TextField(max_length=250, default=summ_str)

    aboutme = models.Manager()

    def __str__(self):
        return self.Name

# class Projectmodel(models.Model):
#     pass
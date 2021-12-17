from datetime import datetime

from django.db import models

"""
Creating XploreBot models 
"""


class Destinations(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/")
    about = models.TextField()
    link = models.URLField()

    def __str__(self):
        return self.name


class TourCompanies(models.Model):
    Cname = models.CharField(max_length=200)
    Cimage = models.ImageField(upload_to="images/")
    Services = models.TextField()
    location = models.TextField()
    website = models.URLField()
    email = models.EmailField(verbose_name='Email address', max_length=255, unique=True, )

    def __str__(self):
        return self.Cname


class CarHire(models.Model):
    type = models.CharField(max_length=100)
    carimage = models.ImageField(upload_to="images/")
    carlocation = models.CharField(max_length=120)
    price = models.DecimalField(decimal_places=2, max_digits=9)
    contact = models.IntegerField()

    def __str__(self):
        return self.type


class Hotels(models.Model):
    rates = models.FileField(upload_to='uploads/%Y/%m/%d/')
    Hname = models.CharField(max_length=130)
    location = models.CharField(max_length=140)
    Image = models.ImageField(upload_to="images/")
    website = models.URLField()
    Services = models.TextField()
    email = models.EmailField(verbose_name='Email address', max_length=255, unique=True, )

    def __str__(self):
        return self.Hname


class Tourguides(models.Model):
    Tname = models.CharField(max_length=120)
    profileimage = models.ImageField(upload_to="images/")
    phonenumber = models.IntegerField()
    Bio = models.TextField()
    link = models.URLField()

    def __str__(self):
        return self.Tname


class Tweets(models.Model):
    body = models.TextField()
    tweetedby = models.CharField(max_length=100)
    thumbnail = models.FileField(upload_to="uploads/%Y/%m/%d/")
    tweetedOn = models.DateTimeField(default=datetime.now)
    runyatweet = models.TextField()
    lugatweet = models.TextField()
    threadurl = models.URLField()

    def __str__(self):
        return self.body


class Facts(models.Model):
    Fbody = models.TextField()
    Image = models.FileField(upload_to="uploads/%Y/%m/%d/")

    def __str__(self):
        return self.Fbody


class Trips(models.Model):
    type_choices = [
        ('BDT', 'Budget'),
        ('MRE', 'Mid-Range'),
        ('LUX', 'Luxury'),
    ]
    accomodation_type = [
        ('Camping', 'Camping'),
        ('Hotel', 'Hotel'),
        ('Hostel', 'Hostel'),
    ]
    poster = models.ImageField(upload_to="images/")
    Date = models.DateField()
    desc = models.CharField(max_length=200)
    Inclusions = models.TextField()
    Exclusions = models.TextField()
    duration = models.CharField(max_length=150, help_text="Specify trip duration in form  of 3days/2nights")
    price = models.DecimalField(decimal_places=1, max_digits=10)
    Triptype = models.CharField(max_length=8, choices=type_choices)
    accmtype = models.CharField(max_length=10, choices=accomodation_type)
    paymentmthd = models.TextField(help_text="Describe the mode of payment, "
                                             "if mobile money,send in the mobile money details ")

    def __str__(self):
        return self.desc


class updates(models.Model):
    image = models.ImageField(upload_to="images/")
    body = models.TextField()
    link = models.URLField()
    runya = models.TextField()
    luga = models.TextField()
    Date = models.DateField()
    postedby= models.TextField()

    def __str__(self):
        return self.body

class Activities(models.Model):
    name = models.TextField()
    about= models.TextField()
    image = models.ImageField(upload_to="images/")
    sight = models.TextField()

    def __str__(self):
        return self.name


class Animals(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField(help_text="Describe it's way of life,gestation period,lifespan,habitat and it's food")
    image = models.ImageField(upload_to="images/")
    sightloc = models.TextField(help_text="Where can this be sighted in Uganda?")

    def __str__(self):
        return self.name

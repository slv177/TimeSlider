from django.contrib.gis.db import models
from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator
from shapely.geometry import LineString as ShLineString

class Shop(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    year = models.IntegerField(default=50)

    class Meta:
        ordering = ['name']


class Person(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    class Meta:
        ordering = ['surname']

    def __str__(self):
        return self.surname


class Link(models.Model):
    name = models.CharField(max_length=100)

    description = models.CharField(max_length=100)
    year = models.PositiveIntegerField(
            validators=[
                MinValueValidator(1900),
                MaxValueValidator(datetime.now().year)],
            help_text="Use the following format: <YYYY>")

    persons = models.ManyToManyField(Person)



    class Meta:
        ordering = ['name']

    pointA = models.ForeignKey(Shop, related_name="pointAA", on_delete=models.PROTECT)
    pointB = models.ForeignKey(Shop, related_name="pointBB", on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    def __init__(self, pointA, pointB):
        self.locations = models.LineStringField(pointA, pointB)


class Link2(models.Model):
    name = models.CharField(max_length=100)


    description = models.CharField(max_length=100)
    year = models.PositiveIntegerField(
            validators=[
                MinValueValidator(1900),
                MaxValueValidator(datetime.now().year)],
            help_text="Use the following format: <YYYY>")

    persons = models.ManyToManyField(Person)

    pointA = models.ForeignKey(Shop, related_name="pointA", on_delete=models.PROTECT)
    pointB = models.ForeignKey(Shop, related_name="pointB", on_delete=models.PROTECT)

    class Meta:
        ordering = ['name']


    def __str__(self):
        return self.name


class Link5(models.Model):
    name = models.CharField(max_length=100)
    pointA = models.ForeignKey(Shop, related_name="point1", on_delete=models.PROTECT)
    pointB = models.ForeignKey(Shop, related_name="point2", on_delete=models.PROTECT)

    def get_location_A(self):
        return self.pointB

    def get_location_B(self):
        return self.pointB

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Friend(models.Model):
    # NICK NAME should be unique
    nick_name = models.CharField(max_length=100, unique =  True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    likes = models.CharField(max_length = 250)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    lives_in = models.CharField(max_length=150, null = True, blank = True)

    def __str__(self):
        return self.nick_name


class Contact(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name



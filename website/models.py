import datetime

from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Trainer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    qualification = models.CharField(max_length=500, blank=True)
    profile = models.TextField(max_length=1000)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, blank=True, related_name="trainers")

    def __str__(self):
        return f"Trainer: {self.first_name} {self.last_name}"


class Course(models.Model):
    title = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, blank=True, related_name="courses")
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, blank=True, related_name="courses")
    course_date = models.DateField(datetime.date, blank=True)
    duration = models.DurationField(max_length=2,  blank=True)
    overview = models.TextField(max_length=1000, blank=True)
    trainers = models.ManyToManyField(Trainer, related_name="courses")

    class Meta:
        ordering = ["-course_date"]

    def __str__(self):
        return self.title

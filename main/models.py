from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=200)
    title_ky = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200)
    desc = models.TextField()
    desc_ky = models.TextField()
    desc_en = models.TextField()
    img = models.ImageField(upload_to='static/img', blank=True, null=True)


class Application(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    email = models.EmailField(blank=True, null=True)


class Feedback(models.Model):
    field_name = models.URLField(max_length=250)

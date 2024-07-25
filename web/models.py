from django.db import models

class Flan(models.Model):
    id = models.IntegerField(primary_key=True)
    #id = models.AutoField(primary_key=True, default=1)
    #flan_uuid = models.UUIDField()
    name = models.CharField (max_length= 64)
    description = models.TextField()
    receta = models.TextField(max_length=20000, default='')
    image_url = models.URLField()
    slug = models.SlugField()
    is_private = models.BooleanField()

class Contact(models.Model):
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()
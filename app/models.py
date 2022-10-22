from django.db import models

class Image(models.Model):
    image = models.ImageField("Image Field", upload_to='images/', height_field=None, width_field=None, max_length=None)
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        default='default.jpg', upload_to='profile_pics')

    # now we want to display more descriptively, otherwise will print as 'object'
    def __str__(self):
        return f'{self.user.username} Profile'

    # to override the default save method to reduce size of image if large, which speeds up website
    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 and img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

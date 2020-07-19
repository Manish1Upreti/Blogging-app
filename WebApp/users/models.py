from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    # if you delete the user your profile is delete , one user has one profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # for user profile picture
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        # To display username Profile
        return f'{self.user.username} Profile'

    # to reduce the size of image
    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)



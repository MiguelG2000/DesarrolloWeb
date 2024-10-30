
import os
from logging import raiseExceptions

from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="users_product",
        blank=True,
        null=True,
    )
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=4, default=0.00)
    is_active = models.BooleanField(default=1)
    image = models.ImageField(
        upload_to="images_product/",
        blank=True,
        null=True
    )
    thumbnail = models.ImageField(
        upload_to="thumbs",
        blank=True,
        null=True,
        editable=False
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.make_thumbnail():
            raise Exception("No se pudo crear la miniatura")

        super(Product, self).save(*args, **kwargs)


    def make_thumbnail(self):
        image = Image.open(self.image)
        thumbnail_size = 75, 75
        image.thumbnail(thumbnail_size)

        thumb_name, thumb_extension = os.path.splitext(self.image.name)
        thumb_extension = thumb_extension.lower()

        thumb_filename = thumb_name + '_thumb' + thumb_extension

        if thumb_extension in ['.jpg', '.jpeg']:
            FTYPE = 'JPEG'
        elif thumb_extension == '.gif':
            FTYPE = 'GIF'
        elif thumb_extension == '.png':
            FTYPE = 'PNG'
        else:
            return False  # Unrecognized file type

        # Save thumbnail to in-memory file as StringIO
        temp_thumb = BytesIO()
        image.save(temp_thumb, FTYPE)
        temp_thumb.seek(0)

        # set save=False, otherwise it will run in an infinite loop
        self.thumbnail.save(thumb_filename, ContentFile(temp_thumb.read()), save=False)
        temp_thumb.close()
        
        return True

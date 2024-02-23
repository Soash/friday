from django.db import models
from django.conf import settings
from .utils import upload_image_to_imgbb

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, default='')
    cateImage = models.ImageField(upload_to='cateImg/', blank=True, null=True)
    imgbb_url = models.URLField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.cateImage:  # Only proceed if an image is provided
            super().save(*args, **kwargs)  # Save the model instance first to generate the ID
            imgbb_url = upload_image_to_imgbb(self.cateImage.path, settings.IMGBB_API_KEY)
            if imgbb_url:
                self.imgbb_url = imgbb_url
                super().save(*args, **kwargs)  # Save the model instance again to update imgbb_url
        else:
            super().save(*args, **kwargs)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"Product : {self.name}"


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_img/', blank=True, null=True)
    imgbb_url = models.URLField(blank=True, null=True)
    def save(self, *args, **kwargs):
        if self.image:  # Only proceed if an image is provided
            super().save(*args, **kwargs)  # Save the model instance first to generate the ID
            imgbb_url = upload_image_to_imgbb(self.image.path, settings.IMGBB_API_KEY)
            if imgbb_url:
                self.imgbb_url = imgbb_url
                super().save(*args, **kwargs)  # Save the model instance again to update imgbb_url
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return f"Image : {self.product.name}"



class Banner(models.Model):
    banner = models.ImageField(upload_to='banner_img/', blank=True, null=True)
    imgbb_url = models.URLField(blank=True, null=True)
    def save(self, *args, **kwargs):
        if self.banner:  # Only proceed if an image is provided
            super().save(*args, **kwargs)  # Save the model instance first to generate the ID
            imgbb_url = upload_image_to_imgbb(self.banner.path, settings.IMGBB_API_KEY)
            if imgbb_url:
                self.imgbb_url = imgbb_url
                super().save(*args, **kwargs)  # Save the model instance again to update imgbb_url
        else:
            super().save(*args, **kwargs)
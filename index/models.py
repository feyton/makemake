from django.db import models
from cloudinary.models import CloudinaryField
from django.urls import reverse

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255)
    summary = models.TextField(blank=True, null=True)
    published_date = models.DateField(auto_now_add=False, blank=True, null=True)
    image = CloudinaryField("image", blank=False, null=True)
    published = models.BooleanField(default=True)
    price = models.IntegerField()

    @property
    def imgURL(self):
        try:
            url = self.image.url
        except:
            url = ""
        return url

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product-detail", kwargs={"pk": self.pk})

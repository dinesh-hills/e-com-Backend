from django.db import models
from store.models import Product

# Create your models here.
class Tag(models.Model):
    label = models.CharField(max_length=255)

class TaggedItems(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
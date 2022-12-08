from django.db import models
from django.urls import reverse

class Category(models.Model):
    category_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100,unique=True)
    description = models.TextField(max_length=256,blank=True)
    cat_image = models.ImageField(upload_to='photos/categories/',blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = "categories"

    def get_url(self):
        return reverse('Product_by_category',args=[self.slug])


    def __str__(self):
        return self.category_name
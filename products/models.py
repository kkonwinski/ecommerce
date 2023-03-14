from django.db import models
from base.models import BaseModel


class Category(BaseModel):
    """
    Model for product categories.
    """
    category_name = models.CharField(max_length=100, verbose_name="Category Name")
    category_image = models.ImageField(upload_to="categories", verbose_name="Category Image")
    slug = models.SlugField(unique=True, null=True, blank=True)


class Product(BaseModel):
    """
    Model for products.
    """
    product_name = models.CharField(max_length=100, verbose_name="Product Name")
    slug = models.SlugField(unique=True, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products',
                                 related_query_name='product', verbose_name="Category")
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Price")
    product_description = models.TextField(verbose_name="Product Description")


class ProductImage(BaseModel):
    """
    Model for product images.
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_images",
                                related_query_name='product_image', verbose_name="Product")
    image = models.ImageField(upload_to='product', verbose_name="Image")

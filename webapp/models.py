from django.db import models

# Create your models here.
class Product(models.Model):
    Id = models.BigAutoField(primary_key=True)
    Product_Name = models.CharField(max_length=200)
    Category = models.CharField(max_length=30, default="")
    Color = models.CharField(max_length=50)
    Full_Description = models.TextField(default="")
    Price = models.FloatField()
    Product_Image = models.ImageField(upload_to='Product_Images/', default="NoImage")

    def __str__(self):
        return f'{self.Product_Name}'
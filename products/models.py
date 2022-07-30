from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

class BannerImage(models.Model):
    image = ProcessedImageField(null=True, upload_to="banner/", 
                                           processors=[ResizeToFill(1500, 800)],
                                           format='JPEG')
    class Meta:
        verbose_name = "Изображение баннера"
        verbose_name_plural = "Изображения баннеров"
class Size(models.Model):
    size = models.CharField(max_length=4, default='S')
    class Meta:
        verbose_name = "размер"

    
class Category(models.Model):
    category_name=models.CharField(max_length=255, verbose_name = "название")
    slug = models.SlugField(max_length=255, unique=True, null=True)


    def __str__(self):
        return self.category_name
    def get_absolute_url(self):
        return reverse('products:product_list_by_category',args=[self.slug])

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"



YEARS=[('2017', '2017'), 
('2018', '2018'),
('2019', '2019'),
 ('2020', '2020'), 
 ('2021', '2021'),
  ('2022', '2022'), 
  ('2023', '2023'), 
  ('2024', '2024'),
   ('2025', '2025')]



class Product(models.Model):
    name= models.CharField(max_length=255, verbose_name = "название")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True,null=True)
    description = models.CharField(max_length=255, verbose_name = "описание")
    pub_date = models.DateField(default=timezone.now, verbose_name = "дата публикации")
    year=models.CharField(max_length=256, choices=YEARS, default='2022',  verbose_name = "коллекция")
    image = models.ImageField(upload_to='products/%Y/%m/%d',blank=True)    
    image2=models.ImageField(null=True, upload_to='products/%Y/%m/%d')
    image3=models.ImageField(null=True, upload_to='products/%Y/%m/%d')
    size=models.ManyToManyField(Size)
    #material
    length=models.CharField(max_length=256, choices=[('длинная', 'длинная'), ('короткая', 'короткая'),('средний', 'средний')], default='длинная',  verbose_name = "длина")
    length_hand=models.CharField(max_length=256, choices=[('длинная', 'длинная'), ('короткая', 'короткая'),('средний', 'средний'),('нет', 'нет')], default='короткая',  verbose_name = "длина рукава")
    #brand
    
    #fason
    image_thumbnail = ProcessedImageField(null=True, upload_to="products/%Y/%m/%d", 
                                           processors=[ResizeToFill(660, 1000)],
                                           format='JPEG')

   
 


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:product_detail',   args=[self.id, self.slug])
    class Meta:
        verbose_name_plural = "Одежда"
        ordering=("-pub_date",)

class ProductImage(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')
 
    def __str__(self):
        return self.product.name


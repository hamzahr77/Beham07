from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime
# Create your models here.
class Allproduct(models.Model):
    model_type = models.CharField(max_length=90)
    name = models.CharField(max_length=150)
    stars = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    price = models.DecimalField( max_digits=6 , decimal_places=2 )
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_active = models.BooleanField( default= True )
    publish_date = models.DateTimeField(default=datetime.now)
    
    def __str__(self):
        return self.name

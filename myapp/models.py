from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Products(models.Model):
    def __str__(self):
        return self.name

    seller_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    desc = models.CharField(max_length= 200)
    image = models.ImageField(blank=True, upload_to='images')

# The process of translating this Django model in to database table is known as migration
#  The problem is that when we are performing migration, we are performing inthe main file(mysite) folder
# To solve the issue we have to go to settings file in mysite and installed apps and write "myapp',
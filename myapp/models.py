from django.db import models

# Create your models here.
class Products(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    desc = models.CharField(max_length= 200)

# The process of translating this Django model in to database table is known as migration
#  The problem is that when we are performing migration, we are performing inthe main file(mysite) folder
# To solve the issue we have to go to settings file in mysite and installed apps and write "myapp',
from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100,verbose_name='kitob nomi')
    author = models.CharField(max_length=50,verbose_name='muallifi')
    year = models.DateTimeField(verbose_name='chop etilgan sanasi',blank=True,null=True)
    pages = models.IntegerField(verbose_name='sahifalar soni')
    image = models.ImageField(upload_to='images/',verbose_name='kitob rasmi')
    
    def __str__(self):
        return self.name
    
    
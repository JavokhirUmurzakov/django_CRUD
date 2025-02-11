from django.contrib import admin
from .models import Book
# Register your models here.

class AdminBook(admin.ModelAdmin):
    list_display = ['name','author','year','pages','image']
    
admin.site.register(Book,AdminBook)
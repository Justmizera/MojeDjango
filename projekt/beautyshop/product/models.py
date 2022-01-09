from django.db import models
from django.forms import ModelForm  
from django.conf import settings

# Create your models here.

class Category(models.Model): #moja klasa dziedziczy z domyślej klasy models
        title = models.CharField(max_length=255) #maksymalna długość 255


        def __str__(self):
            return self.title # w bazie wyświetla się title na liście z produktami



class Product(models.Model): #moja klasa dziedziczy z domyślej klasy models
        category = models.ForeignKey(Category,  blank=True, null=True, on_delete=models.CASCADE) #klucz obcy do kategorii
        title = models.CharField(max_length=255) #maksymalna długość 255
        description = models.TextField(blank=True, null=True) #może być pusty
        price = models.DecimalField(max_digits=6, decimal_places=2) # 2 miejsce po przecinku
        date_added = models.DateTimeField(auto_now_add=True) #dodaje się auktomatycznie
        image = models.ImageField(upload_to='static/img/uploads', blank=True, null=True)


        def __str__(self):
            return self.title # w bazie wyświetla się title na liście z produktami

class Cart(models.Model): #moja klasa dziedziczy z domyślej klasy models
        product_id = models.ForeignKey(Product,  blank=True, null=True, on_delete=models.CASCADE,related_name='product') #klucz obcy do produktów
        user_id = models.ForeignKey(settings.AUTH_USER_MODEL,  blank=True, null=True, on_delete=models.CASCADE) #klucz obcy do użytkowników



class Order(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    paid_amount = models.DecimalField(max_digits=8, decimal_places=2) 
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL,  blank=True, null=True, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False, blank=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product,  blank=True, null=True, on_delete=models.CASCADE)


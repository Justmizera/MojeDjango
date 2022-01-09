from django.contrib import admin
from .models import Product #importuję z models product, któy stworzyłam bo znajduje isę on gdzie indziej
from .models import Category
from .models import Cart
from .models import OrderItem
from .models import Order

# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(OrderItem)
admin.site.register(Order)
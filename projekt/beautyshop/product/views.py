from django.shortcuts import render
from .models import Product
from .models import Cart
from .models import OrderItem
from .models import Order
from django.contrib.auth.models import User
from .forms import ProductForm
from django.contrib import messages
from django.shortcuts import redirect
from .forms import Add_to_cartForm
from .forms import OrderForm
from .forms import OrderItemForm
from django.db.models import Sum
from decimal import Decimal

# Create your views here.

def index(request):
    obj = Product.objects.all()
    kontekst = {
        'obiekt' : obj  
    }
    return render(request, "index.html", kontekst)

#szczegóły produktu i dodawanie do koszyka

def productDetail(request,id):
    obj = Product.objects.get(id=id)
    form = Add_to_cartForm(request.POST or None, initial={'product_id': obj.id, 'user_id': request.user})
    if form.is_valid():
        form.save(commit=True)
        form = Add_to_cartForm()
        messages.success(request, ("Poprawnie dodano produkt do koszyka"))
        return redirect('/')

    kontekst = {
        'obiekt' : obj,
        'form' : form  
    }
    return render(request, "productDetail.html", kontekst)


def vendor(request):
    obj = Product.objects.all()
    ord = Order.objects.all()
    orditem = OrderItem.objects.all()
    kontekst = {
        'obiekt' : obj, 
        'order' : ord,
        'orderitem' : orditem
    }
    return render(request, "vendor_site.html", kontekst)

# dodawanie produktu do bazy danych

def add_product(request):
    form = ProductForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save(commit=True)
        form = ProductForm()

    kontekst = {
        'form' : form  
    }
    return render(request, "add.html", kontekst)

# edytowanie produktu w bazie

def edit_product(request, id):
    obj = Product.objects.get(id=id)
    form = ProductForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect('/strona_sprzedawcy/')
    kontekst = {
        'form' : form  
    }
    return render(request, "edit.html", kontekst)

# usuwanie produktu z bazy danych

def delete_product(request, id): 
    obj = Product.objects.get(id=id)
    obj.delete()
    messages.success(request, ("Usunięto produkt z bazy"))
    return redirect('/strona_sprzedawcy/')

#koszyk zalogowanego użytkownika

def user_cart(request): 
    obj = Cart.objects.filter(user_id=request.user)
    products = Product.objects.all()
    kontekst = {
        'obiekt' : obj,
        'produkt' : products
    }
    return render(request, 'cart.html', kontekst)

#usuwanie z koszyka

def delete_fromcart(request, id): 
    obj = Cart.objects.get(id=id)
    obj.delete()
    messages.success(request, ("Usunięto produkt z koszyka"))
    return redirect('/koszyk/')


#dodaj zamówienie

def order(request):
    products = Product.objects.all()
    obj = Cart.objects.filter(user_id=request.user)
    suma = Cart.objects.filter(user_id=request.user).aggregate(TotalSum=Sum('product_id__price')).get('TotalSum', 0.00)
    suma=float(suma)
    form = OrderForm(request.POST or None, initial={'paid_amount': suma, 'user_id': request.user})
    if form.is_valid():
        currentorder = form.save(commit=True)
        form = OrderForm()
        for items in obj:
            products = Product.objects.filter(id = items.product_id.id)
            for prod in products:
                OrderItem.objects.create(product_id = prod, order=currentorder)

        obj.delete()
        messages.success(request, ("Zamówienie złożone poprawnie"))
        return redirect('/')

    kontekst = {
        'obiekt' : obj,
        'form' : form,  
        'suma' : suma
    }
    return render(request, "order.html", kontekst)

# edytowanie zamówienia w bazie

def edit_order(request, id):
    Order.objects.filter(id = id).update(paid = True)
    return redirect('/strona_sprzedawcy/')
    


    

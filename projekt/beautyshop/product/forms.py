from .models import Product
from django import forms
from .models import Cart
from .models import Order
from .models import OrderItem


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'image', 'title', 'description', 'price']

    def __init__(self, *args, **kwargs): #dzięi temu pola w domyślnym formularzu mają zmieniony wygląd
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['category'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['price'].widget.attrs['class'] = 'form-control'


class Add_to_cartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['user_id', 'product_id']
        widgets = {'user_id': forms.HiddenInput(), 'product_id': forms.HiddenInput()
        }



class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ( 'first_name', 'last_name', 'email', 'address', 'zipcode', 'place','phone','paid_amount','user_id')
        widgets = {'user_id': forms.HiddenInput(), 'paid': forms.HiddenInput(),'paid_amount': forms.HiddenInput()
        }

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ( 'order', 'product_id')
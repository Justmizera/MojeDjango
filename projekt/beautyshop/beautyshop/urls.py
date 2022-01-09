"""beautyshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


#tu definiuję widoki 
from django.contrib import admin
from django.urls import path
from django.urls import include
from pages.views import home_view
from django.conf.urls.static import static
from django.conf import settings
from product.views import index
from product.views import productDetail
from product.views import vendor
from product.views import add_product
from product.views import edit_product
from product.views import delete_product
from product.views import user_cart
from product.views import delete_fromcart
from product.views import order
from product.views import edit_order


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('szczegoly_produktu/<int:id>', productDetail , name='productDetail'),
    path('strona_sprzedawcy/', vendor , name='vendor_site'),
    path('dodaj/', add_product , name='add_site'),
    path('edytuj/<int:id>', edit_product , name='edit_site'),
    path('edytuj_zamowienie/<int:id>', edit_order , name='edit_order'),
    path('usun/<int:id>', delete_product , name='delete_site'),
    path('members/', include('django.contrib.auth.urls')), # umożliwia używanie ścieżek z systemu autentykacji
    path('members/', include('members.urls')), # tu zaczytujemy urls z apki members
    path('koszyk/', user_cart , name='user_cart'),
    path('usunzkoszyka/<int:id>', delete_fromcart , name='delete_fromcart'),
    path('zamowienie/', order , name='order'),

    
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
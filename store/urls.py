from django.urls import path, re_path
from .views import index, signup, login_view, logout_view, Cart, checkOut, OrderView, products , cartPage, update_cart, cartPage, about, support, contact, fabric, process, customization, delete_cart
from . import views
from store.views import OrderView
urlpatterns = [
    path('', index.as_view(), name='index'),
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('cart/', views.Cart, name='cart'),
    path('checkOut/', checkOut.as_view(), name='checkOut'),
    re_path(r'^checkOut$', checkOut.as_view(), name='checkOut'),
    path('order/', OrderView.as_view(), name='order'),
    path('products/', views.products, name='products'),
    # path('cartPage/', views.cartPage, name='cartPage'),
    path('cartPage/<int:product_id>/', views.cartPage, name='cartPage'),
    path('update_cart/', update_cart, name='update_cart'),
    path('cart/<int:product_id>/', cartPage, name='cart_page'),
    path('about/', about, name='about'),
    path('fabric/', fabric, name='fabric'),
    path('process/', process, name='process'),
    path('contact/', contact, name='contact'),
    path('support/', support, name='support'),
    path('customization/', customization, name='customization'),
    path('delete-cart/', delete_cart, name='delete_cart'),
]


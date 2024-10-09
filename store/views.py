from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.hashers import check_password
from django.views import View
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from django.contrib.auth import logout
from store.models.product import Product
from store.models.orders import Order
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseBadRequest
from django.conf.urls import handler404
from .models.contact import Contact



class index(View):
    def post(self, request):
        product_id = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart', {})

        if product_id:
            quantity = cart.get(product_id, 0)

            if remove:
                if quantity <= 1:
                    cart.pop(product_id)
                else:
                    cart[product_id] = quantity - 1
            else:
                cart[product_id] = quantity + 1

            if cart.get(product_id) == 0:
                cart.pop(product_id)

        request.session['cart'] = cart
        return redirect('index')

    def get(self, request):
        products = None
        categories = Category.get_all_category()
        parent_categories = categories.filter(parent__isnull=True)

        products = Product.objects.filter(category__in=parent_categories)

        customer = None
        if 'customer_id' in request.session:
            customer = Customer.objects.filter(id=request.session['customer_id']).first()

        cart = request.session.get('cart', {})

        data = {
            'Categories': parent_categories, 
            'products': products, 
            'Customer': customer,
            'cart': cart 
        }

        return render(request, 'index.html', data)



def signup(request):
    if request.method == 'POST':
        postData = request.POST
        first_name = postData.get('first_name')
        last_name = postData.get('last_name')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        re_password = postData.get('re_password')

        # Validate input
        if not all([first_name, last_name, phone, email, password, re_password]):
            return render(request, 'signup.html', {'All_Required': True})

        if password != re_password:
            return render(request, 'signup.html', {'password_mismatch': True})

        if Customer.objects.filter(email=email).exists() or Customer.objects.filter(phone=phone).exists():
            return render(request, 'signup.html', {'email_phone_match': True})

        # Create new customer
        customer = Customer(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            phone=phone
        )
        customer.save()
        request.session['customer_id'] = customer.id
        request.session['email'] = email

        return redirect('index')
    
    else:
        categories = Category.get_all_category()
        parent_categories = categories.filter(parent__isnull=True)  # Only parent categories

        data = {
            'Categories': parent_categories  # Pass parent categories to the template
        }

        return render(request, 'signup.html', data)


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        return_url = request.POST.get('return_url', '/')

        customer = Customer.get_customer_by_email(email)
        error_message = None

        if customer:
            if check_password(password, customer.password):
                request.session['customer_id'] = customer.id 
                request.session['email'] = email 
                return redirect(return_url)
            
            else:
                error_message = 'Wrong Email or Password'
                return render(request, 'login.html', {'error_message': True, 'return_url': return_url})  
        else:
            error_message = 'Wrong Email or Password'
            return render(request, 'login.html', {'error_message': True, 'return_url': return_url}) 

    else:
        categories = Category.get_all_category()
        parent_categories = categories.filter(parent__isnull=True)
        
        return_url = request.GET.get('return_url', '/')
        return render(request, 'login.html', {
            'Categories': parent_categories,
            'return_url': return_url
            })


def logout_view(request):
    logout(request)
    request.session.flush() 
    return redirect('login')

def Cart(request):
    cart = request.session.get('cart', {})
    ids = list(cart.keys())
    products = Product.get_Products_by_id(ids)
    categories = Category.get_all_category()
    parent_categories = categories.filter(parent__isnull=True)
    customer = None
    if 'customer_id' in request.session:
        customer = Customer.objects.filter(id=request.session['customer_id']).first()
    return render(request, 'cart.html', {'products': products, 'cart': cart, 'Customer': customer, 'Categories': parent_categories,})


class OrderView(View):
    def get(self, request):
        customer_id = request.session.get('customer_id')
        categories = Category.get_all_category()
        parent_categories = categories.filter(parent__isnull=True)
        if not customer_id:
            return redirect('login')
        customer = Customer.objects.get(id=customer_id)
        orders = Order.get_order_by_customer(customer)
        print(orders)

        return render(request, 'order.html', {'orders': orders, 'Customer': customer, 'Categories': parent_categories,})

class checkOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        detail = request.POST.get('detail')
        return_url = request.POST.get('return_url', 'cart')
        customer_id = request.session.get('customer_id')
        cart = request.session.get('cart', {})
        

        if not customer_id:
            return redirect(f'/login/?return_url={return_url}')
        product_ids = [int(id) for id in cart.keys()]
        products = Product.get_Products_by_id(product_ids)

        for product in products:
            order = Order(
                customer=Customer(id=customer_id),
                product=product,
                price=product.price,
                address=address,
                phone=phone,
                detail=detail,
                quantity=cart.get(str(product.id))
            )
            order.placeOrder()

        request.session['cart'] = {}
        return redirect(return_url)
    


def products(request):
    if request.method == "POST":
        product_id = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart', {})

        if product_id:
            quantity = cart.get(product_id, 0)

            if remove:
                if quantity <= 1:
                    cart.pop(product_id)
                else:
                    cart[product_id] = quantity - 1
            else:
                cart[product_id] = quantity + 1

            if cart.get(product_id) == 0:
                cart.pop(product_id)

        request.session['cart'] = cart
        return redirect('products')

    else:
        products = None
        categories = Category.get_all_category()
        category_id = request.GET.get('category')

        if category_id:
            selected_category = Category.objects.filter(id=category_id).first()
            if selected_category:
                child_categories = selected_category.get_children()
                all_categories = [selected_category] + list(child_categories)
                products = Product.objects.filter(category__in=all_categories)
        else:
            products = Product.get_all_products()

        customer = None
        if 'customer_id' in request.session:
            customer = Customer.objects.filter(id=request.session['customer_id']).first()

        cart = request.session.get('cart', {})

        parent_categories = categories.filter(parent__isnull=True)

        data = {
            'Categories': parent_categories,
            'products': products,
            'Customer': customer,
            'cart': cart
        }

        return render(request, 'Products.html', data)



def cartPage(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    materials = product.materials.all()
    sizes = product.sizes.all()
    customizations = product.customizations.all()
    types = product.types.all()
    colors = product.colors.all()
    gsms = product.gsms.all()
    
    cart = request.session.get('cart', {})
    categories = Category.get_all_category()
    parent_categories = categories.filter(parent__isnull=True)
    customer = None
    if 'customer_id' in request.session:
        customer = Customer.objects.filter(id=request.session['customer_id']).first()
    
    return render(request, 'product-details-page.html', {
        'product': product,
        'cart': cart,
        'Categories': parent_categories,
        'Customer': customer,
        'color':colors,
        'material':materials,
        'size':sizes,
        'customization':customizations,
        'type':types,
        'gsms':gsms
        
    })


def update_cart(request):
    if request.method == "POST":
        product_id = request.POST.get('product')
        remove = request.POST.get('remove')

        if not product_id:
            return HttpResponseBadRequest("Product ID is missing")

        cart = request.session.get('cart', {})

        if remove:
            if product_id in cart:
                del cart[product_id]
        else:
            if product_id in cart:
                cart[product_id] += 1

            else:
                cart[product_id] = 1

        request.session['cart'] = cart
        return redirect(request.META.get('HTTP_REFERER', '/'))
    else:
        return HttpResponseBadRequest("Invalid request method")
    

def about(request):
    categories = Category.get_all_category()
    category_id = request.GET.get('category')
    parent_categories = categories.filter(parent__isnull=True)
    products = None

    if category_id:
        products = Product.get_all_products_by_id(category_id)
    else:
        products = Product.get_all_products()

    customer = None
    if 'customer_id' in request.session:
        customer = Customer.objects.filter(id=request.session['customer_id']).first()

    cart = request.session.get('cart', {})

    context = {
        'Categories': parent_categories,
        'products': products,
        'Customer': customer,
        'cart': cart
    }

    return render(request, 'about.html', context)


def process(request):
    categories = Category.get_all_category()
    parent_categories = categories.filter(parent__isnull=True)
    category_id = request.GET.get('category')
    products = None

    if category_id:
        products = Product.get_all_products_by_id(category_id)
    else:
        products = Product.get_all_products()

    customer = None
    if 'customer_id' in request.session:
        customer = Customer.objects.filter(id=request.session['customer_id']).first()

    cart = request.session.get('cart', {})

    context = {
        'Categories': parent_categories,
        'products': products,
        'Customer': customer,
        'cart': cart
    }

    return render(request, 'process.html', context)


def fabric(request):
    categories = Category.get_all_category()
    parent_categories = categories.filter(parent__isnull=True)
    category_id = request.GET.get('category')
    products = None

    if category_id:
        products = Product.get_all_products_by_id(category_id)
    else:
        products = Product.get_all_products()

    customer = None
    if 'customer_id' in request.session:
        customer = Customer.objects.filter(id=request.session['customer_id']).first()

    cart = request.session.get('cart', {})

    context = {
        'Categories': parent_categories,
        'products': products,
        'Customer': customer,
        'cart': cart
    }

    return render(request, 'fabric.html', context)

def contact(request):
    if request.method=='POST':
        contact = Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
        return redirect('contact')
    
    categories = Category.get_all_category()
    parent_categories = categories.filter(parent__isnull=True)
    context = {
        'Categories': parent_categories,
        'products': products,
    }
    return render(request, 'contact.html', context)


def support(request):
    categories = Category.get_all_category()
    parent_categories = categories.filter(parent__isnull=True)
    category_id = request.GET.get('category')
    products = None

    if category_id:
        products = Product.get_all_products_by_id(category_id)
    else:
        products = Product.get_all_products()

    customer = None
    if 'customer_id' in request.session:
        customer = Customer.objects.filter(id=request.session['customer_id']).first()

    cart = request.session.get('cart', {})

    context = {
        'Categories': parent_categories,
        'products': products,
        'Customer': customer,
        'cart': cart
    }
    return render(request,'support.html',context )

def customization(request):
    categories = Category.get_all_category()
    parent_categories = categories.filter(parent__isnull=True)
    category_id = request.GET.get('category')
    products = None

    if category_id:
        products = Product.get_all_products_by_id(category_id)
    else:
        products = Product.get_all_products()

    customer = None
    if 'customer_id' in request.session:
        customer = Customer.objects.filter(id=request.session['customer_id']).first()

    cart = request.session.get('cart', {})

    context = {
        'Categories': parent_categories,
        'products': products,
        'Customer': customer,
        'cart': cart
    }

    return render(request, 'customization.html', context)



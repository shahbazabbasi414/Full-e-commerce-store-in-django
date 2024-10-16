from django import template

register = template.Library()  # Create an instance of the Library class

@register.filter(name='is_in_cart')
def is_in_cart(product, cart):
    # Extract the product ID from cart keys
    product_id = str(product.id)  # Convert product ID to string for comparison
    
    # Check if any cart key starts with the product ID
    for key in cart.keys():
        if key.startswith(product_id + '-'):
            return True
    return False
  
@register.filter(name='cart_quantity')
def cart_quantity(product, cart):
    try:
        # Ensure product.id is converted to a string and properly extracted from the cart key
        product_id = str(product.id)
        for key in cart.keys():
            if key.startswith(product_id):
                return cart[key]
        return 0
    except (ValueError, KeyError):
        return 0



@register.filter(name='price_total')
def price_total(product, cart):
    return product.price * cart_quantity(product, cart)

@register.filter(name='total_cart_price')
def total_cart_price(products, cart):
    total = 0
    for p in products:
        total += price_total(p, cart)
    return total
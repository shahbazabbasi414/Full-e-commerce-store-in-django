from django import template

register = template.Library()  # Create an instance of the Library class

@register.filter(name='is_in_cart')
def is_in_cart(product, cart):
    if not cart:
        return False
    for id in cart.keys():
        if int(id) == product.id:
            return True
    # print(product,cart)
    return False
  
@register.filter(name='cart_quantity')
def cart_quantity(product, cart):
    if not cart:
        return False
    for id in cart.keys():
        if int(id) == product.id:
            return cart.get(id)
    # print(product,cart)
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
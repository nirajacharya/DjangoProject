from django import template

register = template.Library()


@register.filter(name="is_in_cart")
def is_in_cart(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True

    return False

@register.filter(name="cart_quantity")
def cart_quantity(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)

    return 0

@register.filter(name="price_total")
def price_total(product, cart):
    price = product.price
    quantity = cart_quantity(product,cart)
    total_price = price * quantity
    return total_price

@register.filter(name="total_cart_price")
def total_cart_price(products, cart):
    sum = 0
    for product in products:
        sum = sum + price_total(product, cart)
    return sum

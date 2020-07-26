from django import template

register = template.Library()


@register.filter(name="currency")
def get_currency(number):
    currency_symbol = "‎रू"
    number = str(number)
    return currency_symbol + number


@register.filter(name="multiply")
def multiply(number1, number2):
    number1=int(number1)
    number2=int(number2)
    return number1 * number2

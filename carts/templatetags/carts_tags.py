from django import template

from carts.models import Cart

register = template.Library()

@register.simple_tag()
def user_carts(requset):
    if requset.user.is_authenticated:
        return Cart.objects.filter(user=requset.user)

    return Cart.objects.filter(user=requset.user)

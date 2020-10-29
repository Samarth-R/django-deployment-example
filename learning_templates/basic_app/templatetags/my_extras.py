from django import template

register = template.Library()

@register.filter(name='cut1')
def cut1(value,arg):
    """
    Cuts out all values of 'arg' from the string
    """
    return value.replace(arg,'')

# register.filter('cut1',cut1)

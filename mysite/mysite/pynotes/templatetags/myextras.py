from django import template

register = template.Library()

# truncate after a certain number of characters

@register.filter
def testtag(value):
    return value + '---test---'

def truncchar(value, arg):
    if len(value) < arg:
        return value
    else:
        return value[:arg] + '...'
    

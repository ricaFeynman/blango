from django.contrib.auth import get_user_model
user_model = get_user_model()

from django import template
register = template.Library()

from django.utils.html import format_html

@register.filter
def author_details(author, current_user=None):
    if not isinstance(author, user_model):
        return ""
    if author == current_user:
        return format_html('<strong>{}</strong>', 'me')
    
    if author.first_name and author.last_name:
        name = f"{author.first_name} {author.last_name}"
    else:
        name = author.username
    details = format_html('{}', name)

    if author.email:
        details = format_html('<a href="mailto:{}">{}</a>', author.email, details)
    
    return details

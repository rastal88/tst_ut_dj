from django.template import Template, Context
from django import template
from main_page.models import MenuItem


register = template.Library()


def render_menu(menu_item, current_path):
    is_active = current_path == menu_item.get_absolute_url()
    result = f'<ul><li'
    if is_active:
        result += ' class="active"'
        ancestors = menu_item.get_ancestors(include_self=True)
    else:
        ancestors = []
    result += f'><a href="{menu_item.get_absolute_url()}">{menu_item.title}</a>'

    if menu_item.children.all():
        result += '<ul'
        if is_active:
            result += ' style="display: block;"'
        result += '>'
        for child in menu_item.children.all():
            result += render_menu(child, current_path)
        result += '</ul>'

    result += '</li></ul>'
    return result


@register.simple_tag
def draw_menu(menu_name, current_path):
    try:
        menu_items = MenuItem.objects.filter(title=menu_name)
        if menu_items:
            return Template(render_menu(menu_items[0], current_path)).render(Context({}))
    except MenuItem.DoesNotExist:
        pass
    return ''




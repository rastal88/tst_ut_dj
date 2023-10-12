from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404
from main_page.models import MenuItem
class MainView(TemplateView):
    template_name = 'index.html'

def menu_item_detail(request, menu_item_id):
    menu_item = get_object_or_404(MenuItem, pk=menu_item_id)
    return render(request, 'item_detail.html', {'menu_item': menu_item})
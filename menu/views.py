from tkinter import Menu

from django.views.generic import ListView, TemplateView

from .models import TreeMenu


class MainMenuTemplateView(TemplateView):
    template_name = 'menu/main_menu.html'
    model = TreeMenu

    def get_context_data(self, **kwargs):
        context = super(MainMenuTemplateView, self).get_context_data()
        context['menu_items'] = TreeMenu.objects.filter(parent=None)
        context['submenu_items'] = TreeMenu.objects.filter(parent__isnull=False)
        return context


class MenuListView(ListView):
    template_name = 'menu/submenu.html'
    model = TreeMenu

    def get_context_data(self, **kwargs):
        context = super(MenuListView, self).get_context_data()
        context['menu_items'] = TreeMenu.objects.select_related('parent').filter(parent__slug=self.kwargs['menu_slug'])
        context['current_menu'] = TreeMenu.objects.get(slug=self.kwargs['menu_slug'])
        return context

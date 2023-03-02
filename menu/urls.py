from django.urls import path

from .views import MainMenuTemplateView, MenuListView

app_name = 'menu'

urlpatterns = [
    path('', MainMenuTemplateView.as_view(), name='main_menu'),
    path('<slug:menu_slug>/', MenuListView.as_view(), name='menu_list'),
]

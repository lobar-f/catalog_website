
from django.urls import path

from . import views
app_name='products'

urlpatterns = [
    path('', views.index, name='index'),
    path('about_us/', views.about_us, name='about_us'),
    path('faq/', views.faq, name='faq'),
    path('terms/', views.terms, name='terms'),
    path('contacts/', views.contacts, name='contacts'),
    path('products/', views.product_list, name='products'),
	path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
	path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]
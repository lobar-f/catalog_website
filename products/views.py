from django.shortcuts import render
from .models import Product, Category
# Create your views here.

from django.shortcuts import get_object_or_404

def index(request):
    return render(request, 'index.html', {})

def about_us(request):
    return render(request, 'about-us.html', {})

def faq(request):
    return render(request, 'faq.html', {})

def terms(request):
    return render(request, 'terms.html', {})

def contacts(request):
    return render(request, 'contacts.html', {})



def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                    'product_list.html',
                    {'category': category,
                    'categories': categories,
                    'products': products})

def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                            id=id,
                            slug=slug)
    return render(request,  'product_detail.html',   {'product': product})
from django.shortcuts import render
from .models import Product, Category, Banner

def home(request):
    categories = Category.objects.all()
    banner = Banner.objects.all()
    return render(request, 'home.html', {'categories': categories, 'banner':banner})

def category(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'category.html', {'category': category, 'products': products})

def product(request, category_slug, product_id):
    product = Product.objects.get(id=product_id)
    context = {'product': product}
    return render(request, 'product.html', context)

def custom_404(request, exception):
    return render(request, '404.html', status=404)
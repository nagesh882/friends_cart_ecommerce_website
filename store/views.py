from django.shortcuts import render, get_object_or_404
from store.models import Product
from category.models import Category
# Create your views here.
def store(request, category_slug=None):
    categories = None

    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.all().filter(category=categories, is_available=True)
        products_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        products_count = products.count()

    context = {
        'products_count' : products_count,
        'products' : products
    }
    return render(request, 'store/store.html', context)


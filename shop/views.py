from django.shortcuts import render
from models import Product, Category, Basket
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.


def index(request):
    categories = Category.objects.all()
    products = Product.objects.filter(active=True)
    paginator = Paginator(products, 10)
    page = request.GET.get('page', 1)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'categories': categories, 'products': products})


def category(request, category_slug):
    categories = Category.objects.all()
    active_category = Category.objects.get(slug=category_slug)
    products = Product.objects.filter(active=True, category=active_category)
    paginator = Paginator(products, 10)
    page = request.GET.get('page', 1)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'categories': categories, 'products': products,
                                          'active_category': active_category})


def product(request, product_slug):
    categories = Category.objects.all()
    product_obj = Product.objects.get(slug=product_slug)
    return render(request, 'index.html', {'categories': categories, 'product': product_obj})


def login(request):
    return render(request, 'login.html', {})


def register(request):
    return render(request, 'register.html', {})
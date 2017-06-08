# -*- encoding: utf-8 -*-
from django.shortcuts import render, redirect
from django.db.models import Sum
from models import Product, Category, Basket, Message
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.files import File
import datetime
# Create your views here.


def index(request):
    basket = 0
    if request.user.is_authenticated():
        basket = Basket.objects.filter(user=request.user).count()
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
    return render(request, 'index.html', {'categories': categories, 'products': products,
                                          'basket': basket})


def category(request, slug):
    basket = 0
    if request.user.is_authenticated():
        basket = Basket.objects.filter(user=request.user).count()
    categories = Category.objects.all()
    active_category = Category.objects.get(slug=slug)
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
                                          'active_category': active_category, 'basket': basket})


def product(request, slug):
    basket = 0
    if request.user.is_authenticated():
        basket = Basket.objects.filter(user=request.user).count()
    categories = Category.objects.all()
    product_obj = Product.objects.get(slug=slug)
    return render(request, 'product.html', {'categories': categories, 'product': product_obj,
                                            'basket': basket})


def add_to_basket(request):
    redirect_url = '/basket/'
    if request.GET.get('cont') is not None:
        redirect_url = '/'
    if not request.user.is_authenticated():
        return redirect('/login/')
    product_id = request.GET.get('id')
    if product_id is None:
        return redirect('/')
    Basket.objects.create(user=request.user, product_id=product_id)
    return redirect(redirect_url)


def basket(request):
    basket = 0
    if request.user.is_authenticated():
        basket = Basket.objects.filter(user=request.user).count()
    categories = Category.objects.all()
    products = Product.objects.filter(id__in=Basket.objects.filter(user=request.user)
                                      .values_list('product_id', flat=True))
    total_price = products.aggregate(sum=Sum('price')).get('sum')
    if total_price is None:
        total_price = 0
    return render(request, 'basket.html', {'products': products, 'price': total_price,
                                           'categories': categories, 'basket': basket})


def delete_from_basket(request):
    prod = request.GET.get('id')
    if prod is None:
        return redirect('/basket/')
    Basket.objects.filter(user=request.user, product_id=prod).delete()
    return redirect('/basket/')


def finish(request):
    with open('paps/static/media/receipt.txt', 'w') as f:
        myfile = File(f)
        products = Product.objects.filter(id__in=Basket.objects.filter(user=request.user)
                                          .values_list('product_id', flat=True))
        if not len(products):
            return redirect('/')
        total_price = products.aggregate(sum=Sum('price')).get('sum')
        for prod in products:
            str_t = '%s - %s\n' % (str(prod.name), str(prod.price))
            myfile.write(str_t)
        str_t = '-'*15 + '\n'
        myfile.write(str_t)
        myfile.write('TOTAL - %s\n' % str(total_price))
        myfile.write('Time - %s' % str(datetime.datetime.now()))
        Basket.objects.filter(user=request.user).delete()
        return redirect('/media/receipt.txt')

def help(request):
    return render(request, 'help.html', {})


def help_mes(request):
    message = request.GET.get('message')
    Message.objects.create(text=message)
    return redirect('/')
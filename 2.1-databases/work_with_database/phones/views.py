from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_phone = request.GET.get('sort')
    if sort_phone == 'min_price':
        phone_obj = Phone.objects.all().order_by('price')
    elif sort_phone == 'max_price':
        phone_obj = Phone.objects.all().order_by('-price')
    elif sort_phone == 'name':
        phone_obj = Phone.objects.all().order_by('name')
    else:
        phone_obj = Phone.objects.all()
    context = {
        'phones': phone_obj
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {
        'phone': Phone.objects.get(slug=slug)
    }
    return render(request, template, context)

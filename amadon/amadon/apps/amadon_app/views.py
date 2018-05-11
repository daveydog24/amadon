from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime

def index(request):
    return render(request, "amadon_app_templates/index.html")

def add_item(request):
    if 'items' not in request.session:
        request.session['items'] = []

    if request.method == "POST":
        name = request.POST['name']
        price = request.POST['price']
        request.session['price'] = price

    request.session['items'].append({'name': name, 'price': price})
    request.session.modified = True
    return redirect("/amadon/results")

def buy(request):
    if 'cart' not in request.session:
        request.session['cart'] = []

    request.session['quantity'] = request.POST.get('quantity')

    for item in request.session['items']:
        if item['name'] == request.POST.get('product'):
            request.session['price'] = item['price']
    request.session.modified = True
    return redirect("amadon/process")

def results(request):
    if 'items' not in request.session:
        request.session['items'] = []
    items = {
        "items": request.session['items']
    }
    return render(request, "amadon_app_templates/results.html", items)

def process(request):
    cart_price = int(request.session.get('price')) * int(request.session.get('quantity'))
    request.session['cart_price'] = cart_price
    if 'total_count' not in request.session:
        request.session['total_count'] = 1
    else:
        request.session['total_count'] += int(request.session['quantity'])
    if 'grand_total' not in request.session:
        request.session['grand_total'] = 0
    else:
        request.session['grand_total'] += cart_price
    return redirect('amadon/checkout')

def checkout(request):
    return render(request, "amadon_app_templates/checkout.html")

def clear(request):
    if request.method == "POST":
        request.session.clear()
    return redirect("/")

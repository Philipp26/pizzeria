from django.shortcuts import render
from .models import Pizza

def index(request):
    return render(request, 'pizz_app/index.html')

def pizzas(request):
    "Output the list of pizzas"
    pizzas = Pizza.objects.all()
    context = {'pizzas' : pizzas}
    return render(request, 'pizz_app/pizzas.html', context)

def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id = pizza_id)
    toppings = pizza.topping_set.all()
    context = {'pizza' : pizza, 'toppings' : toppings}
    return render(request, "pizz_app/pizza.html", context)

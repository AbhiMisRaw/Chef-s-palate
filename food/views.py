from django.http import HttpResponse
from django.shortcuts import render
from .models import Item
from django.template import loader

# Create your views here.


def hello_world(request):
    item_list = Item.objects.all() 
    template = loader.get_template('food/index.html')
    context = {
        'all_items' : item_list,
    }
    return render(request,'food/index.html',context)

def items(request):
    return HttpResponse("<h1>This is Items</h1>")

def details(request,item_id):
    item = Item.objects.get(pk=item_id)
    context={
        'item':item,
    }
    return render(request,'food/detail.html',context)
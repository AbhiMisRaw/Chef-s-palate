from django.http import HttpResponse
from django.shortcuts import redirect, render

from food.forms import ItemForm
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

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request , 'food/items-forms.html',{'form':form})

def update_item(request,item_id):
    item = Item.objects.get(id = item_id)
    form = ItemForm(request.POST or None , instance=item)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request, 'food/items-forms.html',{'form':form , 'item':item})

def delete_item(request , id):
    item = Item.objects.get(id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    return render(request, 'food/item-delete.html',{'item':item})
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import ShoppingListItem
from .forms import ItemForm
from django.views.generic.edit import DeleteView


# Create your views here.
def get_shopping_list(request):
    shoppinglistitems = ShoppingListItem.objects.all()
    context = {
        'shoppinglistitems': shoppinglistitems
    }
    return render(request, 'shoppinglist/shoppinglist.html', context)


# This function based view will allow a user to add a new item to his list
# & display his full list back
def add_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_shopping_list')
    # This will create an instance of our item form.
    form = ItemForm()
    # Then return it to the template in the context
    context = {
        'form': form
    }
    # This will return the html page on the next line to the user
    return render(request, 'shoppinglist/add_shopping_item.html', context)


def edit_item(request, item_id):
    listitem = get_object_or_404(ShoppingListItem, id=item_id)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=listitem)
        if form.is_valid():
            form.save()
            return redirect('get_shopping_list')
    form = ItemForm(instance=listitem)
    context = {
        'form': form
    }
    return render(request, 'shoppinglist/edit_shopping_item.html', context)


class DeleteView(DeleteView):
    model = ShoppingListItem
    context_object_name = 'shoppinglistitem'
    success_url = reverse_lazy('get_shopping_list')


def delete_list(request):
    ShoppingListItem.objects.all().delete()
    return redirect('get_shopping_list')

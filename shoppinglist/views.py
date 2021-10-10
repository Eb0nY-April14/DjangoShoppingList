from django.shortcuts import render
from .models import ShoppingListItem


# Create your views here.
def get_shopping_list(request):
    shoppinglistitems = ShoppingListItem.objects.all()
    context = {
        'shoppinglistitems': shoppinglistitems
    }
    return render(request, 'shoppinglist/shoppinglist.html', context)

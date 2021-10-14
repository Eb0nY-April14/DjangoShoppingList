from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
# from django.views.generic.detail import DetailView
# from django.views.generic.edit import CreateView
from .models import ShoppingListItem
from .forms import ItemForm
# from django.template import Context
# from django.urls import reverse_lazy
# from django.http import HttpResponse


# Create your views here.
def get_shopping_list(request):
    shoppinglistitems = ShoppingListItem.objects.all()
    context = {
        'shoppinglistitems': shoppinglistitems
    }
    return render(request, 'shoppinglist/shoppinglist.html', context)

# This view displays back to the user all the items in a list
# class ShoppingListList(ListView):
#     model = ShoppingListItem
#     context_object_name = 'shoppinglistitems'
#     template_name = 'shoppinglist/shoppinglist.html'  # don't touch this at all


# This function based view will allow a user to add a new item to his list & display his full list back
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
    # This will return the add_shopping_item.html template to the user
    return render(request, 'shoppinglist/add_shopping_item.html', context)

# This class based view will allow a user to add a new item to his list & display his list back
# class ShoppingListItemCreate(CreateView):
#     model = ShoppingListItem
#     fields = '__all__'
#     # render_template('shoppinglist.html')
#     # success_url = reverse_lazy('add_shopping_item.html')
#     template_name = 'shoppinglist/add_shopping_item.html'  # don't touch this at all


def edit_item(request, item_id ):
    # This will get an instance/a copy of the Item model that has an ID equal
    # to the item_id that was passed into the view via the URL from the database
    listitem = get_object_or_404(ShoppingListItem, id=item_id)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=listitem)
        if form.is_valid():
            form.save()
            return redirect('get_shopping_list')
    # This will create an instance of our item form & the instance
    # of listitem passed into the form as an argument will prepopulate
    # the form with the current shopping list item's details.
    form = ItemForm(instance=listitem)
    # Then return it to the template in the context
    context = {
        'form': form
    }
    return render(request, 'shoppinglist/edit_shopping_item.html', context)


# This view displays back to the user information about a specific shopping list item
# class ShoppingListDetail(DetailView):
#     model = ShoppingListItem


# class ShoppingListAdd(CreateView):
#     model = ShoppingListItem
#     def post(self, request):
#         AddItem.model = ShoppingListItem
#         if request.method == "POST":
#             add_form = ItemForm(request.POST)
#             if add_form.is_valid():
#                 add_form.save()
#                 return redirect('shoppinglist/add_shopping_item.html')
#         add_form = ItemForm()
#         context = {
#             'add_form': add_form
#         }
#         return render(
#             request,
#             'shoppinglistitem_list.html',
#             context
#         )


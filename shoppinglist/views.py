from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import DeleteView, FormView
from .forms import ItemForm
from django.urls import reverse_lazy
from django.contrib import messages

from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# from django_shoppinglist import helpers
from django.contrib import auth

from .models import ShoppingListItem


class CustomLoginView(LoginView):
    template_name = 'shoppinglist/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        messages.add_message(
            self.request, messages.SUCCESS, 'Logged in Successfully!')
        return reverse_lazy('get_shopping_list')


class RegisterView(FormView):
    template_name = 'shoppinglist/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('get_shopping_list')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('get_shopping_list')
        return super(RegisterView, self).get(*args, **kwargs)


def logout(request):
    auth.logout(request)
    template_name = 'shoppinglist/logout.html'
    return render(request, template_name)


#     url(r'^accounts/logout/$',
#     auth_views.logout,
#     {'template_name': 'blog/logout.html'},
#     name='logout'
# )

#     return reverse_lazy('login.html')
#     # return render(request, 'shoppinglist/logout.html')


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


def bought_item(request, item_id):
    listitem = get_object_or_404(ShoppingListItem, id=item_id)
    listitem.done_status = not listitem.done_status
    listitem.save()

    return redirect('get_shopping_list')

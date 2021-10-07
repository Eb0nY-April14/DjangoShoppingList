from django.shortcuts import render


# Create your views here.
def get_shopping_list(request):
    return render(request, 'shoppinglist/shoppinglist.html')

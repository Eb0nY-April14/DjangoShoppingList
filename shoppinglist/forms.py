from django import forms
from .models import ShoppingListItem


class ItemForm(forms.ModelForm):
    class Meta:
        model = ShoppingListItem
        fields = [
            'item_name',
            'unit_price',
            'quantity',
            'total_price',
            'done_status']

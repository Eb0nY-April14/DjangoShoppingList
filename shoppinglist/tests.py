from django.test import TestCase
from .models import ShoppingListItem


# Create your tests here.
# Test models.py file
class ModelTest(TestCase):

    def setUp(self):
        self.shoppinglistitem = ShoppingListItem()
        self.shoppinglistitem.item_name = "Toothpaste"
        self.shoppinglistitem.unit_price = 1.49
        self.shoppinglistitem.quantity = 4
        self.shoppinglistitem.total_price = 5.96
        self.shoppinglistitem.save()

    def test_fields(self):
        shoppinglistitem = ShoppingListItem()
        shoppinglistitem.item_name = "Toothpaste"
        shoppinglistitem.unit_price = 1.49
        shoppinglistitem.quantity = 4
        shoppinglistitem.total_price = 5.96
        # shoppinglistitem.done_status = False
        shoppinglistitem.save()

        record = ShoppingListItem.objects.get(pk=shoppinglistitem.id)
        self.assertEqual(record, shoppinglistitem)

    def test_done_status(self):
        self.shoppinglistitem.done_status
        self.assertEqual(self.shoppinglistitem.done_status, False)
        self.shoppinglistitem.done_status = True
        self.assertEqual(self.shoppinglistitem.done_status, True)

    # def test_calculate_total_price(self):
    #     totalprice = unit_price * quantity

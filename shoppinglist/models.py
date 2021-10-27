from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class ShoppingListItem(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=200, null=False, blank=False)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    done_status = models.BooleanField(null=False, blank=False, default=False)

    class Meta:
        # This will place items that are purchased
        # beneath the list & newly added ones on top
        ordering = ['done_status']


    def __str__(self):
        return self.item_name

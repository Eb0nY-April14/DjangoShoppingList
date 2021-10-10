from django.db import models


# Create your models here.
class ShoppingListItem(models.Model):
    item_name = models.CharField(max_length=200, null=False, blank=False)
    # user = models.ForeignKey(
    #    User, on_delete=models.CASCADE, related_name="list_items")
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    done_status = models.BooleanField(null=False, blank=False, default=False)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.item_name

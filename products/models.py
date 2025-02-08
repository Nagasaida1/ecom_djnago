from django.db import models
from users.models import CustomUser

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    image_url = models.URLField(blank=True, null=True)  # URL for product images
    vendor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'user_type': 'vendor'})

    def __str__(self):
        return self.title

class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'user_type': 'customer'})
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.title} - {self.quantity}"

from django.db import models

# The `TimestampModel` class is an abstract model in Django with `created_at` and `updated_at` fields
# for timestamp tracking.

class TimestampModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        abstract= True

class Category(TimestampModel):
    category_name=models.CharField(max_length=100)
    category_description=models.TextField(max_length=300)

    def __str__(self):
        return self.category_name

class Product(TimestampModel):
    product_name=models.CharField(max_length=50)
    product_description=models.TextField(max_length=150)
    price=models.DecimalField(max_digits=5, decimal_places=2)
    image=models.FileField(upload_to='products/')
    category=models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name
    
class order(TimestampModel):
    customer_name=models.CharField(max_length=60)
    customer_email=models.EmailField()
    customer_address=models.TextField(max_length=200)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()

    def __str__(self):
        return f"Order #{self.id}"
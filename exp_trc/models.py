from django.db import models

# Create your models here.
class Expense(models.Model):
    """A topic the user is learning about."""
    name=models.CharField(max_length=10)
    amount=models.DecimalField(max_digits=9,decimal_places=2)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
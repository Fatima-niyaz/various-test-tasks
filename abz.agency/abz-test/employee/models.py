from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Employee(MPTTModel):
    name = models.CharField(max_length=30, unique=True)
    job = models.CharField(max_length=30)
    employment_date = models.DateField(auto_now_add=False)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return '{}'.format(self.name) + ' ' + '{}'.format(self.job)

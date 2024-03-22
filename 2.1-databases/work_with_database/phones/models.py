from django.db import models


class Phone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.ImageField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    release_date = models.DateTimeField()
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.name


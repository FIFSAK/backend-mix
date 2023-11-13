from django.db import models


class Size(models.Model):
    size = models.CharField(max_length=10)

    def __str__(self):
        return self.size


class Trousers(models.Model):
    name = models.TextField()
    vendore_code = models.BigIntegerField()
    price = models.IntegerField()
    count = models.IntegerField()
    sizes = models.ManyToManyField(Size)

    def __str__(self):
        return self.name


class TshirtsAndTops(models.Model):
    pass

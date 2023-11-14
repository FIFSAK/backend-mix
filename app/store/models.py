from django.db import models


class Size(models.Model):
    size = models.CharField(max_length=10)

    def __str__(self):
        return self.size


class Clothes(models.Model):
    name = models.TextField()
    vendore_code = models.BigIntegerField()
    price = models.IntegerField()
    count = models.IntegerField()
    sizes = models.ManyToManyField(Size)

    class Meta:
        abstract = True


class Trousers(Clothes):

    def __str__(self):
        return self.name


class TShirtsAndTops(Clothes):

    def __str__(self):
        return self.name


class Jacket(Clothes):

    def __str__(self):
        return self.name


class ShirtsAndBlouses(Clothes):

    def __str__(self):
        return self.name


class Dresses(Clothes):

    def __str__(self):
        return self.name


class OverallsJacketsRaincoatsCardigans(Clothes):

    def __str__(self):
        return self.name


class pantsuitsShortsSkirts(Clothes):

    def __str__(self):
        return self.name


class Jeans(Clothes):

    def __str__(self):
        return self.name


class Underwear(Clothes):

    def __str__(self):
        return self.name

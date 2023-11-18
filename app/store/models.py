import boto3
from django.db import models
from django.contrib import admin

from app import settings


class Size(models.Model):
    size = models.CharField(max_length=10)

    def __str__(self):
        return self.size


class Clothes(models.Model):
    image = models.ImageField(upload_to='images/', null=True)
    name = models.TextField()
    vendore_code = models.BigIntegerField()
    price = models.IntegerField()
    count = models.IntegerField()
    sizes = models.ManyToManyField(Size)

    def delete(self, *args, **kwargs):
        # Connect to S3
        s3 = boto3.client('s3',
                          aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                          aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)

        # Delete the file from S3
        if self.image:
            s3.delete_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key=self.image.name)
        super(Clothes, self).delete(*args, **kwargs)

    class Meta:
        abstract = True


class ClothesAdmin(admin.ModelAdmin):
    def delete_queryset(self, request, queryset):
        for obj in queryset:
            obj.delete()

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

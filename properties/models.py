from django.db import models
from users.models import User


class Property(models.Model):
    HOUSE = "house"
    DEPARTMENT = "deparment"
    LAND = "land"
    TYPE_PROPERTY = (
        (HOUSE,  "Casa"),
        (DEPARTMENT, "Departamento"),
        (LAND, "Terreno"),
    )
    description = models.CharField(max_length=200, blank=True, null=True)
    street = models.CharField(max_length=100, blank=True, null=True)
    colony = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=6, blank=True, null=True)
    external_number = models.CharField(max_length=5, blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=4, default=0)
    type = models.CharField(max_length=100, choices=TYPE_PROPERTY, blank=True, null=True)
    wide = models.FloatField(default=0)
    long = models.FloatField(default=0)
    ranking = models.IntegerField(default=0)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.PROTECT, related_name="property_user", blank=True, null=True)


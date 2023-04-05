from django.db import models
from django.contrib.auth.models import User

# from diwe_product.models import DiweRegion


# GENRES = (("Adulte", "Adulte"), ("Enfant", "Enfant"))

# LISTE_TYPES = (
#     ("VOIE", "Voie"),
#     ("AVENUE", "Avenue"),
#     ("TER", "Ter"),
#     ("RUE", "Rue"),
#     ("ALLEE", "Allée"),
# )


# class Country(models.Model):
#     country_name = models.CharField(max_length=100, blank=True, null=True)

#     def __str__(self):
#         return self.name


# class City(models.Model):
#     city_name = models.CharField(max_length=100, blank=True, null=True)
#     region = models.ForeignKey(DiweRegion, on_delete=models.SET_NULL, null=True)
#     zip_code = models.CharField(max_length=10, blank=True)
#     country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)

#     def __str__(self):
#         return self.city_name


# class Street(models.Model):
#     street_name = models.CharField(max_length=100)
#     street_type = models.CharField(
#         max_length=50, choices=LISTE_TYPES, blank=True, null=True)
#     city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
#     zip_code = models.CharField(max_length=10, blank=True, null=True)

#     def __str__(self):
#         return self.street_name


# class Adress(models.Model):
#     numero = models.CharField(max_length=30, blank=True)
#     complement = models.CharField(
#         default="facultatif", max_length=50, blank=True, null=True)
#     street = models.ForeignKey(Street, on_delete=models.SET_NULL, null=True)

#     def __str__(self):
#         return (str(self.numero) + ", " + str(self.street))


# class Client(models.Model):
#     user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
#     # adresse = models.ForeignKey(Adress, on_delete=models.CASCADE, null=True)
#     date_naissance = models.DateField()
#     segment = models.CharField(choices=GENRES, max_length=10)
#     tel1 = models.CharField(max_length=15, blank=True)
#     tel2 = models.CharField(max_length=15, blank=True, null=True)

#     class Meta:
#         verbose_name = "Client"
#         verbose_name_plural = "Clients"

#     def __str__(self):
#         return (str(self.user.first_name) + " " + str(self.user.last_name))


# class ShippingAddress(models.Model):
#     order = models.OneToOneField(
#         'Order', on_delete=models.CASCADE, null=True, blank=True)
#     address = models.CharField(max_length=200, null=True, blank=True)
#     city = models.CharField(max_length=200, null=True, blank=True)
#     postalCode = models.CharField(max_length=200, null=True, blank=True)
#     country = models.CharField(max_length=200, null=True, blank=True)
#     shippingPrice = models.DecimalField(
#         max_digits=7, decimal_places=2, null=True, blank=True)
#     _id = models.AutoField(primary_key=True, editable=False)

#     def __str__(self):
#         return str(self.address)

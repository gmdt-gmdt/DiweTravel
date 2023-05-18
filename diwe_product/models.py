import random
from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver


LISTE_SEGMENT = (("Adulte", "Adulte"), ("Enfant", "Enfant"))

LISTE_DEVISE = (("EURO", "EURO"), ("DOLLAR", "DOLLAR"))


class Accueil(models.Model):
    tel1 = models.CharField(max_length=100, blank=True)
    tel2 = models.CharField(max_length=100, blank=True)
    mail = models.EmailField(
        max_length=250, default="buhofergnami@fastmail.fm")
    image = models.ImageField(upload_to="static/media/img/", blank=True)
    image1 = models.ImageField(upload_to="static/media/img/", blank=True)
    image2 = models.ImageField(upload_to="static/media/img/", blank=True)
    whatsapp = models.CharField(
        max_length=255, blank=True, null=True, default="https://www.whatsapp.com/")
    facebook = models.CharField(
        max_length=255, blank=True, null=True, default="https://www.facebook.com/")
    instagram = models.CharField(
        max_length=255, blank=True, null=True, default="https://www.instagram.com/")
    twitter = models.CharField(max_length=255, blank=True,
                             null=True, default="https://twitter.com/")
    
    description = models.TextField()
    _id = models.AutoField(primary_key=True, editable=False)
    
    def __str__(self):
        return self.mail


class Pays(models.Model):
    name = models.CharField(max_length=100, blank=True, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Pays"
        verbose_name_plural = "Pays"


class DiweRegion(models.Model):
    name = models.CharField(max_length=200, null=False)
    description = models.TextField()
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regions"


class Ville(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    region = models.ForeignKey(
        DiweRegion, on_delete=models.SET_NULL, null=True)
    code_postal = models.CharField(max_length=10, blank=True)
    pays = models.ForeignKey(
        Pays, on_delete=models.SET_NULL, null=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name


class DiweCategory(models.Model):
    name = models.CharField(max_length=200, null=False)
    description = models.TextField()
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Categorie"
        verbose_name_plural = "Categories"


class DiweRoute(models.Model):
    name = models.CharField(max_length=200, null=False)
    travel_mode = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    route_lenght = models.FloatField()
    duration = models.IntegerField()
    is_circle = models.BooleanField()
    score = models.IntegerField()
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Route"
        verbose_name_plural = "Routes"


class Site(models.Model):
    ville = models.ForeignKey(
        Ville, on_delete=models.CASCADE)
    category = models.ForeignKey(
        DiweCategory, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200, blank=True)
    rue = models.CharField(max_length=128, blank=True)
    numero_rue = models.CharField(max_length=20, blank=True, null=False)
    laltitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField()
    score = models.IntegerField()
    source = models.CharField(max_length=100, blank=True, null=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name


class Sequence(models.Model):
    route = models.ForeignKey(DiweRoute, on_delete=models.CASCADE, null=True)
    start_site = models.ForeignKey(
        Site, related_name="start_sites", on_delete=models.CASCADE, null=True)
    end_site = models.ForeignKey(
        Site, related_name="end_sites", on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.route.name) + " : " + str(self.start_site.name) + " --> " + str(self.end_site.name)


class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    sequence = models.ForeignKey(
        Sequence, on_delete=models.CASCADE, null=True)
    route = models.ForeignKey(DiweRoute, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField()
    package = models.ForeignKey(
        'Package', on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to="static/media/img/", null=True, blank=True)
    video = models.FileField(upload_to='static/media/video/', blank=True, null=True)
    vitrine = models.BooleanField()
    _id = models.AutoField(primary_key=True, editable=False)

    def save(self, *args, **kwargs):
        self.name = self.site.name + " : " + self.package.name
        super(Image, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Produit"
        verbose_name_plural = "Produits"


class ContactSite(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    tel1 = models.CharField(max_length=64, blank=True, null=True)
    tel2 = models.CharField(max_length=64, blank=True, null=True)
    mail = models.EmailField(max_length=200, blank=True, null=False)
    website = models.CharField(max_length=255, blank=True, null=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name


class Schedule(models.Model):
    site = models.ForeignKey(Site, on_delete=models.SET_NULL, null=True)
    opening_time = models.DateTimeField()
    closing_time = models.DateTimeField()
    week_day = models.CharField(max_length=255, blank=True, null=True)
    delay = models.DurationField(default=timedelta)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.site.name


class Distance(models.Model):
    start_site = models.ForeignKey(
        Site, related_name="dis_start_sites", on_delete=models.SET_NULL, null=True)
    end_site = models.ForeignKey(
        Site, related_name="dis_end_sites", on_delete=models.SET_NULL, null=True)
    travel_mode = models.CharField(max_length=200, blank=True, null=True)
    time_between_site = models.DurationField()
    distance_between_site = models.FloatField()
    _id = models.AutoField(primary_key=True, editable=False)


class Package(models.Model):
    name = models.CharField(max_length=200, null=False)
    description = models.TextField()
    tarif = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=False)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name


class TypeService(models.Model):
    name = models.CharField(max_length=200, null=False)
    description = models.TextField()
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name


class Service(models.Model):
    type_service = models.ForeignKey(
        TypeService, on_delete=models.DO_NOTHING, blank=True)
    site = models.ForeignKey(Site, on_delete=models.DO_NOTHING, blank=True)
    package = models.ForeignKey(
        Package, on_delete=models.DO_NOTHING, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.site.name) + "-" + str(self.type_service.name)


class Commande(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    reference = models.CharField(max_length=50, blank=True, null=True)
    tel1 = models.CharField(max_length=50)
    tel2 = models.CharField(max_length=50, blank=True, null=True)
    segment = models.CharField(
        max_length=50, choices=LISTE_SEGMENT)
    pays = CountryField()
    ville = models.CharField(max_length=50)
    code_postal = models.CharField(max_length=10)
    rue = models.CharField(max_length=128)
    numero_rue = models.CharField(max_length=20)
    commande_date = models.DateTimeField(
        auto_now_add=True, blank=True, null=False)
    devise = models.CharField(
        max_length=20, choices=LISTE_DEVISE, blank=True, null=False)
    _id = models.AutoField(primary_key=True, editable=False)

    def save(self, *args, **kwargs):
        self.user = self.request.user
        super(Commande, self).save(*args, **kwargs)

    def __str__(self):
        return self.reference


class DetailCommande(models.Model):
    commande = models.ForeignKey(
        Commande, on_delete=models.CASCADE, blank=True)
    package = models.ForeignKey(
        Package, on_delete=models.DO_NOTHING, blank=True)
    prix_unitaire = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=False)
    quantite = models.IntegerField()
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.commande) + "-" + str(self.package)
    
    class Meta:
        verbose_name = "Detail commande"
        verbose_name_plural = "Detail commandes"


class Participant(models.Model):
    commande = models.ForeignKey(
        Commande, on_delete=models.CASCADE, blank=True)
    nom = models.CharField(max_length=50, blank=True, null=False)
    prenom = models.CharField(max_length=50, blank=True, null=False)
    date_naissance = models.DateField()
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.commande) + "-" + str(self.nom) + "-" + str(self.prenom)



@receiver(post_save, sender=Commande)
def update_commande(sender, created, instance, **kwargs):
    if created:
        randomVal = f'{random.randrange(1, 10**2):02}'
        date = datetime.now()
        anneeYY = date.strftime("%y")
        moisMM = date.strftime("%m")
        pk_ref = str(instance.pk)
        id_ref = pk_ref.rjust(5, '9')
        instance.reference = anneeYY + moisMM + id_ref + randomVal

        instance.save()

    return instance




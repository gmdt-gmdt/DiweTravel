from datetime import datetime
import random
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Commande


def updateCommande(sender, instance, **kwargs):
    randomVal = f'{random.randrange(1, 10**2):02}'
    date = datetime.now()
    anneeYY = date.strftime("%y")
    moisMM = date.strftime("%m")
    pk_ref = str(instance.pk)
    id_ref = pk_ref.rjust(5, '9')

    instance.reference = anneeYY + moisMM + id_ref + randomVal


post_save.connect(updateCommande, sender=Commande)

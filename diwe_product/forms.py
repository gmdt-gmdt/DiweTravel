import csv
import re
import django.forms.widgets

from datetime import datetime
from datetime import date
from django import forms

from diwe_product.models import Commande, Distance, Image, Schedule, Sequence, Site, TypeService



class ImageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ImageForm, self).__init__(*args, **kwargs)
        # self.fields["date_cours"].label = "Date du cours"
    
    class Meta:
        model = Image
        fields = ('site', 'sequence', 'route',
                  'description', 'package', 'image', 'video', 'vitrine')


class SiteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SiteForm, self).__init__(*args, **kwargs)
        self.fields["category"].label = "Categorie"
        self.fields["name"].label = "Nom du site"
        self.fields["rue"].label = "Nom de la rue"
        self.fields["numero_rue"].label = "Numero de la rue"

    class Meta:
        model = Site
        fields = ('ville', 'category', 'name',
                  'rue', 'numero_rue', 'laltitude', 'longitude', 'description', 'score')


class SequenceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SequenceForm, self).__init__(*args, **kwargs)
        self.fields["route"].label = "Route"
        self.fields["start_site"].label = "Site de depart"
        self.fields["end_site"].label = "Site d'arrivé"

    class Meta:
        model = Sequence
        fields = ('route', 'start_site', 'end_site', 'description')


class ScheduleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ScheduleForm, self).__init__(*args, **kwargs)
        self.fields["opening_time"].label = "Ouverture"
        self.fields["closing_time"].label = "Fermeture"
        self.fields["week_day"].label = "Jour"
        self.fields["delay"].label = "Durée"

    class Meta:
        model = Schedule
        fields = ('site', 'opening_time', 'closing_time', 'week_day', 'delay')


class DistanceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DistanceForm, self).__init__(*args, **kwargs)
        self.fields["start_site"].label = "Site de depart"
        self.fields["end_site"].label = "Site d'arrivé"
        self.fields["travel_mode"].label = "Mode de deplacement"
        self.fields["time_between_site"].label = "Durée du trajet"
        self.fields["distance_between_site"].label = "Distance"

    class Meta:
        model = Distance
        fields = ('start_site', 'end_site',
                  'travel_mode', 'time_between_site', 'distance_between_site')


class TypeServiceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TypeServiceForm, self).__init__(*args, **kwargs)
        self.fields["name"].label = "Nom"

    class Meta:
        model = TypeService
        fields = ('name', 'description')


class CommandeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommandeForm, self).__init__(*args, **kwargs)
        self.fields["rue"].label = "Nom de la rue"
        self.fields["numero_rue"].label = "Numero de la rue"
        self.fields["tel1"].label = "Telephone portable"
        self.fields["tel2"].label = "Telephone fixe"

    class Meta:
        model = Commande
        fields = ('segment', 'pays',
                  'ville', 'code_postal', 'rue', 'numero_rue', 'tel1', 'tel2', 'devise')
        


from django.utils import timezone
from django_countries import Countries
from rest_framework import serializers, fields
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django_countries.serializer_fields import CountryField


from base.serializers import UserSerializer

from .models import (
    DiweRegion, Site, Service,
    Image, ContactSite,
    Distance, Sequence, DiweCategory,
    DiweRoute, TypeService,
    Ville, Package, Schedule,
    Commande, DetailCommande,
    Participant, Pays
)


class ServiceSerializer(serializers.ModelSerializer):
    # packages = serializers.SerializerMethodField(read_only=True)
    #sites = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Service
        fields = '__all__'

    # def get_packages(self, obj):
    #     items = obj.package_set.all()
    #     serializer = PackageSerializer(items, many=True)
    #     return serializer.data

    # def get_sites(self, obj):
    #     items = obj.site_set.all()
    #     serializer = SiteSerializer(items, many=True)
    #     return serializer.data


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'


class TypeServiceSerializer(serializers.ModelSerializer):
    services = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = TypeService
        fields = '__all__'

    def get_services(self, obj):
        items = obj.service_set.all()
        serializer = ServiceSerializer(items, many=True)
        return serializer.data


class ContactSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSite
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):
    opening_time = fields.DateField(input_formats=['%Y-%m-%dT%H:%M:%S.%fZ'])
    closing_time = fields.DateField(input_formats=['%Y-%m-%dT%H:%M:%S.%fZ'])
    delay = serializers.DurationField()

    class Meta:
        model = Schedule
        fields = ['site', 'opening_time',
                  'closing_time', 'week_day', 'delay']


class DistanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Distance
        fields = '__all__'


class PaysSerializer(serializers.ModelSerializer):
    villes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Pays
        fields = '__all__'

    def get_villes(self, obj):
        items = obj.ville_set.all()
        serializer = VilleSerializer(items, many=True)
        return serializer.data


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'


class DetailCommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailCommande
        fields = '__all__'


class CommandeSerializer(serializers.ModelSerializer):
    segment = serializers.CharField(source='get_segment_display')
    devise = serializers.CharField(source='get_devise_display')
    # pays = CountryField()

    class Meta:
        model = Commande
        fields = ('user', 'reference', 'tel1',
                  'tel2', 'segment', 'pays', 'ville', 'code_postal', 'rue', 'numero_rue', 'commande_date', 'devise')


class VilleSerializer(serializers.ModelSerializer):
    sites = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Ville
        fields = '__all__'

    def get_sites(self, obj):
        items = obj.site_set.all()
        serializer = SiteSerializer(items, many=True)
        return serializer.data


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class DiweRouteSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField(read_only=True)
    sequences = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = DiweRoute
        fields = '__all__'

    def get_images(self, obj):
        items = obj.image_set.all()
        serializer = ImageSerializer(items, many=True)
        return serializer.data

    def get_sequences(self, obj):
        items = obj.sequence_set.all()
        serializer = SequenceSerializer(items, many=True)
        return serializer.data


class DiweRegionSerializer(serializers.ModelSerializer):
    villes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = DiweRegion
        fields = '__all__'

    def get_villes(self, obj):
        items = obj.ville_set.all()
        serializer = VilleSerializer(items, many=True)
        return serializer.data


class DiweCategorySerializer(serializers.ModelSerializer):
    sites = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = DiweCategory
        fields = '__all__'

    def get_sites(self, obj):
        items = obj.site_set.all()
        serializer = SiteSerializer(items, many=True)
        return serializer.data


class SiteSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField(read_only=True)
    schedules = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Site
        fields = '__all__'

    def get_images(self, obj):
        items = obj.image_set.all()
        serializer = ImageSerializer(items, many=True)
        return serializer.data

    def get_schedules(self, obj):
        items = obj.schedule_set.all()
        serializer = ScheduleSerializer(items, many=True)
        return serializer.data


class SequenceSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Sequence
        fields = '__all__'

    def get_images(self, obj):
        items = obj.image_set.all()
        serializer = ImageSerializer(items, many=True)
        return serializer.data

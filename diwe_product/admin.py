from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from django.utils.html import format_html
from django.forms import TextInput, Textarea

from diwe_product.forms import CommandeForm, DistanceForm, ImageForm, ScheduleForm, SequenceForm, SiteForm, TypeServiceForm

from .models import *


class DiweCategoryAdmin(admin.ModelAdmin):
    def editModel(self, obj):
        return format_html(
            '<span aria-label="Modifier" class="text-info"><span class="fa fa-edit" aria-hidden="true" title="Modifier" style=""></span></span>'
        )
    editModel.short_description = "Action"

    def get_name(self, obj):
        return obj.name
    get_name.short_description = "Nom"

    list_display = ('editModel', 'get_name', 'description')
    list_display_links = ('editModel', )


class DiweRegionAdmin(admin.ModelAdmin):
    def editModel(self, obj):
        return format_html(
            '<span aria-label="Modifier" class="text-info"><span class="fa fa-edit" aria-hidden="true" title="Modifier" style=""></span></span>'
        )
    editModel.short_description = "Action"

    def get_name(self, obj):
        return obj.name
    get_name.short_description = "Nom"

    list_display = ('editModel', 'get_name', 'description')
    list_display_links = ('editModel', )


class DiweRouteAdmin(admin.ModelAdmin):
    def editModel(self, obj):
        return format_html(
            '<span aria-label="Modifier" class="text-info"><span class="fa fa-edit" aria-hidden="true" title="Modifier" style=""></span></span>'
        )
    editModel.short_description = "Action"

    def get_name(self, obj):
        return obj.name
    get_name.short_description = "Nom"

    def get_travel_mode(self, obj):
        return obj.travel_mode
    get_travel_mode.short_description = "Moyen de déplacement"

    def get_route_lenght(self, obj):
        return obj.route_lenght
    get_route_lenght.short_description = "Distance"

    def get_duration(self, obj):
        return obj.duration
    get_duration.short_description = "Durée"

    list_display = ('editModel', 'get_name', 'get_travel_mode', 'description',
                    'get_route_lenght', 'get_duration', 'score', 'is_circle')
    list_display_links = ('editModel', )
    search_fields = ('name', 'travel_mode', 'route_lenght', 'duration')


class ImageAdmin(admin.ModelAdmin):
    form = ImageForm

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.image.url))

    thumbnail.short_description = 'Produit'

    def editModel(self, obj):
        return format_html(
            '<span aria-label="Modifier" class="text-info"><span class="fa fa-edit" aria-hidden="true" title="Modifier" style=""></span></span>'
        )
    editModel.short_description = "Action"

    def get_name(self, obj):
        return obj.name
    get_name.short_description = "Nom"

    list_display = ('editModel', 'thumbnail', 'vitrine', 'site', 'sequence',
                    'route', 'get_name', 'description', 'user')
    list_display_links = ('editModel',)
    search_fields = ['site__name', 'route__name', 'name']


class SiteAdmin(admin.ModelAdmin):
    form = SiteForm

    def thumbnail(self, obj):
        return format_html(
            '<span aria-label="Modifier" class="text-info"><span class="fa fa-edit" aria-hidden="true" title="Modifier" style=""></span></span>'
        )
    thumbnail.short_description = "Action"

    def get_name(self, obj):
        return obj.name
    get_name.short_description = "Nom"

    list_display = ('thumbnail', 'get_name', 'ville', 'category',
                    'rue', 'numero_rue', 'laltitude', 'longitude', 'score')
    list_display_links = ('thumbnail',)
    search_fields = ['ville__name', 'category__name', 'name']


class SequenceAdmin(admin.ModelAdmin):
    form = SequenceForm

    def thumbnail(self, obj):
        return format_html(
            '<span aria-label="Modifier" class="text-info"><span class="fa fa-edit" aria-hidden="true" title="Modifier" style=""></span></span>'
        )
    thumbnail.short_description = "Action"

    def get_start_site(self, obj):
        return obj.start_site
    get_start_site.short_description = "Site de depart"

    def get_end_site(self, obj):
        return obj.end_site
    get_end_site.short_description = "Site d'arrivé"

    list_display = ('thumbnail', 'route', 'get_start_site',
                    'get_end_site', 'description')
    list_display_links = ('thumbnail', )
    search_fields = ['route__name', 'start_site__name', 'end_site__name']


class ContactSiteAdmin(admin.ModelAdmin):
    def thumbnail(self, obj):
        return format_html(
            '<span aria-label="Modifier" class="text-info"><span class="fa fa-edit" aria-hidden="true" title="Modifier" style=""></span></span>'
        )
    thumbnail.short_description = "Action"

    def get_name(self, obj):
        return obj.name
    get_name.short_description = "Nom"

    list_display = ('thumbnail', 'get_name', 'site', 'tel1', 'tel2', 'mail')
    list_display_links = ('thumbnail', )
    search_fields = ['site__name', 'name', 'tel1']


class ScheduleAdmin(admin.ModelAdmin):
    form = ScheduleForm

    def thumbnail(self, obj):
        return format_html(
            '<span aria-label="Modifier" class="text-info"><span class="fa fa-edit" aria-hidden="true" title="Modifier" style=""></span></span>'
        )
    thumbnail.short_description = "Action"

    def get_opening_time(self, obj):
        return obj.opening_time
    get_opening_time.short_description = "Heure d'ouverture"

    def get_closing_time(self, obj):
        return obj.closing_time
    get_closing_time.short_description = "Heure de fermeture"

    def get_week_day(self, obj):
        return obj.week_day
    get_week_day.short_description = "Jour"

    def get_deday(self, obj):
        return obj.delay
    get_deday.short_description = "Durée"

    list_display = ('thumbnail', 'site', 'get_opening_time',
                    'get_closing_time', 'get_week_day', 'get_deday')
    list_display_links = ('thumbnail', )
    search_fields = ['site__name', 'opening_time', 'closing_time']


class DistanceAdmin(admin.ModelAdmin):
    form = DistanceForm

    def thumbnail(self, obj):
        return format_html(
            '<span aria-label="Modifier" class="text-info"><span class="fa fa-edit" aria-hidden="true" title="Modifier" style=""></span></span>'
        )
    thumbnail.short_description = "Action"

    def get_start_site(self, obj):
        return obj.start_site
    get_start_site.short_description = "Site de depart"

    def get_end_site(self, obj):
        return obj.end_site
    get_end_site.short_description = "Site d'arrivé"

    def get_travel_mode(self, obj):
        return obj.travel_mode
    get_travel_mode.short_description = "Moyen de déplacement"

    def get_time_between_site(self, obj):
        return obj.time_between_site
    get_time_between_site.short_description = "Durée"

    def get_distance_between_site(self, obj):
        return obj.distance_between_site
    get_distance_between_site.short_description = "Distance"

    list_display = ('thumbnail', 'get_start_site', 'get_end_site',
                    'get_travel_mode', 'get_time_between_site', 'get_distance_between_site')
    list_display_links = ('thumbnail', )
    search_fields = ['start_site__name', 'end_site__name', 'travel_mode']


class VilleAdmin(admin.ModelAdmin):
    def thumbnail(self, obj):
        return format_html(
            '<span aria-label="Modifier" class="text-info"><span class="fa fa-edit" aria-hidden="true" title="Modifier" style=""></span></span>'
        )
    thumbnail.short_description = "Action"

    def get_name(self, obj):
        return obj.name
    get_name.short_description = "Nom"

    list_display = ('thumbnail', 'get_name', 'code_postal', 'region', 'pays')
    list_display_links = ('thumbnail', )
    search_fields = ['name', 'pays__name', 'code_postal']


class TypeServiceAdmin(admin.ModelAdmin):
    form = TypeServiceForm

    def thumbnail(self, obj):
        return format_html(
            '<span aria-label="Modifier" class="text-info"><span class="fa fa-edit" aria-hidden="true" title="Modifier" style=""></span></span>'
        )
    thumbnail.short_description = "Action"

    def get_name(self, obj):
        return obj.name
    get_name.short_description = "Nom"

    list_display = ('thumbnail', 'get_name', 'description')
    list_display_links = ('thumbnail', )
    search_fields = ['name', ]


class ServiceAdmin(admin.ModelAdmin):
    def thumbnail(self, obj):
        return format_html(
            '<span aria-label="Modifier" class="text-info"><span class="fa fa-edit" aria-hidden="true" title="Modifier" style=""></span></span>'
        )
    thumbnail.short_description = "Action"

    list_display = ('thumbnail', 'type_service', 'site', 'package')
    list_display_links = ('thumbnail', )
    search_fields = ['site__name', ]


class PackageAdmin(admin.ModelAdmin):
    def thumbnail(self, obj):
        return format_html(
            '<span aria-label="Modifier" class="text-info"><span class="fa fa-edit" aria-hidden="true" title="Modifier" style=""></span></span>'
        )
    thumbnail.short_description = "Action"

    def get_name(self, obj):
        return obj.name
    get_name.short_description = "Nom"

    list_display = ('thumbnail', 'get_name', 'tarif', 'description')
    list_display_links = ('thumbnail', )
    search_fields = ['name', ]


class CommandeAdmin(admin.ModelAdmin):
    form = CommandeForm

    def thumbnail(self, obj):
        return format_html(
            '<span aria-label="Modifier" class="text-info"><span class="fa fa-edit" aria-hidden="true" title="Modifier" style=""></span></span>'
        )
    thumbnail.short_description = "Action"

    # .strftime("%d %b %Y %H:%M:%S")

    def get_commande(self, obj):
        return obj.commande_date.strftime("%d %b %Y %H:%M:%S")
    get_commande.short_description = "Date de la commande"


    list_display = ('thumbnail', 'user', 'reference', 'tel1', 'tel2',
                    'segment', 'pays', 'ville', 'code_postal', 'rue', 'numero_rue', 'commande_date', 'devise')
    list_display_links = ('thumbnail', 'reference')
    search_fields = ['reference', 'tel1']


class CommandeDetailsAdmin(admin.ModelAdmin):
    def thumbnail(self, obj):
        return format_html(
            '<span aria-label="Modifier" class="text-info"><span class="fa fa-edit" aria-hidden="true" title="Modifier" style=""></span></span>'
        )
    thumbnail.short_description = "Action"

    list_display = ('thumbnail', 'commande', 'package',
                    'prix_unitaire', 'quantite')
    list_display_links = ('thumbnail', )
    search_fields = ['commande__reference', 'package__name']


class ParticipantAdmin(admin.ModelAdmin):
    def thumbnail(self, obj):
        return format_html(
            '<span aria-label="Modifier" class="text-info"><span class="fa fa-edit" aria-hidden="true" title="Modifier" style=""></span></span>'
        )

    thumbnail.short_description = "Action"

    list_display = ('thumbnail', 'commande', 'nom', 'prenom', 'date_naissance')
    list_display_links = ('thumbnail', )
    search_fields = ['commande__reference', 'nom', 'prenom']


class AccueilAdmin(admin.ModelAdmin):
    def thumbnail(self, obj):
        return format_html(
            '<span aria-label="Modifier" class="text-info"><span class="fa fa-edit" aria-hidden="true" title="Modifier" style=""></span></span>'
        )

    thumbnail.short_description = "Action"

    list_display = ('thumbnail', 'tel1', 'tel2', 'mail', 'whatsapp',
                    'facebook', 'instagram', 'twitter')
    list_display_links = ('thumbnail', )


class UserAdmin(BaseUserAdmin):
    def editModel(self, obj):
        return format_html(
            '<span aria-label="Modifier" class="text-info"><span class="fa fa-edit" aria-hidden="true" title="Modifier" style=""></span></span>'
        )
    editModel.short_description = "Action"

    def get_username(self, obj):
        return obj.username
    get_username.short_description = "Identifiant"

    def get_first_name(self, obj):
        return obj.first_name
    get_first_name.short_description = "Prenom"

    def get_last_name(self, obj):
        return obj.last_name
    get_last_name.short_description = "Nom"

    def get_mail(self, obj):
        return obj.email
    get_mail.short_description = "Mail"

    def get_isadmin(self, obj):
        return obj.is_staff
    get_isadmin.short_description = "Is_admin"

    list_display = ('editModel', 'get_username',
                    'get_first_name', 'get_last_name', 'get_mail', 'get_isadmin')
    list_display_links = ('editModel', )



admin.site.register(DiweCategory, DiweCategoryAdmin)
admin.site.register(DiweRegion, DiweRegionAdmin)
admin.site.register(DiweRoute, DiweRouteAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Site, SiteAdmin)
admin.site.register(Sequence, SequenceAdmin)
admin.site.register(ContactSite, ContactSiteAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Distance, DistanceAdmin)
admin.site.register(Pays)
admin.site.register(Ville, VilleAdmin)
admin.site.register(TypeService, TypeServiceAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Package, PackageAdmin)
admin.site.register(Commande, CommandeAdmin)
admin.site.register(DetailCommande, CommandeDetailsAdmin)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Accueil, AccueilAdmin)


admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(User, UserAdmin)

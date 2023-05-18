from django.urls import path
from . import views


urlpatterns = [

    path('category/', views.getDiweCategory, name='category'),

    path('create-category/', views.createDiweCategory, name="diwe_category"),

    path('update-category/<str:pk>/',
         views.updateCategory, name="update_category"),

    path('delete-category/<str:pk>/',
         views.deleteCategory, name='category_delete'),

    path('region/', views.getDiweRegion, name="region"),

    path('create-region/', views.createDiweRegion, name="diwe_region"),

    path('update-region/<str:pk>/',
         views.updateRegion, name="update_region"),

    path('delete-region/<str:pk>/',
         views.deleteRegion, name='region_delete'),

    path('route/', views.getDiweRoute, name="route"),

    path('create-route/', views.createDiweRoute, name="diwe_route"),

    path('update-route/<str:pk>/',
         views.updateRoute, name="update_route"),

    path('delete-route/<str:pk>/',
         views.deleteRoute, name='route_delete'),

    path('pays/', views.getDiwePays, name="pays"),

    path('create-pays/', views.createDiwePays, name="create_pays"),

    path('update-pays/<str:pk>/',
         views.updatePays, name="update_pays"),

    path('delete-pays/<str:pk>/',
         views.deletePays, name="pays_delete"),

    path('ville/', views.getDiweVille, name="ville"),

    path('create-ville/', views.createDiweVille, name="create_ville"),

    path('update-ville/<str:pk>/',
         views.updateVille, name="update_ville"),

    path('delete-ville/<str:pk>/',
         views.deleteVille, name="ville_delete"),

    path('site/', views.getDiweSite, name="site"),

    path('create-site/', views.createDiweSite, name="create_site"),

    path('update-site/<str:pk>/',
         views.updateSite, name="update_site"),

    path('delete-site/<str:pk>/',
         views.deleteSite, name="site_delete"),

    path('sequence/', views.getDiweSequence, name="sequence"),

    path('create-sequence/', views.createDiweSequence, name="create_sequence"),

    path('update-sequence/<str:pk>/',
         views.updateSequence, name="update_sequence"),

    path('delete-sequence/<str:pk>/',
         views.deleteSequence, name="sequence_delete"),

    path('image/', views.getImage, name="image"),

    path('create-image/', views.createImage, name="diwe_image"),

    path('upload/', views.uploadImage, name="image_upload"),

    path('update-image/<str:pk>/',
         views.updateImage, name="update_image"),

    path('delete-image/<str:pk>/', views.deleteImage, name="image_delete"),

    path('contactsite/', views.getContactSite, name="contact_site"),

    path('create-contactsite/', views.createDiweContactSite, name="create_contact"),

    path('update-contactsite/<str:pk>/',
         views.updateContactSite, name="update_contactsite"),

    path('delete-contactsite/<str:pk>/',
         views.deleteContactSite, name="contactsite_delete"),

    path('schedule/', views.getSchedule, name="schedule"),

    path('create-schedule/', views.createDiweSchedule, name="create_schedule"),

    path('update-schedule/<str:pk>/',
         views.updateSchedule, name="update_schedule"),

    path('delete-schedule/<str:pk>/',
         views.deleteSchedule, name="schedule_delete"),

    path('distance/', views.getDistance, name="distance"),

    path('create-distance/', views.createDiweDistance, name="create_distance"),

    path('update-distance/<str:pk>/',
         views.updateDistance, name="update_distance"),

    path('delete-distance/<str:pk>/',
         views.deleteDistance, name="distance_delete"),

    path('typeservice/', views.getTypeService, name="typeservice"),

    path('create-typeservice/', views.createTypeService, name="create_typeservice"),

    path('update-typeservice/<str:pk>/',
         views.updateTypeService, name="update_typeservice"),

    path('delete-typeservice/<str:pk>/',
         views.deleteTypeService, name="typeservice_delete"),

    path('service/', views.getService, name="service"),

    path('create-service/', views.createService, name="create_service"),

    path('update-service/<str:pk>/',
         views.updateService, name="update_service"),

    path('delete-service/<str:pk>/',
         views.deleteService, name="service_delete"),

    path('package/', views.getPackage, name="package"),

    path('create-package/', views.createPackage, name="create_package"),

    path('update-package/<str:pk>/',
         views.updatePackage, name="update_package"),

    path('delete-package/<str:pk>/',
         views.deletePackage, name="package_delete"),

    path('commande/', views.getCommande, name="commande"),

    path('create-commande/', views.createDiweCommande, name="create_commande"),

    path('update-commande/<str:pk>/',
         views.updateCommande, name="update_commande"),

    path('delete-commande/<str:pk>/',
         views.deleteCommande, name="commande_delete"),

    path('detailcommande/', views.getDetailCommande,
         name="detailcommande"),

    path('create-detailcommande/', views.createDetailCommande,
         name="create_detailcommande"),

    path('update-detailcommande/<str:pk>/',
         views.updateDetailCommande, name="update_detailcommande"),

    path('delete-detailcommande/<str:pk>/',
         views.deleteDetailCommande, name="detailcommande_delete"),

    path('participant/', views.getParticipant,
         name="participant"),

    path('create-participant/', views.createParticipant,
         name="create_participant"),

    path('update-participant/<str:pk>/',
         views.updateParticipant, name="update_participant"),

    path('delete-participant/<str:pk>/',
         views.deleteParticipant, name="participant_delete"),

     path('accueil/', views.getAccueil, name="accueil"),

    path('create-accueil/', views.createAccueil,
         name="create_accueil"),

    path('update-accueil/<str:pk>/',
         views.updateAccueil, name="update_accueil"),

    path('delete-accueil/<str:pk>/',
         views.deleteAccueil, name="accueil_delete"),

]

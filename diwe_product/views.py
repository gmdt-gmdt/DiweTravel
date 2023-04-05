from time import strftime
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime, timedelta

from diwe_product.models import (
    Image, Sequence, DiweRoute, DiweCategory,
    DiweRegion, Site, ContactSite, Distance,
    Ville, Commande, DetailCommande, Participant, Pays,
    TypeService, Package, Service, Schedule
)
from diwe_product.serializers import (
    ImageSerializer, SiteSerializer, ContactSiteSerializer,
    DistanceSerializer, SequenceSerializer, DiweRouteSerializer, DiweRegionSerializer,
    DiweCategorySerializer, VilleSerializer, CommandeSerializer,
    DetailCommandeSerializer, PaysSerializer, ScheduleSerializer,
    TypeServiceSerializer, PackageSerializer, ServiceSerializer, ParticipantSerializer
)

from rest_framework import status


@api_view(['GET'])
def getDiweCategory(request):
    categorys = DiweCategory.objects.all()
    serializer = DiweCategorySerializer(categorys, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def createDiweCategory(request):
    data = request.data
    try:
        category = DiweCategory.objects.create(
            name=data['name'],
            description=data['description'],
        )
        serializer = DiweCategorySerializer(category, many=False)

        return Response(serializer.data)
    except:
        message = {'detail': 'This category already exists'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateCategory(request, pk):
    category = DiweCategory.objects.get(id=pk)

    data = request.data

    category.name = data['name']
    category.description = data['description']

    category.save()

    serializer = DiweCategorySerializer(category, many=False)

    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteCategory(request, pk):
    categoryForDeletion = DiweCategory.objects.get(id=pk)
    categoryForDeletion.delete()
    return Response('Category was deleted')


@api_view(['GET'])
def getDiweRegion(request):
    regions = DiweRegion.objects.all()
    serializer = DiweRegionSerializer(regions, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def createDiweRegion(request):
    data = request.data
    try:
        region = DiweRegion.objects.create(
            name=data['name'],
            description=data['description'],
        )

        serializer = DiweRegionSerializer(region, many=False)
        print(serializer.data)

        return Response(serializer.data)
    except:
        message = {'detail': 'This region already exists'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateRegion(request, pk):
    region = DiweRegion.objects.get(id=pk)

    data = request.data

    region.name = data['name']
    region.description = data['description']

    region.save()

    serializer = DiweRegionSerializer(region, many=False)

    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteRegion(request, pk):
    regionForDeletion = DiweRegion.objects.get(id=pk)
    regionForDeletion.delete()
    return Response('Region was deleted')


@api_view(['GET'])
def getDiweRoute(request):
    routes = DiweRoute.objects.all()
    serializer = DiweRouteSerializer(routes, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def createDiweRoute(request):
    data = request.data
    try:
        route = DiweRoute.objects.create(
            name=data['name'],
            travel_mode=data['travel_mode'],
            description=data['description'],
            route_lenght=data['route_lenght'],
            duration=data['duration'],
            is_circle=data['is_circle'],
            score=data['score'],
        )

        serializer = DiweRouteSerializer(route, many=False)

        return Response(serializer.data)
    except:
        message = {'detail': 'This route already exists'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateRoute(request, pk):
    route = DiweRoute.objects.get(id=pk)

    data = request.data

    route.name = data['name']
    route.travel_mode = data['travel_mode']
    route.description = data['description']
    route.route_lenght = data['route_lenght']
    route.duration = data['duration']
    route.is_circle = data['is_circle']
    route.score = data['score']

    route.save()

    serializer = DiweRouteSerializer(route, many=False)

    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteRoute(request, pk):
    routeForDeletion = DiweRoute.objects.get(id=pk)
    routeForDeletion.delete()
    return Response('Route was deleted')


@api_view(['GET'])
def getDiwePays(request):
    pays = Pays.objects.all()
    serializer = PaysSerializer(pays, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def createDiwePays(request):
    data = request.data
    try:
        pays = Pays.objects.create(
            name=data['name'],
        )
        serializer = PaysSerializer(pays, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'This pays already exists'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updatePays(request, pk):
    pays = Pays.objects.get(id=pk)
    data = request.data

    pays.name = data['name']

    pays.save()

    serializer = PaysSerializer(pays, many=False)

    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deletePays(request, pk):
    pays = Pays.objects.get(_id=pk)
    pays.delete()
    return Response('Pays Deleted')


@api_view(['GET'])
def getDiweVille(request):
    villes = Ville.objects.all()
    serializer = VilleSerializer(villes, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def createDiweVille(request):
    data = request.data
    region = DiweRegion.objects.get(_id=data['region'])
    pays = Pays.objects.get(id=data['pays'])
    try:
        ville = Ville.objects.create(
            name=data['name'],
            region=region,
            code_postal=data["code_postal"],
            pays=pays,
        )
        serializer = VilleSerializer(ville, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'Thanks !'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateVille(request, pk):
    ville = Ville.objects.get(_id=pk)
    data = request.data

    region = DiweRegion.objects.get(_id=data['region'])
    pays = Pays.objects.get(id=data['pays'])

    ville.name = data['name']
    ville.region = region
    ville.code_postal = data["code_postal"]
    ville.pays = pays

    ville.save()

    serializer = VilleSerializer(ville, many=False)

    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteVille(request, pk):
    ville = Ville.objects.get(_id=pk)
    ville.delete()
    return Response('ville Deleted')


@api_view(['GET'])
def getDiweSite(request):
    sites = Site.objects.all()
    serializer = SiteSerializer(sites, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def createDiweSite(request):
    data = request.data

    ville = Ville.objects.get(_id=data['ville'])
    category = DiweCategory.objects.get(_id=data['category'])

    try:
        site = Site.objects.create(
            ville=ville,
            category=category,
            name=data["name"],
            rue=data["rue"],
            numero_rue=data["numero_rue"],
            laltitude=data["laltitude"],
            longitude=data["longitude"],
            description=data["description"],
            scrore=data["scrore"],
            source=data["source"],
        )
        serializer = SiteSerializer(site, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'Thanks !'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateSite(request, pk):
    site = Site.objects.get(_id=pk)
    data = request.data

    ville = Ville.objects.get(_id=data['ville'])
    category = DiweCategory.objects.get(_id=data['category'])

    site.ville = ville
    site.category = category
    site.name = data["name"]
    site.rue = data["rue"]
    site.numero_rue = data["numero_rue"]
    site.laltitude = data["laltitude"]
    site.longitude = data["longitude"]
    site.description = data["description"]
    site.scrore = data["scrore"]
    site.source = data["source"]

    site.save()

    serializer = SiteSerializer(site, many=False)

    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteSite(request, pk):
    site = Site.objects.get(_id=pk)
    site.delete()
    return Response('Site Deleted')


@api_view(['GET'])
def getDiweSequence(request):
    sequences = Sequence.objects.all()
    serializer = SequenceSerializer(sequences, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def createDiweSequence(request):
    data = request.data

    route = DiweRoute.objects.get(_id=data['route'])
    start_site = Site.objects.get(_id=data['start_site'])
    end_site = Site.objects.get(_id=data['end_site'])

    try:
        sequence = Sequence.objects.create(
            route=route,
            start_site=start_site,
            end_site=end_site,
            description=data["description"],
        )
        serializer = SequenceSerializer(sequence, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'Thanks !'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateSequence(request, pk):
    sequence = Sequence.objects.get(_id=pk)
    data = request.data

    route = DiweRoute.objects.get(_id=data['route'])
    start_site = Site.objects.get(_id=data['start_site'])
    end_site = Site.objects.get(_id=data['end_site'])

    sequence.route = route
    sequence.start_site = start_site
    sequence.end_site = end_site
    sequence.description = data["description"]

    sequence.save()

    serializer = SequenceSerializer(sequence, many=False)

    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteSequence(request, pk):
    sequence = Sequence.objects.get(_id=pk)
    sequence.delete()
    return Response('Sequence Deleted')


@api_view(['GET'])
def getImage(request):
    images = Image.objects.all()
    serializer = ImageSerializer(images, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def createImage(request):
    user = request.user
    data = request.data

    site = Site.objects.get(_id=data['site'])
    sequence = Sequence.objects.get(_id=data['sequence'])
    route = DiweRoute.objects.get(_id=data['route'])

    try:

        image = Image.objects.create(
            user=user,
            site=site,
            sequence=sequence,
            route=route,
            name=data['name'],
            description=data['description'],
        )

        serializer = ImageSerializer(image, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'Thanks !'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def uploadImage(request):
    data = request.data

    image = Image.objects.get(_id=data['image'])

    image.image = request.FILES.get('image')
    image.save()

    return Response('Image was uploaded')


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateImage(request, pk):
    image = Image.objects.get(_id=pk)
    user = request.user
    data = request.data

    site = Site.objects.get(_id=data['site'])
    sequence = Sequence.objects.get(_id=data['sequence'])
    route = DiweRoute.objects.get(_id=data['route'])

    image.user = user
    image.site = site
    image.sequence = sequence
    image.route = route
    image.name = data['name']
    image.description = data['description']

    image.save()

    serializer = ImageSerializer(image, many=False)

    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteImage(request, pk):
    image = Image.objects.get(_id=pk)
    image.delete()
    return Response('Image Deleted')


@api_view(['GET'])
def getContactSite(request):
    contactsites = ContactSite.objects.all()
    serializer = ContactSiteSerializer(contactsites, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def createDiweContactSite(request):
    data = request.data

    site = Site.objects.get(_id=data['site'])
    try:
        contact_site = ContactSite.objects.create(
            site=site,
            name=data['name'],
            tel1=data["tel1"],
            tel2=data["tel2"],
            mail=data['mail'],
            website=data['website'],
        )
        serializer = ContactSiteSerializer(contact_site, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'Thanks !'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateContactSite(request, pk):
    contact_site = ContactSite.objects.get(_id=pk)
    data = request.data

    site = Site.objects.get(_id=data['site'])

    contact_site.site = site
    contact_site.name = data['name']
    contact_site.tel1 = data["tel1"]
    contact_site.tel2 = data["tel2"]
    contact_site.mail = data['mail']
    contact_site.website = data['website']

    contact_site.save()

    serializer = ContactSiteSerializer(contact_site, many=False)

    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteContactSite(request, pk):
    contact_site = ContactSite.objects.get(_id=pk)
    contact_site.delete()
    return Response('Contact site Deleted')


@api_view(['GET'])
def getSchedule(request):  # à revoir car problème avec datetime
    schedules = Schedule.objects.all()
    serializer = ScheduleSerializer(schedules, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def createDiweSchedule(request):
    data = request.data

    site = Site.objects.get(_id=data['site'])

    try:
        schedule = Schedule.objects.create(
            site=site,
            opening_time=data['opening_time'],
            closing_time=data["closing_time"],
            week_day=data["week_day"],
            delay=timedelta(minutes=int(data['delay'])),
        )
        print(schedule)
        serializer = ScheduleSerializer(schedule, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'Thanks !'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateSchedule(request, pk):
    schedule = Schedule.objects.get(_id=pk)
    data = request.data
    site = Site.objects.get(_id=data['site'])

    schedule.site = site
    schedule.opening_time = data['opening_time']
    schedule.closing_time = data["closing_time"]
    schedule.week_day = data["week_day"]
    schedule.delay = timedelta(minutes=int(data['delay']))

    schedule.save()

    serializer = ScheduleSerializer(schedule, many=False)

    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteSchedule(request, pk):
    schedule = Schedule.objects.get(_id=pk)
    schedule.delete()
    return Response('Schedule Deleted')


@api_view(['GET'])
def getDistance(request): 
    distances = Distance.objects.all()
    serializer = DistanceSerializer(distances, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def createDiweDistance(request):
    data = request.data
    start_site = Site.objects.get(_id=data['start_site'])
    end_site = Site.objects.get(_id=data['end_site'])

    try:
        distance = Distance.objects.create(
            start_site=start_site,
            end_site=end_site,
            travel_mode=data["travel_mode"],
            time_between_site=timedelta(
                minutes=int(data["time_between_site"])),
            distance_between_site=data['distance_between_site'],
        )
        print(distance)
        serializer = DistanceSerializer(distance, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'Thanks !'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateDistance(request, pk):
    distance = Distance.objects.get(_id=pk)
    data = request.data

    start_site = Site.objects.get(_id=data['start_site'])
    end_site = Site.objects.get(_id=data['end_site'])

    distance.start_site = start_site
    distance.end_site = end_site
    distance.travel_mode = data["travel_mode"]
    distance.time_between_site = timedelta(
        minutes=int(data["time_between_site"]))
    distance.distance_between_site = data['distance_between_site']

    distance.save()

    serializer = DistanceSerializer(distance, many=False)

    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteDistance(request, pk):
    distance = Distance.objects.get(_id=pk)
    distance.delete()
    return Response('Distance Deleted')


@api_view(['GET'])
def getTypeService(request): 
    typeservices = TypeService.objects.all()
    serializer = TypeServiceSerializer(typeservices, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def createTypeService(request):
    data = request.data

    try:
        typeservice = TypeService.objects.create(
            name=data['name'],
            description=data['description'],
        )
        serializer = TypeServiceSerializer(typeservice, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'Thanks !'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateTypeService(request, pk):
    typeservice = TypeService.objects.get(_id=pk)
    data = request.data

    typeservice.name = data['name']
    typeservice.description = data['description']

    typeservice.save()

    serializer = TypeServiceSerializer(typeservice, many=False)

    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteTypeService(request, pk):
    typeservice = TypeService.objects.get(_id=pk)
    typeservice.delete()
    return Response('Typeservice Deleted')


@api_view(['GET'])
def getService(request): 
    services = Service.objects.all()
    serializer = ServiceSerializer(services, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def createService(request):
    data = request.data
    type_service = TypeService.objects.get(_id=data['type_service'])
    site = Site.objects.get(_id=data['site'])
    package = Package.objects.get(_id=data['package'])

    try:
        service = Service.objects.create(
            type_service=type_service,
            site=site,
            package=package,
        )
        serializer = ServiceSerializer(service, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'Thanks !'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateService(request, pk):
    service = Service.objects.get(_id=pk)
    data = request.data

    type_service = TypeService.objects.get(_id=data['type_service'])
    site = Site.objects.get(_id=data['site'])
    package = Package.objects.get(_id=data['package'])

    service.type_service = type_service
    service.site = site
    service.package = package

    service.save()
    serializer = ServiceSerializer(service, many=False)

    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteService(request, pk):
    service = Service.objects.get(_id=pk)
    service.delete()
    return Response('Service Deleted')


@api_view(['GET'])
def getPackage(request): 
    packages = Package.objects.all()
    serializer = PackageSerializer(packages, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def createPackage(request):
    data = request.data
    try:
        package = Package.objects.create(
            name=data['name'],
            description=data['description'],
            tarif=data['tarif'],
        )
        serializer = PackageSerializer(package, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'Thanks !'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updatePackage(request, pk):
    package = Package.objects.get(_id=pk)
    data = request.data

    package.name = data['name']
    package.description = data['description']
    package.tarif = data['tarif']

    package.save()
    serializer = PackageSerializer(package, many=False)

    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deletePackage(request, pk):
    package = Package.objects.get(_id=pk)
    package.delete()
    return Response('Package Deleted')


@api_view(['GET'])
def getCommande(request): 
    commandes = Commande.objects.all()
    serializer = CommandeSerializer(commandes, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createDiweCommande(request):
    data = request.data
    user = request.user

    try:
        commandes = Commande.objects.create(
            user=user,
            reference=data['reference'],
            tel1=data["tel1"],
            tel2=data["tel2"],
            segment=data["segment"],
            pays=data["pays"],
            ville=data["ville"],
            code_postal=data["code_postal"],
            rue=data["rue"],
            numero_rue=data['numero_rue'],
            # commande_date=data["commande_date"],
            devise=data["devise"]

        )
        print(commandes)
        serializer = CommandeSerializer(commandes, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'Thanks !'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateCommande(request, pk):
    commande = Commande.objects.get(_id=pk)
    data = request.data
    user = request.user

    commande.user = user,
    commande.reference = data['reference'],
    commande.tel1 = data["tel1"],
    commande.tel2 = data["tel2"],
    commande.segment = data["segment"],
    commande.pays = data["pays"],
    commande.ville = data["ville"],
    commande.code_postal = data["code_postal"],
    commande.rue = data["rue"],
    # commande.commande_date = data["commande_date"],
    commande.devise = data["devise"]

    commande.save()
    serializer = CommandeSerializer(commande, many=False)

    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteCommande(request, pk):
    commande = Commande.objects.get(_id=pk)
    commande.delete()
    return Response('Commande Deleted')


@api_view(['GET'])
def getDetailCommande(request): 
    detailcommandes = DetailCommande.objects.all()
    serializer = DetailCommandeSerializer(detailcommandes, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createDetailCommande(request):
    data = request.data
    commande = Commande.objects.get(_id=data['commande'])
    package = Package.objects.get(_id=data['package'])

    try:
        details = DetailCommande.objects.create(
            commande=commande,
            package=package,
            prix_unitaire=data["prix_unitaire"],
            quantite=data["quantite"],
        )

        serializer = DetailCommandeSerializer(details, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'Thanks !'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateDetailCommande(request, pk):
    detail = DetailCommande.objects.get(_id=pk)

    data = request.data

    commande = Commande.objects.get(_id=data['commande'])
    package = Package.objects.get(_id=data['package'])

    detail.commande = commande
    detail.package = package
    detail.prix_unitaire = data["prix_unitaire"],
    detail.quantite = data["quantite"],

    detail.save()
    serializer = DetailCommandeSerializer(detail, many=False)

    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteDetailCommande(request, pk):
    detail = DetailCommande.objects.get(_id=pk)
    detail.delete()
    return Response('Detail Deleted')


@api_view(['GET'])
def getParticipant(request): 
    participants = Participant.objects.all()
    serializer = ParticipantSerializer(participants, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createParticipant(request):
    data = request.data
    commande = Commande.objects.get(_id=data['commande'])

    try:
        participant = Participant.objects.create(
            commande=commande,
            nom=data['nom'],
            prenom=data["prenom"],
            date_naissance=data["date_naissance"],
        )
        serializer = ParticipantSerializer(participant, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'Thanks !'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateParticipant(request, pk):
    participant = Participant.objects.get(_id=pk)

    data = request.data

    commande = Commande.objects.get(_id=data['commande'])

    participant.commande = commande
    participant.nom = data['nom']
    participant.prenom = data["prenom"]
    participant.date_naissance = data["date_naissance"]

    participant.save()

    serializer = ParticipantSerializer(participant, many=False)

    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteParticipant(request, pk):
    participant = Participant.objects.get(_id=pk)
    participant.delete()
    return Response('Participant Deleted')

from django.shortcuts import render
from django.views.generic import ListView
from .models import Guest
from rest_framework import generics
from .models import Event, Item, GuestItem
from .serializers import EventSerializer,ItemSerializer, GuestSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response


class GuestListView(generics.ListAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

class EventListView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class InvitationView(ListView):
    template_name = 'invitation.html'
    context_object_name = 'Guest'

    def get_queryset(self):
    # Filtrar objetos por un criterio
        return Guest.objects.all()
    

class ItemListAPIView(APIView):
    def get(self, request, event_id):
        # Obtener el evento por ID
        try:
            event = Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            return Response({"error": "Evento no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        
        # Obtener los items cuyo evento sea posterior o el mismo que el evento recibido
        items = Item.objects.filter(event__start_time__gte=event.start_time)
        
        # Serializar los items
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class confirm_items(APIView):
    """
    Endpoint para confirmar los ítems seleccionados por un invitado.
    Recibe un JSON con el ID del invitado y los IDs de los ítems seleccionados.
    """

    def post(self, request):
        guest_id = request.data.get('guest_id')  # ID del invitado
        item_ids = request.data.get('item_ids', [])  # Lista de IDs de los ítems seleccionados
        password = request.data.get('password')  # Lista de IDs de los ítems seleccionados
        
        print(password)
        # Validar que el invitado exista
        guest = Guest.objects.filter(id=guest_id, password=password).first()
        if not guest:
            return Response({"detail": "Invitado no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        
        # Validar que los ítems existan
        items = Item.objects.filter(id__in=item_ids)
        if not items:
            return Response({"detail": "Ítems no encontrados"}, status=status.HTTP_404_NOT_FOUND)
        
        # Crear las relaciones GuestItem
        guest_items = []
        for item in items:
            guest_items.append(GuestItem(guest=guest, item=item, confirmed=True))
        
        # Guardar las relaciones en la base de datos
        GuestItem.objects.bulk_create(guest_items)
        
        return Response({"detail": "Ítems confirmados correctamente"}, status=status.HTTP_201_CREATED)
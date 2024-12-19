from django.urls import path
from .views import InvitationView, EventListView, ItemListAPIView, GuestListView, confirm_items


urlpatterns = [
    path('invitation/', InvitationView.as_view(), name='invitation'),  # Enlace a la vista
    path('api/events/', EventListView.as_view(), name='event-list'),
    path('api/items/<int:event_id>/', ItemListAPIView.as_view(), name='item-list'),
    path('guests/', GuestListView.as_view(), name='guest-list'),
    path('confirm-items/', confirm_items.as_view(), name='confirm-items'),
]

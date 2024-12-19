from django.db import models

# Create your models here.

class Guest(models.Model):
    name = models.CharField(blank=False, null=False, verbose_name="Nombre", max_length=256)
    password = models.CharField(blank=False, null=False, verbose_name="password", max_length=256)

class Gift(models.Model):
    name = models.CharField(blank=False, null=False, verbose_name="Nombre", max_length=256)


class Event(models.Model):
    name = models.CharField(max_length=200, verbose_name="Event Name")
    description = models.TextField(blank=True, verbose_name="Event Description")
    start_time = models.DateTimeField(verbose_name="Start Time")
    end_time = models.DateTimeField(verbose_name="End Time")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
        ordering = ['start_time']


class Item(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="items", verbose_name="Event")
    name = models.CharField(max_length=200, verbose_name="Item Name")
    description = models.TextField(blank=True, verbose_name="Item Description")
    image = models.ImageField(upload_to='event_items/', blank=True, null=True, verbose_name="Item Image")
    unique = models.BooleanField(default=False)
    personal = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"


class GuestItem(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, related_name="guest_items", verbose_name="Guest")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="guest_items", verbose_name="Item")
    
    # Otras propiedades adicionales si lo necesitas
    confirmed = models.BooleanField(default=False)  # Confirmación del invitado para el item
    
    def __str__(self):
        return f"{self.guest.name} - {self.item.name}"

    class Meta:
        verbose_name = "Guest Item"
        verbose_name_plural = "Guest Items"
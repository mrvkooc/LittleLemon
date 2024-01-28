from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import generics, viewsets, permissions

from restaurant import models, serializers

# Create your views here.
def index(request):
    return render(request, 'index.html', {})


# Create your views here. 
class MenuItemsView(generics.ListCreateAPIView):
    queryset = models.MenuItem.objects.all()
    serializer_class = serializers.MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = models.MenuItem.objects.all()
    serializer_class = serializers.MenuItemSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = models.Booking.objects.all()
    serializer_class = serializers.BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
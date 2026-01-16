from rest_framework import generics
from .models import Plot
from .serializers import PlotSerializer, PlotBookingSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.permissions import IsSales
from rest_framework.permissions import IsAuthenticated

class PlotListCreateView(generics.ListCreateAPIView):
    queryset = Plot.objects.all()
    serializer_class = PlotSerializer

class PlotDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plot.objects.all()
    serializer_class = PlotSerializer
    lookup_field = 'pk'

class PlotBookView(APIView):
    permission_classes = [IsAuthenticated, IsSales]
    serializer_class = PlotBookingSerializer
    def post(self, request, id):
        plot = Plot.objects.get(pk=id)
        if not plot.is_available:
            return Response({"error": "Plot is already booked."}, status=400)
        
        plot.is_available = False
        plot.booked_for = request.data.get("booked_for", "Not Booked")
        plot.booked_by = request.user
        plot.save()
        
        serializer = PlotSerializer(plot)
        return Response(serializer.data)

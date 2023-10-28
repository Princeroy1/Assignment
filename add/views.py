from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Ad, DailyVisitor
from .serializers import AdSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Location
from .serializers import LocationSerializer,VisitorCountSerializer
from rest_framework.viewsets import ModelViewSet
from datetime import date
from django.shortcuts import render

@api_view(['GET'])
def get_ads_by_location(request, location_keyword):
    try:
        location_keyword=location_keyword.title()
        if location_keyword is None:
            return Response({'message': 'location_keyword is required in the URL path'}, status=status.HTTP_400_BAD_REQUEST)
        today = date.today()

        filtered_visitors = DailyVisitor.objects.filter(location__name=location_keyword, is_blocked=True)
        f = DailyVisitor.objects.filter(location__name=location_keyword, is_blocked=False)
        max_visitors_values = f.values('location__max_visitors')
        for max_visitors_value in max_visitors_values:
          max_visitors = max_visitors_value['location__max_visitors']

        non_blocked_ad_ids = [visitor.ad.id for visitor in filtered_visitors]
       
        ads = Ad.objects.filter(locations__name=location_keyword).exclude(id__in=non_blocked_ad_ids)
        for data in f:
            if data.visitor_count==max_visitors:
              data.is_blocked=True
              data.save()
            else:
              data.visitor_count+=1
              data.save() 


        serializer = AdSerializer(ads, many=True)
        for ad_data in serializer.data:
            ad = Ad.objects.get(pk=ad_data['id'])
            location_names = [location.name for location in ad.locations.all()]
            ad_data['locations'] = location_names

        response_data = serializer.data if serializer.data else {}
        return Response(response_data, status=status.HTTP_200_OK)
    except Ad.DoesNotExist:
        return Response({'message': 'Location not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def create_ad(request):
    serializer = AdSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_ad(request, pk):
    try:
        ad = Ad.objects.get(id=pk)
        ad.delete()
        return Response({'message': 'Ad deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except Ad.DoesNotExist:
        return Response({'message': 'Ad not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def update_ad(request, pk):
    try:
        ad = Ad.objects.get(id=pk)
        serializer = AdSerializer(ad, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Ad.DoesNotExist:
        return Response({'message': 'Ad not found'}, status=status.HTTP_404_NOT_FOUND)
    
class LocationListView(ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class LocationDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class DailyVisitorViewSet(ModelViewSet):
    queryset = DailyVisitor.objects.all()
    serializer_class = VisitorCountSerializer

def Report(request):
    
    if request.method == "POST":
     selected_location = request.POST.get("location")
     
     filtered_visitors = DailyVisitor.objects.filter(location__name=selected_location, is_blocked=True)
     print(filtered_visitors)
     filtered2 = DailyVisitor.objects.filter(location__name=selected_location, is_blocked=False)
    location=Location.objects.all()
    return render(request,'Report.html',locals())
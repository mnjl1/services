from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Location, WorkerLocationJobInterval
from .serializers import LocationSerializer, WorkerLocationJobIntervalSerializer


class LocationList(APIView):
    def get(self, request, format=None):
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WorkerJobIntervalList(APIView):
    def get(self, request, format=None):
        jobs = WorkerLocationJobInterval.free_for_appontment_objects.all()
        serializer = WorkerLocationJobIntervalSerializer(jobs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = WorkerLocationJobIntervalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
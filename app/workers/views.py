from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Speciality, Worker
from .serializers import SpecialtySerializer, WorkerSerializer


class SpecialtyList(APIView):
    def get(self, request, format=None):
        skills = Speciality.objects.all()
        serializer = SpecialtySerializer(skills, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SpecialtySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SpecialtyDetail(APIView):
    def get_object(self, pk):
        try:
            return Speciality.objects.get(pk=pk)
        except Speciality.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        skill = self.get_object(pk)
        serializer = SpecialtySerializer(skill)
        return Response(serializer.data)


class WorkersList(APIView):
    def get(self, request, format=None):
        workers = Worker.objects.all()
        serializer = WorkerSerializer(workers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = WorkerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WorkerDetail(APIView):
    def get_object(self, pk):
        try:
            return Worker.objects.get(pk=pk)
        except Speciality.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        worker = self.get_object(pk)
        serializer = WorkerSerializer(worker)
        return Response(serializer.data)

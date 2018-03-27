from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.views import APIView,status
from rest_framework.response import Response
from rest_framework import authentication, permissions
from voltageapi.serializers import MeasurementSerializer
from voltageapi.models import measurement
# Create your views here.

class MeasurementList(APIView):
    @csrf_exempt
    def get(self,request):
        measurements = measurement.objects.all()
        serializer=MeasurementSerializer(measurements,many=True)
        return Response(serializer.data)
    @csrf_exempt
    def post(self,request):
        serializer = MeasurementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

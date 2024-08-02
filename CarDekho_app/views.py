from django.shortcuts import render
from .models import Carlist, showroomList
from django.http import JsonResponse
from .api_file.serializers import CarSerializer, showroomSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.


# def car_list_view(req):
#     cars = Carlist.objects.all()

#     data = {
#         'cars': list(cars.values()),
#     }
#     return JsonResponse(data)


# def car_detail_view(req, pk):
#     car = Carlist.objects.get(pk=pk)
#     data = {
#         'name': car.name,
#         'description': car.description,
#         'active': car.active
#     }
#     return JsonResponse(data)


# Function view

@api_view(["GET", "POST"])
def car_list_view(req):
    if req.method == 'GET':
        car = Carlist.objects.all()
        serializer = CarSerializer(car, many=True)
        return Response(serializer.data)

    if req.method == 'POST':
        serializer = CarSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def car_detail_view(req, pk):
    if req.method == 'GET':
        try:
            car = Carlist.objects.get(pk=pk)
        except:
            return Response({'Error': 'Car not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CarSerializer(car)
        return Response(serializer.data)

    if req.method == 'PUT':
        car = Carlist.objects.get(pk=pk)
        serializer = CarSerializer(car, data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if req.method == 'DELETE':
        car = Carlist.objects.get(pk=pk)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Class view

class Showroom_View(APIView):
    def get(self, request):
        showroom = showroomList.objects.all()
        serializer = showroomSerializer(showroom, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = showroomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

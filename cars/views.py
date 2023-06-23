from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Car, Brand
from .serializers import CarSerializer, BrandSerializer
import json


class CarBaseView(View):
    model = Car
    fields = '__all__'
    success_url = reverse_lazy('cars:all')


class CarListView(CarBaseView, ListView):
    """View to list all cars
    """

class CarDetailView(CarBaseView, DetailView):
    """View to list the details from one car
    """

class CarCreateView(CarBaseView, CreateView):
    """View to create a new car
    """

class CarUpdateView(CarBaseView, UpdateView):
    """View to update a car
    """

class CarDeleteView(CarBaseView, DeleteView):
    """View to delete a car
    """


def update_cars_view(request):
    return render(request, 'cars/car_panel.html')


@api_view(["GET"])
def get_colors(requets):
    colors = Car.COLOR_CHOICES,
    response = [{"tag": tag, "name": name} for tag, name in colors[0]]
    return JsonResponse({'colors': response}, safe=False, status=status.HTTP_200_OK)
        


@api_view(["GET"])
def get_brands(requets):
    brands = Brand.objects.all()
    serializer = BrandSerializer(brands, many=True)
    return JsonResponse({'brands': serializer.data}, safe=False, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_cars(request):
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many=True)
    return JsonResponse({'cars': serializer.data}, safe=False, status=status.HTTP_200_OK)

@csrf_exempt
@api_view(["PUT"])
def update_cars(request):
    update_serializer = CarSerializer(data=request.data, many=True)

    if update_serializer.is_valid(raise_exception=True):
        for item in update_serializer.validated_data:
            car = Car.objects.get(id=item['id'])
            car.model = item.get("model")
            car.brand = item.get("brand")
            car.color = item.get("color")
            car.value = item.get("value")
            car.production_cost = item.get("production_cost")
            car.transportation_cost = item.get("transportation_cost")
            car.save()

    cars = Car.objects.all()
    serializer = CarSerializer(cars, many=True)
    
    return JsonResponse({'cars':serializer.data}, safe=False, status=status.HTTP_200_OK)

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import Response
from django.http.response import HttpResponse, JsonResponse
from rest_framework import status
#from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

from .models import ConjuntoModel
from .serializer import ConjuntoSerializer

#API View listar todos los datos.
@api_view(['GET'])
def Conjunto_list(request):
    try:
        if request.method == 'GET':
            conjunto = ConjuntoModel.objects.all()
            conjunto_serializer = ConjuntoSerializer(conjunto, many=True)
            return Response(conjunto_serializer.data, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

#API Vista listar un registro especifico
@api_view(['GET'])
def Conjunto_detail(request, pk):
    try:
        conjunto = ConjuntoModel.objects.get(pk = pk)
        if not conjunto.is_active:
            return Response(data={'message': 'El valor no esta activo'}, status=status.HTTP_400_BAD_REQUEST)
        
    except ConjuntoModel.DoesNotExist:
        return HttpResponse({'El valor no existe'},status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        conjunto_serializer = ConjuntoSerializer(conjunto)
        return Response(conjunto_serializer.data, status=status.HTTP_200_OK)

#API vista insertar un registro
@api_view(['POST'])
def Conjunto_insert(request):
    if request.method == 'POST':
        conjunto_data = JSONParser().parse(request)
        conjunto_serializer = ConjuntoSerializer(data=conjunto_data)
        if conjunto_serializer.is_valid():
            conjunto_serializer.save()
            return JsonResponse(conjunto_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(conjunto_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#API Vista actualiza
@api_view(['PUT'])
def Conjunto_update(request, pk):
    try:
        conjunto = ConjuntoModel.objects.get(pk = pk)
        if not conjunto.is_active:
            return Response(DATA={'message': 'El valor no esta activo'}, status=status.HTTP_400_BAD_REQUEST)
        
    except ConjuntoModel.DoesNotExist:
    #except ObjectDoesNotExist:
        return HttpResponse({'El valor no existe'},status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        conjunto_data = JSONParser().parse(request)
        conjunto_serializer = ConjuntoSerializer(conjunto, data=conjunto_data)
        if conjunto_serializer.is_valid():
            conjunto_serializer.save()
            return Response(conjunto_serializer.data, status=status.HTTP_201_CREATED)
        return Response(conjunto_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#API Vista actualiza con un patch temporal
@api_view(['GET','PATCH'])
def Conjunto_update_patch(request, pk):
    try:
        conjunto = ConjuntoModel.objects.get(pk = pk)
        if not conjunto.is_active:
            return Response(data={'message': 'El valor no esta activo'}, status=status.HTTP_400_BAD_REQUEST)
        
    except ConjuntoModel.DoesNotExist:
        return HttpResponse({'El valor no existe'},status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        conjunto_data = JSONParser().parse(request)
        conjunto_serializer = ConjuntoSerializer(conjunto, data=conjunto_data, partial=True)
        if conjunto_serializer.is_valid():
            conjunto_serializer.save()
            return Response(conjunto_serializer.data)
        return Response(conjunto_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# API Vista borrar dato
@api_view(['GET', 'DELETE'])
def Conjunto_delete(request, pk):
    try:
        conjunto = ConjuntoModel.objects.get(pk = pk)
        if not conjunto.is_active:
            return Response(data={'message': 'El valor no esta activo'}, status=status.HTTP_400_BAD_REQUEST)

    except ConjuntoModel.DoesNotExist:
    #except ObjectDoesNotExist:
        return HttpResponse({'El valor no existe'},status=status.HTTP_400_BAD_REQUEST)

    if request.method=='DELETE':
        conjunto.delete()
        return Response('El valor fue borrado', status=status.HTTP_204_NO_CONTENT)
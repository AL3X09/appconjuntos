from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import Response
from django.http.response import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

from .models import AsistenciaModel
from .serializer import AsistenciaSerializer

# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def Conjunto_view(request):

    try:
        if request.method == 'GET':
            asistencia = AsistenciaModel.objects.all()
            asistencia_serializer = AsistenciaSerializer(asistencia, many=True)
            return Response(asistencia_serializer.data, status=status.HTTP_200_OK)
            
        elif request.method == 'POST':
            asistencia_data = JSONParser().parse(request)
            asistencia_serializer = AsistenciaSerializer(data=asistencia_data)
            if asistencia_serializer.is_valid():
                asistencia_serializer.save()
                return JsonResponse(asistencia_serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse(asistencia_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method=='DELETE':
            count = asistencia.objects.all().delete()
            return JsonResponse({'message': '{} se borro correctamente todo el contenido'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

    except ObjectDoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def Conjunto_list(request):

    try:
        if request.method == 'GET':
            asistencia = AsistenciaModel.objects.all()
            asistencia_serializer = AsistenciaSerializer(asistencia, many=True)
            return Response(asistencia_serializer.data, status=status.HTTP_200_OK)
            
        elif request.method == 'POST':
            return JsonResponse({'message': '{} Metodo no existente'.format(count[0])}, status=status.HTTP_500)

        elif request.method=='DELETE':
             return JsonResponse({'message': '{} Metodo no existente'.format(count[0])}, status=status.HTTP_500)

    except ObjectDoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

# Vista listar todo
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def Conjunto_detail(request, pk):
    try:
        asistencia = AsistenciaModel.objects.get(pk = pk)
        if not asistencia.is_active:
            return Response(data={'message': 'El valor no esta activo'}, status=status.HTTP_400_BAD_REQUEST)
        
    except AsistenciaModel.DoesNotExist:
    #except ObjectDoesNotExist:
        return HttpResponse({'El valor no existe'},status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        asistencia_serializer = AsistenciaSerializer(asistencia)
        return Response(asistencia_serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        asistencia_data = JSONParser().parse(request)
        asistencia_serializer = AsistenciaSerializer(asistencia, data=asistencia_data)
        if asistencia_serializer.is_valid():
            asistencia_serializer.save()
            return Response(asistencia_serializer.data, status=status.HTTP_201_CREATED)
        return Response(asistencia_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        asistencia_data = JSONParser().parse(request)
        asistencia_serializer = AsistenciaSerializer(asistencia, data=asistencia_data, partial=True)
        if asistencia_serializer.is_valid():
            asistencia_serializer.save()
            return Response(asistencia_serializer.data)
        return Response(asistencia_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method=='DELETE':
        asistencia.delete()
        return Response('El valor fue borrado', status=status.HTTP_204_NO_CONTENT)

# Vista listar todo
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def Conjunto_update(request, pk):
    try:
        asistencia = AsistenciaModel.objects.get(pk = pk)
        if not asistencia.is_active:
            return Response(data={'message': 'El valor no esta activo'}, status=status.HTTP_400_BAD_REQUEST)
        
    except AsistenciaModel.DoesNotExist:
    #except ObjectDoesNotExist:
        return HttpResponse({'El valor no existe'},status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        asistencia_data = JSONParser().parse(request)
        asistencia_serializer = AsistenciaSerializer(asistencia, data=asistencia_data)
        if asistencia_serializer.is_valid():
            asistencia_serializer.save()
            return Response(asistencia_serializer.data, status=status.HTTP_201_CREATED)
        return Response(asistencia_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        return Response(asistencia_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   
    
    elif request.method == 'PATCH':
        return JsonResponse({'message': '{} Metodo no existente'.format(count[0])}, status=status.HTTP_500)

    elif request.method=='DELETE':
        return JsonResponse({'message': '{} Metodo no existente'.format(count[0])}, status=status.HTTP_500)

# Vista listar todo
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def Conjunto_delete(request, pk):
    try:
        asistencia = AsistenciaModel.objects.get(pk = pk)
        if not asistencia.is_active:
            return Response(data={'message': 'El valor no esta activo'}, status=status.HTTP_400_BAD_REQUEST)
        
    except AsistenciaModel.DoesNotExist:
    #except ObjectDoesNotExist:
        return HttpResponse({'El valor no existe'},status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        return JsonResponse({'message': '{} Metodo no existente'.format(count[0])}, status=status.HTTP_500)

    elif request.method == 'PUT':
        return JsonResponse({'message': '{} Metodo no existente'.format(count[0])}, status=status.HTTP_500)
    
    elif request.method == 'PATCH':
        return JsonResponse({'message': '{} Metodo no existente'.format(count[0])}, status=status.HTTP_500)

    elif request.method=='DELETE':
        asistencia.delete()
        return Response('El valor fue borrado', status=status.HTTP_204_NO_CONTENT)
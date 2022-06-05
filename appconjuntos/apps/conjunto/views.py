from sre_parse import State
#from django.shortcuts import render
#from django.views.decorators.csrf import csrf_exempt

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from django.core.exceptions import ObjectDoesNotExist
#from django.http import HttpResponse, JsonResponse
#from rest_framework.views import APIView
#from rest_framework.parsers import JSONParser
#from rest_framework.decorators import api_view

from .models import ConjuntoModel
from .serializer import ConjuntoSerializer

class ConjuntoListView(generics.ListAPIView):
    serializer_class = ConjuntoSerializer

    def get_queryset(self):
        return ConjuntoModel.objects.filter(is_active = True)

class ConjuntoCreateView(generics.CreateAPIView):
    serializer_class = ConjuntoSerializer

    def post(self, request):
        try:
            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"mensaje" : "Conjunto guradado correctamente"},status = status.HTTP_201_CREATED)
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ConjuntoDetailView(generics.RetrieveAPIView):
    serializer_class = ConjuntoSerializer
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(is_active = True)

class ConjuntoDeleteView(generics.DestroyAPIView):
    serializer_class = ConjuntoSerializer

    def get_queryset(self):
        return self.get_queryset().Meta.model.objects.filter(is_active = True)
    
    #sobreescribo el metodo para borrar de manera logica
    def delete(self, request, pk=None):
        try:
            conjunto = self.get_serializer().Meta.model.objects.filter(id = pk).First
            if conjunto:
                conjunto.is_active = False
                conjunto.save()
                return Response({"mensaje" : "Conjunto eliminado correctamente"},status = status.HTTP_200_OK)
            return Response({"Error" : "Valor no existe"},status = status.HTTP_400_BAD_REQUEST)

        except ObjectDoesNotExist:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class ConjuntoUpdateView(generics.UpdateAPIView):
    serializer_class = ConjuntoSerializer

    def get_queryset(self,pk):
        #return self.get_queryset().Meta.model.objects.filter(is_active = True) #.filter(id = pk).first()
        return self.serializer_class().Meta.model.objects.filter(is_active = True).filter(id = pk).first()
    
    #sobreescribo el metodo
    def patch(self, request, pk=None):
        try:
            if self.get_queryset(pk):
            #conjunto = self.get_queryset().filter(id = pk).first()
            #if conjunto:
            #self.get_queryset(pk):
                #conjunto_serializer = self.serializer_class(conjunto)
                conjunto_serializer = self.serializer_class(self.get_queryset(pk))
                return Response(conjunto_serializer.data ,status = status.HTTP_200_OK)
            return Response({"Error" : "Valor no existe"},status = status.HTTP_400_BAD_REQUEST)

        except ObjectDoesNotExist:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    #sobreescribo el metodo
    def put(self, request, pk=None):
        try:
            if self.get_queryset(pk):
                conjunto_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
                if conjunto_serializer.is_valid():
                    conjunto_serializer.save()
                    return Response(conjunto_serializer.data ,status = status.HTTP_200_OK)
            return Response({"Error" : "Valor no existe"},status = status.HTTP_400_BAD_REQUEST)

        except ObjectDoesNotExist:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


"""
#API View listar todos los datos.
@api_view(['GET', 'POST'])
def Conjunto_view(request):
    try:
        if request.method == 'GET':
            conjunto = ConjuntoModel.objects.all()
            conjunto_serializer = ConjuntoSerializer(conjunto, many=True)
            return Response(conjunto_serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'POST':
            conjunto_data = JSONParser().parse(request)
            conjunto_serializer = ConjuntoSerializer(data=conjunto_data)
            if conjunto_serializer.is_valid():
                conjunto_serializer.save()
                return Response(conjunto_serializer.data, status=status.HTTP_201_CREATED)
            return Response(conjunto_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
def Conjunto_insert1(request):
    if request.method == 'POST':
        conjunto_data = JSONParser().parse(request)
        print("hola" + conjunto_data).text
        conjunto_serializer = ConjuntoSerializer(data=conjunto_data)
        if conjunto_serializer.is_valid():
            conjunto_serializer.save()
            return JsonResponse(conjunto_serializer.data, status=status.HTTP_204_NO_CONTENT)
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
@api_view(['PATCH'])
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
@api_view(['DELETE'])
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
"""
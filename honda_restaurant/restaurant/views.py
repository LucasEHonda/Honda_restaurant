from django.shortcuts import render
from rest_framework import viewsets
from .models import Cooker, Recipe
from .serializers import CookerSerializer, RecipeSerializer
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.renderers import JSONRenderer
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
)
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi






class CookerViewSet(viewsets.ModelViewSet):
    serializer_class = CookerSerializer
    renderer_classes = [JSONRenderer]

    name_param_config = openapi.Parameter('name',in_=openapi.IN_QUERY,description='Cooker name to config',type=openapi.TYPE_STRING)
    
    @swagger_auto_schema(manual_parameters=[name_param_config])
    def get_queryset(self):
        queryset_list = Cooker.objects.all()
        query = self.request.GET.get("name")
        if query:
            queryset_list = queryset_list.filter(
                Q(name__icontains=query)                
            ).distinct()
        return queryset_list

    def create(self, request, *args,**kwargs):
        data = request.data
        new_cooker = Cooker.objects.create(name=data['name'])
        new_cooker.save()
        serializer = CookerSerializer(new_cooker)

        return Response(serializer.data)
        

class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    renderer_classes = [JSONRenderer]
    filter_backends = [SearchFilter]
    
    search_fields = ['name','ingredients','prepationMode','prepationTime','cooker__name'] #Atributos que o query param vai usar no 'search'

    query_params = ['name','ingredients','prepartionMode','prepationTime','cookerName'] #Query params que existe na rota '/recipe/'
    

    def get_queryset(self):
        queryset_list = Recipe.objects.all() #lista com todas as receitas
        querys = [(query_param, self.request.GET.get(query_param)) for query_param in self.query_params if self.request.GET.get(query_param)]#Verifica se o usuario esta buscando por alguma query especifica. Caso sim retorna uma lista de tupla com essa query e o  seu respectivo parametro.
        if querys: #se existir um query ele vai procurar pelo parametro que foi passado se nao ele retorna a lista com todos os parametros.
            query = querys[0][1] #sempre vai ter apenas 1 elemento nessa lista e queremos acessar o parametro passado na query.
            if querys[0][0] == 'name':#verifica qual query foi usada e procura no seu respectivo atributo se existe o parametro que foi passado.
                queryset_list = queryset_list.filter(
                    Q(name__icontains=query)                
                ).distinct()
            elif querys[0][0] == 'ingredients':
                queryset_list = queryset_list.filter(
                    Q(ingredients__icontains=query)                
                ).distinct()        
            elif querys[0][0] == 'prepartionMode':
                queryset_list = queryset_list.filter(
                    Q(prepartionMode__icontains=query)                
                ).distinct()
            elif querys[0][0] == 'prepationTime':
                queryset_list = queryset_list.filter(
                    Q(prepationTime__icontains=query)                
                ).distinct()
            elif querys[0][0] == 'cookerName':
                queryset_list = queryset_list.filter(
                    Q(cooker__name__icontains=query)                
                ).distinct()
        return queryset_list

    def create(self, request, *args,**kwargs):
        data = request.data
        new_recipe = Recipe.objects.create(name=data['name'],ingredients=data['ingredients'],prepationMode=data['prepationMode'],prepationTime=data['prepationTime'],cooker=Cooker.objects.get(name=data['cooker']['name']))
        new_recipe.save()
        serializer = RecipeSerializer(new_recipe)

        return Response(serializer.data)
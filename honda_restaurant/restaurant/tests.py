from django.test import TestCase
import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .serializers import CookerSerializer, RecipeSerializer

from .models import Cooker, Recipe
import json


class TestCookerView(APITestCase):
    
    def setUp(self):
        self.data = {'id':1,'name': 'testecase'}
        self.cooker = Cooker.objects.create(name='testecase')


    def test_cooker_registration(self):
        response = self.client.post("/cooker/", self.data)
        body = json.loads((response.content).decode())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(body['name'], self.data['name'])
        

    def test_cooker_put_sucess_status_code(self):
        url = "/cooker/{0}/".format(self.cooker.pk)
        response = self.client.put(url, self.data)
        body = json.loads((response.content).decode())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(body['name'], self.data['name'])

    def test_cooker_put_failure_data_error_status_code(self):
        url = "/cooker/{0}/".format(self.cooker.pk)
        response = self.client.put(url)
        body = json.loads((response.content).decode())
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(body['name'], ['This field is required.'])


    def test_cooker_put_failure_status_code(self):
        url = '/cooker/99/'
        response = self.client.put(url, self.data)
        body = json.loads((response.content).decode())
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(body['detail'], 'Not found.')
        
    def test_cooker_delete_success_status_code(self):
        url = '/cooker/{0}/'.format(self.cooker.pk)
        response = self.client.delete(url)
        body = (response.content).decode()
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(body, '')

    def test_cooker_delete_failure_status_code(self):
        url = '/cooker/99/'
        response = self.client.delete(url)
        body = json.loads((response.content).decode())
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)  
        self.assertEqual(body['detail'], 'Not found.')  

    def test_cooker_get_query_param_sucess_status_code(self):
        response = self.client.get('/cooker/?name=testecase')
        body = json.loads((response.content).decode())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(body[0]['id'], 1)  
        
    def test_cooker_get_sucess_status_code(self):
        response = self.client.get(reverse('cooker-detail',kwargs={"pk":1}))
        body = json.loads((response.content).decode())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(body['id'], 1)  

        
class TestRecipeView(APITestCase):
    
    def setUp(self):
        self.cooker = Cooker.objects.create(name='testecase')
        self.cooker.save()
        self.data =  json.dumps({"name":"honda","ingredients":"pao","prepationMode":"fritar","prepationTime":15,"cooker":{"id":1,"name":"testecase"}})
        self.recipe = Recipe.objects.create(name="honda",ingredients="pao",prepationMode="fritar",prepationTime=15,cooker=Cooker.objects.first())
        


    def test_recipe_registration(self):
        response = self.client.post("/recipe/", self.data,content_type="application/json")
        body = json.loads((response.content).decode())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(body['name'], "honda")
        

    def test_recipe_put_sucess_status_code(self):
        url = "/recipe/{0}/".format(self.recipe.pk)
        response = self.client.put(url, self.data,content_type="application/json")
        body = json.loads((response.content).decode())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(body['name'], "honda")

    def test_recipe_put_failure_data_error_status_code(self):
        url = "/recipe/{0}/".format(self.recipe.pk)
        response = self.client.put(url)
        body = json.loads((response.content).decode())
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(body['name'], ['This field is required.'])

    def test_recipe_put_failure_status_code(self):
        url = '/recipe/99/'
        response = self.client.put(url, self.data,content_type="application/json")
        body = json.loads((response.content).decode())
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(body['detail'], 'Not found.')

    def test_recipe_delete_success_status_code(self):
        url = '/recipe/{0}/'.format(self.recipe.pk)
        response = self.client.delete(url)
        body = (response.content).decode()
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(body, '')

    def test_recipe_delete_failure_status_code(self):
        url = '/recipe/99/'
        response = self.client.delete(url)
        body = json.loads((response.content).decode())
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)  
        self.assertEqual(body['detail'], 'Not found.')  

    def test_recipe_get_query_param_sucess_status_code(self):
        response = self.client.get('/recipe/?name=honda')
        body = json.loads((response.content).decode())       
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(body[0]['id'], 1)  

    def test_recipe_get_sucess_status_code(self):
        response = self.client.get(reverse('recipe-detail',kwargs={"pk":1}))
        body = json.loads((response.content).decode())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(body['id'], 1)  

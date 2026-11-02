from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from json import loads
from recipe_manager.models import RecipeDb

# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class RecipeListCreateView(View):
    def get(self, request):
        contacts = RecipeDb.objects.all().values()
        return JsonResponse(list(contacts), safe=False)

    def post(self, request):
        data = request.body
        fd = loads(data)

        RecipeDb.objects.create(**fd)
        return JsonResponse({"message": "Recipe added successfully!"})

@method_decorator(csrf_exempt, name='dispatch')
class RecipeRetrieveUpdateDeleteView(View):
    def get(self, request, pk):
        recipe = get_object_or_404(RecipeDb, id=pk)
        return JsonResponse({
            "id": recipe.id, 
            "recipe_name": recipe.recipe_name, 
            "ingredients": recipe.ingredients, 
            "instructions": recipe.instructions, 
            "category": recipe.category, 
            "preparation_time": recipe.preparation_time, 
            "cooking_time": recipe.cooking_time, 
            "servings": recipe.servings})

    def put(self, request, pk):
        recipe = get_object_or_404(RecipeDb, id=pk)
        data = loads(request.body)
        for field, value in data.items():
            if field == 'recipe_name':
                recipe.recipe_name = value
            elif field == 'ingredients':
                recipe.ingredients = value
            elif field == 'instructions':
                recipe.instructions = value
            elif field == 'category':
                recipe.category = value
            elif field == 'preparation_time':
                recipe.preparation_time = value
            elif field == 'cooking_time':
                recipe.cooking_time = value
            elif field == 'servings':
                recipe.servings = value
        recipe.save()
        return JsonResponse({"message": "Recipe updated successfully!"})

    def delete(self, request, pk):
        recipe = get_object_or_404(RecipeDb, id=pk)
        recipe.delete()
        return JsonResponse({"message": "Recipe deleted successfully!"})
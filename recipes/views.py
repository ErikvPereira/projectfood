from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from .models import Recipe


@login_required
def home(request):

    recipes = Recipe.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(request, 'recipes/home.html', {
        'recipes': recipes
    })
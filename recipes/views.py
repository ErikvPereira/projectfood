from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from .models import Recipe

from django.shortcuts import (
    render,
    redirect
)

from .models import (
    Recipe,
    Ingredient,
    Step
)

@login_required
def home(request):

    recipes = Recipe.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(request, 'recipes/home.html', {
        'recipes': recipes
    })


@login_required
def create_recipe(request):

    if request.method == 'POST':

        title = request.POST.get('title')

        ingredient_names = request.POST.getlist(
            'ingredient_name[]'
        )

        ingredient_quantities = request.POST.getlist(
            'ingredient_quantity[]'
        )

        steps = request.POST.getlist(
            'steps[]'
        )

        recipe = Recipe.objects.create(
            user=request.user,
            title=title
        )

        for name, quantity in zip(
            ingredient_names,
            ingredient_quantities
        ):

            if name.strip():

                Ingredient.objects.create(
                    recipe=recipe,
                    name=name,
                    quantity=quantity
                )

        for index, description in enumerate(
            steps,
            start=1
        ):

            if description.strip():

                Step.objects.create(
                    recipe=recipe,
                    order=index,
                    description=description
                )

        return redirect('home')

    return render(
        request,
        'recipes/create_recipe.html'
    )
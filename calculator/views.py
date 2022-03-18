from pprint import pprint
from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def counter(request):
    if 'omlet' in request.path:
        template = 'calculator/omlet.html'
        data = DATA['omlet']
    elif 'pasta' in request.path:
        template = 'calculator/pasta.html'
        data = DATA['pasta']
    elif 'buter' in request.path:
        template = 'calculator/buter.html'
        data = DATA['buter']
        
    reagents = dict()
    context = {}
    count = request.GET.get('servings')
    if count:
        for key, value in data.items():
            reagents[key] = round(value * int(count), 2)
            
        context['reagents'] = reagents
    else:
        for key, value in data.items():
            reagents[key] = value
            
        context['reagents'] = reagents
        
            

    
    return render(request, template, context)
    
    

    


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

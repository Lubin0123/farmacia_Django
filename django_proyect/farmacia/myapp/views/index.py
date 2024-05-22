from django.shortcuts import render

def index(request):
    context = {
        'titulo': 'Farmacia Futurista',
        'mensaje_bienvenida': '¡Bienvenido a la farmacia del futuro!'
    }
    return render(request, 'myapp/index.html', context)

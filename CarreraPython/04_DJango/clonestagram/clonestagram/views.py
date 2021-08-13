"""Local Views"""

# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime
import json


 
def hellow_world(request):
    """devuelve string con la fecha actual"""
    now  = datetime.now().strftime('%b %dth, %Y - %H:%M:%S hrs')
    return HttpResponse(f"<h1>Hola Mundo, Django</h1>Server time is {now} <br><h3>mostrando fecha en esta url</h3>")



def sorted_numeros(request):
    numbers = [ int(i) for i in request.GET['numbers'].split(',') ]
    sorted_ints = sorted(numbers)

    data = {
        'hi': "Hola care monda desde un json",
        'detalle': 'esta url recibe numeros por get y los ordena',
        'ejemplo': 'http://127.0.0.1:8000/sorted/?numbers=9,33,56,14,2,1000',
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted successfully' 
    }

    #import pdb; pdb.set_trace()
    return HttpResponse( json.dumps(data), content_type="application/json" )


def hi(request, name, age):
    
    if age > 14:
        message = f'<h2>Bienvenido a clonestagram</h2><p>Hola {name}, {age}</p><h4>recibiendo nombre y edad por get</h4>'
    else:
        message = f'Sorry {name} {age} no puede estar aquí'

    return HttpResponse(message)

"""platzigram views."""

#Django
from django.http import HttpResponse
from django.http import JsonResponse
import json

# Debugger
import pdb

# Utilities
from datetime import datetime

def hello_world(request):
    """ Return a greeting """
    return HttpResponse('Hello, the current servertime is {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
        ))

def sort_integers(request):
    """sort_integers"""
    # pdb.set_trace()
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'messages': 'Integers sorted successfully.',
    }

    return HttpResponse(
        json.dumps(data, indent=4),
        content_type='application/json'
    )

def say_hi(request, name, age):
    """ return a greeting message"""
    if age < 12:
        message = 'Sorry {}, you are not allowed here 😜'.format(name)
    else:
        message = 'Hello!!! {}, Welcome to Platzigram'.format(name)
    return HttpResponse(message)
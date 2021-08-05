""" Posts views. """
# Django
from django.shortcuts import render

# Utilities
from datetime import datetime

posts = [
    {
        'title': 'Mont Blac',
        'user': {
            'name': 'Yésica Cortéx',
            'picture': 'https://picsum.photos/200/200/?image=1027',
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/600/?image=1036'
    },
    {
        'title': 'Pink Woman',
        'user': {
            'name': 'Khe.',
            'picture': 'https://picsum.photos/id/84/200/200?image=903'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/600/?image=903'
    },
    {
        'title': 'Nautural web.',
        'user': {
            'user': 'Pancho Villa',
            'picture': 'https://picsum.photos/id/784/200/200?image=1076'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/600/?image=883'
    },
]

def list_posts(request):
    """ List existing posts. """
    return render(request, 'feed.html', {'posts': posts})
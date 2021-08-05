""" Script para agregar datos masivamente"""
from datetime import date
from posts.models import User

users = [
    {
        'email': 'cvander@platzi.com',
        'first_name': 'Christian',
        'last_name': 'Van der Henst',
        'password': '1234567',
        'is_admin': True,
        'country': 'US',
        'city': 'San Francisco',
    },
    {
        'email': 'freddier@platzi.com',
        'first_name': 'Freddy',
        'last_name': 'Vega',
        'password': '987654321',
        'country': 'US',
        'city': 'Las Vegas',
    },
    {
        'email': 'yesica@platzi.com',
        'first_name': 'Yésica',
        'last_name': 'Cortés',
        'password': 'qwerty',
        'birthday': date(1990, 12,19),
        'country': 'MX',
        'city': 'Querétaro'
    },
    {
        'email': 'arturo@platzi.com',
        'first_name': 'Arturo',
        'last_name': 'Martínez',
        'password': 'msicomputer',
        'is_admin': True,
        'birthday': date(1981, 11, 6),
        'bio': "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
        'country': 'MX',
        'city': 'Nuevo León'
    }
]

for i in users:
    print(i.get('last_name'))

for user in users:
    obj = User(**user)
    obj.save()
    print(obj.pk, ':', obj.email)


""" Como invocarlo
    python3 manage.py shell < posts/myscript.py

    #para ejecutar un archivo dentro el shell de python3:
    exec(open("name_file.py").read())
"""

""" Crear un usuario 
    from django.contrib.auth.models import User
    u = User.objects.create_user()


"""
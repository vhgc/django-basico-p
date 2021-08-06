""" User admin classes."""
# Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

# Models 
from django.contrib.auth.models import User
from users.models import Profile

# show the profile in dashboard
# admin.site.register(Profile)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """ Profile Admin."""
    # Listado de atributos para esa sección
    list_display = ('pk', 'user', 'username', 'phone_number', 'website', 'picture')
    # Listado de atributos que tendrán link para modificar perfil
    list_display_links = ('pk', 'user')
    # Campos editables directamente en la pantalla
    list_editable = (
        'phone_number', 
        'website', 
        'picture'
    )
    # Campos de búsqueda
    search_fields = (
        'user__email', 
        'user__username', 
        'user__first_name', 
        'user__last_name'
    )
    # Filtrado de datos
    list_filter = (
        'user__is_active',
        'user__is_staff',
        'created',
        'modified',
    )

    # Tuplas o renglones para el acomodo de los datos en la página visual
    fieldsets = (
        ('Profile', {
            'fields': ('user', 'picture') # Es un renglón
            # 'fields': (       # Múltiples renglones con datos en cada uno
            #     ('user', 'picture'),
            #     ('phone_number', 'website')
            # ),
        }),
        ('Extra Information!!', {
            'fields': (
                ('website', 'phone_number'),
                ('biography'),
            ),
        }),
        ('MEtaData', {
            'fields': (('created', 'modified'),),
        })

    )
    
    readonly_fields = ('created', 'modified')

# Agregamos la sección de perfil a la sección de creación de usuarios
class ProfileInLine(admin.StackedInline):
    """ Pofile in-line admin for users."""
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profiles'

class UserAdmin(BaseUserAdmin):
    """ Add profile admin to base user admin."""
    inlines = (ProfileInLine,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name', 
        'is_active',
        'is_staff'
    )


admin.site.unregister(User)
admin.site.register(User, UserAdmin) 
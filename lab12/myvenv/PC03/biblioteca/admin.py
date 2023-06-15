from django.contrib import admin

from .models import Autor, Usuario, Libro, Prestamos


class AutorAdmin(admin.ModelAdmin):
    list_display = ('IdAutor','Nombre', 'Nacionalidad')


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('IdUsuario','numUsuario', 'nif', 'Nombre', 'Direccion', 'Telefono')


class LibroAdmin(admin.ModelAdmin):
    list_display = ('IdLibro','codigo', 'titulo', 'isbn', 'editorial', 'numPags', 'autor')
    list_filter = ('editorial',)
    search_fields = ('titulo', 'autor__nombre')


class PrestamosAdmin(admin.ModelAdmin):
    list_display = ('IdPrestamo','IdLibro','IdUsuario','fecPrestamo','fecDevolucion')

    def get_IdLibro(self, obj):
        return obj.IdLibro.id

    def get_IdUsuario(self, obj):
        return obj.IdUsuario.id

    get_IdLibro.short_description = 'IdLibro'
    get_IdUsuario.short_description = 'IdUsuario'




admin.site.register(Autor,AutorAdmin)
admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(Libro,LibroAdmin)
admin.site.register(Prestamos,PrestamosAdmin)
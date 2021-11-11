from django.contrib import admin
#
from .models import Cliente, Sale, SaleDetail


class SaleAdmin(admin.ModelAdmin):
    list_display = (
        'date_sale',
        'count',
        'amount',
        'user',
        'close',
        'anulate',
    )
    list_filter = ('type_invoce', 'type_payment', 'anulate', 'user', )
    search_fields = ('user',)

class SaleDetailAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'sale',
        'count',
        'anulate',
    )
    search_fields = ('product__name',)


class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        'P_nombre',
        'P_apellido',
        'Nit',
        'Direccion',
        'Telefono',
        'Correo',
    )
    #los nombre que aparecen en el display son los nombres de los compos en el modelo
    search_fields = ('Nit', 'Telefono',)
    

#
admin.site.register(Cliente, ClienteAdmin)
#
admin.site.register(Sale, SaleAdmin)
#
admin.site.register(SaleDetail, SaleDetailAdmin)

from django import forms
from django.db.models import fields
from django.forms import widgets
#local
from .models import Sale, Cliente


class ClienteRegisterForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = (
        'P_nombre',
        'P_apellido',
        'Nit',
        'Direccion',
        'Telefono',
        'Correo',
        )
        widgets = {
            'P_nombre': forms.TextInput(
                attrs={
                    'placeholder': 'Nombres del Cliente',
                    'class': 'imput-group-field',
                }
            ),
            'P_apellido': forms.TextInput(
                attrs={
                    'placeholder': 'Apellidos del Cliente',
                    'class': 'imput-group-field',
                }
            ),
            
            'Nit': forms.TextInput(
                attrs={
                    'placeholder': 'Nit del cliente',
                    'class': 'imput-group-field',
                }
            ),
            'Direccion': forms.TextInput(
                attrs={
                    'placeholder': 'Direccion del cliente',
                    'class': 'imput-group-field',
                }
            ),
            'Telefono': forms.TextInput(
                attrs={
                    'placeholder': 'Telefono del cliente',
                    'class': 'imput-group-field',
                }
            ),
            'Correo': forms.EmailInput(
                attrs={
                    'placeholder': 'Correo elctronico del Cliente',
                    'class': 'imput-group-field',
                }
            )
        }


class ClienteUpdateForm(forms.ModelForm):
     class Meta:
         model = Cliente
         fields = (
             'P_nombre',
             'P_apellido',
             'Nit',
             'Direccion',
             'Telefono',
             'Correo',
         )
         widgets = {
            'P_nombre': forms.TextInput(
                 attrs={
                     'placeholder': 'Nombres del Cliente',
                     'class': 'imput-group-field',
                 }
             ),
             'P_apellido': forms.TextInput(
                 attrs={
                     'placeholder': 'Apellidos del Cliente',
                     'class': 'imput-group-field',
                 }
             ),
           
             'Nit': forms.TextInput(
                 attrs={
                     'placeholder': 'Nit del cliente',
                     'class': 'imput-group-field',
                 }
             ),
             'Direccion': forms.TextInput(
                 attrs={
                     'placeholder': 'Direccion del cliente',
                     'class': 'imput-group-field',
                 }
             ),
             'Telefono': forms.TextInput(
                 attrs={
                     'placeholder': 'Telefono del cliente',
                     'class': 'imput-group-field',
                 }
             ),
             'Correo': forms.EmailInput(
                 attrs={
                     'placeholder': 'Correo elctronico del Cliente',
                     'class': 'imput-group-field',
                 }
             )
         }



class VentaForm(forms.Form):
    barcode = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs = {
                'placeholder': 'Codigo de barras',
                'class': 'input-group-field',
            }
        )
    )
    count = forms.IntegerField(
        min_value=1,
        widget=forms.NumberInput(
            attrs = {
                'value': '1',
                'class': 'input-group-field',
            }
        )
    )
    #
    def clean_count(self):
        count = self.cleaned_data['count']
        if count < 1:
            raise forms.ValidationError('Ingrese una cantidad mayor a cero')

        return count
    

class VentaVoucherForm(forms.Form):

    type_payment = forms.ChoiceField(
        required=False,
        choices=Sale.TIPO_PAYMENT_CHOICES,
        widget=forms.Select(
            attrs = {
                'class': 'input-group-field',
            }
        )
    )
    type_invoce = forms.ChoiceField(
        required=False,
        choices=Sale.TIPO_INVOCE_CHOICES,
        widget=forms.Select(
            attrs = {
                'class': 'input-group-field',
            }
        )
    )
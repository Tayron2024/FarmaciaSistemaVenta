from django import forms
from .models import Pedido, DetallePedido, Sucursal, Medicamento, Cliente

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'sucursal_origen', 'sucursal_destino', 'estado']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'sucursal_origen': forms.Select(attrs={'class': 'form-control'}),
            'sucursal_destino': forms.Select(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
        }

class DetallePedidoForm(forms.ModelForm):
    class Meta:
        model = DetallePedido
        fields = ['medicamento', 'cantidad']
        widgets = {
            'medicamento': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class InventarioForm(forms.Form):
    sucursal = forms.ModelChoiceField(queryset=Sucursal.objects.all(), required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    medicamento = forms.ModelChoiceField(queryset=Medicamento.objects.all(), required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    cantidad = forms.IntegerField(min_value=1, required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['direccion', 'telefono']
        widgets = {
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
        }

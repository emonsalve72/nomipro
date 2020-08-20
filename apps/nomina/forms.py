from django import forms
from .models import Cargos, Tipo_Vinculacion, Empleado, Parafiscales, Periodo, Nomina, DetalleParafiscal, Reporte_Horas, Horas_Adicionales, Detalle_Horas


class cargoform(forms.ModelForm):
    class Meta:
        Model = Cargos
        fields = [
        'ide_cargos'
        'nombre'
        'estado'
        'valor_cargo'
    ]
    labels = {
        'ide_cargos' 
        'nombre'
        'estado'
        'valor_cargo'
    }
    widgets = {
        'ide_cargos': forms.TextInput(attrs={'class': 'form.control'}),
        'nombre': forms.TextInput(attrs={'class': 'form.control'}),
        'estado': forms.TextInput(attrs={'class': 'form.control'}),
        'valor_cargo': forms.TextInput(attrs={'class': 'form.control'}),  
    }

class tipo_vinculacionform(forms.ModelForm):
    class Meta:
        Model = Tipo_Vinculacion
        fields = [
        'ide_tipovinculacion'
        'descripciontipo'
        'estado'    
    ]
    labels = {
        'ide_tipovinculacion'
        'descripciontipo'
        'estado'
    }
    widgets = {
        'ide_tipovinculacion': forms.TextInput(attrs={'class': 'form.control'}),
        'descripciontipo': forms.TextInput(attrs={'class': 'form.control'}),
        'estado': forms.TextInput(attrs={'class': 'form.control'}),
    }

class empleadoform(forms.ModelForm):
    class Meta:
        Model = Empleado
        fields = [
        'ide_empleado'
        'nombre'
        'apellido'
        'correo'
        'telefono'
        'numero_documento'
        'tipo_documento'
        'ide_cargos'
        'ide_tipovinculacion'
        'estado'
    ]
    labels = {
         'ide_empleado'
        'nombre'
        'apellido'
        'correo'
        'telefono'
        'numero_documento'
        'tipo_documento'
        'ide_cargos'
        'ide_tipovinculacion'
        'estado'
    }
    widgets = {
        'ide_empleado': forms.TextInput(attrs={'class': 'form.control'}),
        'nombre': forms.TextInput(attrs={'class': 'form.control'}),
        'apellido': forms.TextInput(attrs={'class': 'form.control'}),
        'correo': forms.TextInput(attrs={'class': 'form.control'}),
        'telefono': forms.TextInput(attrs={'class': 'form.control'}),
        'numero_documento': forms.TextInput(attrs={'class': 'form.control'}),
        'tipo_documento': forms.TextInput(attrs={'class': 'form.control'}),
        'ide_cargos': forms.TextInput(attrs={'class': 'form.control'}),
        'ide_tipovinculacion': forms.TextInput(attrs={'class': 'form.control'}),
        'estado': forms.TextInput(attrs={'class': 'form.control'}),
    }

class parafiscalesform(forms.ModelForm):
    class Meta:
        Model = Parafiscales
        fields = [
        'ide_detalleparafiscal'
        'ide_nomina'
        'totalparafiscal'
        'ide_parafiscales'
    ]
    labels = {
        'ide_detalleparafiscal'
        'ide_nomina'
        'totalparafiscal'
        'ide_parafiscales'
    }
    widgets = {
        'ide_detalleparafiscal': forms.TextInput(attrs={'class': 'form.control'}),
        'ide_nomina': forms.TextInput(attrs={'class': 'form.control'}),
        'totalparafiscal': forms.TextInput(attrs={'class': 'form.control'}),
        'ide_parafiscales': forms.TextInput(attrs={'class': 'form.control'}),  
    }

class periodoform(forms.ModelForm):
    class Meta:
        Model = Periodo
        fields = [
        'ide_periodo'
        'anual'
        'mes'    
    ]
    labels = {
        'ide_periodo'
        'anual'
        'mes'
    }
    widgets = {
        'ide_periodo': forms.TextInput(attrs={'class': 'form.control'}),
        'anual': forms.TextInput(attrs={'class': 'form.control'}),
        'mes': forms.TextInput(attrs={'class': 'form.control'}),
    }


class nominaform(forms.ModelForm):
    class Meta:
        Model = Nomina
        fields = [
        'ide_nomina'
        'valorapagar'
        'subtotal'
        'ide_periodo' 
        'ide_empleado'
        ' '     
    ]
    labels = {
        'ide_nomina'
        'valorapagar'
        'subtotal'
        'ide_periodo' 
        'ide_empleado'
        'estado' 
    }
    widgets = {
        'ide_nomina': forms.TextInput(attrs={'class': 'form.control'}),
        'valorapagar': forms.TextInput(attrs={'class': 'form.control'}),
        'subtotal': forms.TextInput(attrs={'class': 'form.control'}),
        'ide_periodo': forms.TextInput(attrs={'class': 'form.control'}),
        'ide_empleado': forms.TextInput(attrs={'class': 'form.control'}),
        'estado': forms.TextInput(attrs={'class': 'form.control'}),
    }

class detalleparafiscalform(forms.ModelForm):
    class Meta:
        Model = DetalleParafiscal
        fields = [
        'ide_detalleparafiscal'
        'ide_nomina'
        'totalparafiscal'
        'ide_parafiscales' 
         
    ]
    labels = {
        'ide_detalleparafiscal'
        'ide_nomina'
        'totalparafiscal'
        'ide_parafiscales' 
    }
    widgets = {
        'ide_detalleparafiscal': forms.TextInput(attrs={'class': 'form.control'}),
        'ide_nomina': forms.TextInput(attrs={'class': 'form.control'}),
        'totalparafiscal': forms.TextInput(attrs={'class': 'form.control'}),
        'ide_parafiscales': forms.TextInput(attrs={'class': 'form.control'}),
     
    }

class reportehorasform(forms.ModelForm):
    class Meta:
        Model = Reporte_Horas
        fields = [
        'ide_reportehoras'
        'ide_empleado'
        'ide_periodo'
        'numerohoras' 
         
    ]
    labels = {
        'ide_reportehoras'
        'ide_empleado'
        'ide_periodo'
        'numerohoras'  
    }
    widgets = {
        'ide_reportehoras': forms.TextInput(attrs={'class': 'form.control'}),
        'ide_empleado': forms.TextInput(attrs={'class': 'form.control'}),
        'ide_periodo': forms.TextInput(attrs={'class': 'form.control'}),
        'numerohoras': forms.TextInput(attrs={'class': 'form.control'}),
     
    }

class horasadicionalesform(forms.ModelForm):
    class Meta:
        Model = Reporte_Horas
        fields = [
        'ide_horasadicionales'
        'nombre'
        'valor_porhora'
        'estado'
        'ide_reportehoras' 
         
    ]
    labels = {
        'ide_horasadicionales'
        'nombre'
        'valor_porhora'
        'estado'
        'ide_reportehoras'  
    }
    widgets = {
        'ide_horasadicionales': forms.TextInput(attrs={'class': 'form.control'}),
        'nombre': forms.TextInput(attrs={'class': 'form.control'}),
        'valor_porhora': forms.TextInput(attrs={'class': 'form.control'}),
        'estado': forms.TextInput(attrs={'class': 'form.control'}),
        'ide_reportehoras': forms.TextInput(attrs={'class': 'form.control'}),
    }

class detallehorasform(forms.ModelForm):
    class Meta:
        Model = Detalle_Horas
        fields = [
        'ide_detallehoras'
        'ide_nomina'
        'ide_horasadicionales'
        'total'
        'cantidad' 
         
    ]
    labels = {
        'ide_detallehoras'
        'ide_nomina'
        'ide_horasadicionales'
        'total'
        'cantidad'  
    }
    widgets = {
        'ide_detallehoras': forms.TextInput(attrs={'class': 'form.control'}),
        'ide_nomina': forms.TextInput(attrs={'class': 'form.control'}),
        'ide_horasadicionales': forms.TextInput(attrs={'class': 'form.control'}),
        'total': forms.TextInput(attrs={'class': 'form.control'}),
        'cantidad': forms.TextInput(attrs={'class': 'form.control'}),
    }
    
    



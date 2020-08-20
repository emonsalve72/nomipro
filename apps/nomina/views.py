from django.shortcuts import render

# Create your views here.

 #importamos las vistas genericas
from django.views.generic import ListView 
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DetailView

# Create your views here.
from apps.nomina.models import Cargos, Tipo_Vinculacion, Empleado, Parafiscales, Periodo, Nomina, DetalleParafiscal, Reporte_Horas, Horas_Adicionales, Detalle_Horas

#direccionar despues de una accion
from django.urls import reverse
#habilitar mensajes
from django.contrib import messages
#habilitar mensajes  para vistas basadas en clases
#from django.contrib.messages.views import SuccessMessageMixin
#habilitar los formularios django
from django import forms
from django.urls import reverse_lazy
from apps.nomina.forms import cargoform, tipo_vinculacionform, empleadoform, parafiscalesform 
from apps.nomina.forms import periodoform, nominaform, detalleparafiscalform, reportehorasform, horasadicionalesform, detallehorasform

class Cargolistado(ListView):
    model = Cargos 
    template_name= 'cargo/listar.html'

class CrearCargo(CreateView):
    model = Cargos
    form = cargoform
    fields = "__all__"
    success_message = 'Cargo creado de manera exitosa'
    success_url = reverse_lazy('cargo_listar')
    template_name='cargo/crear.html'
    
    #para redireccionar a pagina de inicio luego que se crea un registro

# def get_success_url(self):
#      return reverse('index.html')


class CargoDetalle(DetailView):
     model = Cargos
     

class CargoEditar(UpdateView):
    model = Cargos
    form = cargoform
    fields = "__all__"
    success_message = 'Cargo creado de manera exitosa'
    success_url = reverse_lazy('cargo_listar')
    template_name='cargo/crear.html'

    # def get_success_url(self):
    #     return reverse('index')




class listadoTipo_Vinculacion(ListView):
    model= Tipo_Vinculacion
    template_name= 'tipo_vinculacion/listartp.html'

class creartipo_vinculacion(CreateView):
    model = Tipo_Vinculacion
    form = tipo_vinculacionform
    fields = "__all__"
    success_message = 'tipo de vinculacion creado de manera exitosa'
    success_url = reverse_lazy('listar_tipovinculacion')
    template_name='tipo_vinculacion/creartp.html'

class detalletipo_vinculacion(DetailView):
     model = Tipo_Vinculacion

class editartipo_vinculacion(UpdateView):
    model = Tipo_Vinculacion
    form = tipo_vinculacionform
    fields = "__all__"
    success_message = 'tipo de vinculacion actualizado de manera exitosa'
    success_url = reverse_lazy('listar_tipovinculacion')
    template_name='tipo_vinculacion/creartp.html'

    # def get_success_url(self):
    #     return reverse('index')



    
class listadoempleado(ListView):
    model = Empleado
    template_name= 'empleado/listar.html'

class Crearempleado(CreateView):
    model = Empleado
    form = empleadoform
    fields = "__all__"
    success_message = 'empleado creado de manera exitosa'
    success_url = reverse_lazy('listar_empleado')
    template_name='empleado/crear.html'
    
    #para redireccionar a pagina de inicio luego que se crea un registro

# def get_success_url(self):
#      return reverse('index.html')


class EmpleadoDetalle(DetailView):
     model = Empleado

class EmpleadoEditar(UpdateView):
    model = Empleado
    form = empleadoform
    fields = "__all__"
    success_message = 'empleado actualizado de manera exitosa'
    success_url = reverse_lazy('listar_empleado')
    template_name='empleado/crear.html'




class listadoparafiscales(ListView):
    model = Parafiscales
    template_name= 'parafiscales/listar.html'

class Crearparafiscal(CreateView):
    model = Parafiscales
    form = parafiscalesform
    fields = "__all__"
    success_message = 'parafiscal creado de manera exitosa'
    success_url = reverse_lazy('listar_parafiscal')
    template_name='parafiscales/crear.html'
    

def get_success_url(self):
     return reverse('index.html')


class Detalleparafiscal(DetailView):
     model = Parafiscales

class ParafiscalEditar(UpdateView):
    model = Parafiscales
    form = parafiscalesform
    fields = "__all__"
    success_message = 'parafiscal actualizado de manera exitosa'
    success_url = reverse_lazy('listar_parafiscal')
    template_name='parafiscales/crear.html'



class listadoperiodo(ListView):
    model = Periodo
    template_name= 'periodo/listado.html'

class Crearperiodo(CreateView):
    model = Periodo
    form = periodoform
    fields = "__all__"
    success_message = 'periodo creado de manera exitosa'
    success_url = reverse_lazy('listar_periodo')
    template_name='periodo/crear.html'
    

# def get_success_url(self):
#      return reverse('index.html')


class Detalleperiodo(DetailView):
     model = Periodo

class PeriodoEditar(UpdateView):
    model = Periodo
    form = periodoform
    fields = "__all__"
    success_message = 'periodo actualizado de manera exitosa'
    success_url = reverse_lazy('listar_periodo')
    template_name='periodo/crear.html'



class listadonomina(ListView):
    model = Nomina
    template_name= 'nomina/listar.html'

class Crearnomina(CreateView):
    model = Nomina
    form = nominaform
    fields = "__all__"
    success_message = 'nomina creada de manera exitosa'
    success_url = reverse_lazy('listar_nomina')
    template_name='nomina/crear.html'
    

# def get_success_url(self):
#      return reverse('index.html')


class Detallenomina(DetailView):
     model = Nomina

class NominaEditar(UpdateView):
    model = Nomina
    form = nominaform
    fields = "__all__"
    success_message = 'nomina actualizada de manera exitosa'
    success_url = reverse_lazy('listar_nomina')
    template_name='nomina/crear.html'



class listadodetalleparafiscal(ListView):
    model = DetalleParafiscal
    template_name= 'detalleparafiscal/listar.html'


class Creardetalleparafiscal(CreateView):
    model = DetalleParafiscal
    form = detalleparafiscalform
    fields = "__all__"
    success_message = 'detalle parafiscal creado de manera exitosa'
    success_url = reverse_lazy('listar_detalleparafiscal')
    template_name='detalleparafiscal/crear.html'
    

# def get_success_url(self):
#      return reverse('index.html')


class DetalleParafiscaldetalle(DetailView):
     model = DetalleParafiscal

class DetalleparafiscalEditar(UpdateView):
    model = DetalleParafiscal
    form = detalleparafiscalform
    fields = "__all__"
    success_message = 'detalleparafiscal actualizado de manera exitosa'
    success_url = reverse_lazy('listar_detalleparafiscal')
    template_name='detalleparafiscal/crear.html'


class listadoreportehoras(ListView):
    model = Reporte_Horas
    template_name= 'reportehoras/listar.html'


class CrearReportehoras(CreateView):
    model = Reporte_Horas
    form = reportehorasform
    fields = "__all__"
    success_message = 'detalle parafiscal creado de manera exitosa'
    success_url = reverse_lazy('listar_reportehoras')
    template_name='reportehoras/crear.html'
    

# def get_success_url(self):
#      return reverse('index.html')


class DetalleReportehoras(DetailView):
     model = Reporte_Horas

class ReportehorasEditar(UpdateView):
    model = Reporte_Horas
    form = reportehorasform
    fields = "__all__"
    success_message = 'detalleparafiscal actualizado de manera exitosa'
    success_url = reverse_lazy('listar_horasadicionales')
    template_name='reportehoras/crear.html'

class listadohorasadicionales(ListView):
    model = Horas_Adicionales
    template_name= 'horasadicionales/listar.html'


class Crearhorasadicionales(CreateView):
    model = Horas_Adicionales
    form = horasadicionalesform
    fields = "__all__"
    success_message = 'horas adicionales creadas de manera exitosa'
    success_url = reverse_lazy('listar_horasadicionales')
    template_name='horasadicionales/crear.html'
    

# def get_success_url(self):
#      return reverse('index.html')


class Detallehorasadicionales(DetailView):
     model = Horas_Adicionales

class horasadicionalesEditar(UpdateView):
    model = Horas_Adicionales
    form = horasadicionalesform
    fields = "__all__"
    success_message = 'horas adicionales actualizadas de manera exitosa'
    success_url = reverse_lazy('listar_detallehoras')
    template_name='horasadicionales/crear.html'


class listadodetallehoras(ListView):
    model = Detalle_Horas
    template_name= 'detallehoras/listar.html'


class Creardetallehoras(CreateView):
    model = Detalle_Horas
    form = detallehorasform
    fields = "__all__"
    success_message = 'detalle horas creadas de manera exitosa'
    success_url = reverse_lazy('listar_detallehoras')
    template_name='detallehoras/crear.html'
    

# def get_success_url(self):
#      return reverse('index.html')


class Detalledetallehoras(DetailView):
     model = Detalle_Horas

class detallehorasEditar(UpdateView):
    model = Detalle_Horas
    form = detallehorasform
    fields = "__all__"
    success_message = 'detalle horas actualizadas de manera exitosa'
    success_url = reverse_lazy('listar_detallehoras')
    template_name='detallehoras/crear.html'







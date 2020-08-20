
from django.conf.urls import url, include
from apps.nomina.views import Cargolistado, CrearCargo, CargoEditar, CargoDetalle
from apps.nomina.views import listadoTipo_Vinculacion, creartipo_vinculacion, detalletipo_vinculacion, editartipo_vinculacion
from apps.nomina.views import listadoempleado, Crearempleado, EmpleadoDetalle, EmpleadoEditar
from apps.nomina.views import listadoparafiscales, Crearparafiscal, Detalleparafiscal, ParafiscalEditar
from apps.nomina.views import listadoperiodo, Crearperiodo, Detalleperiodo, PeriodoEditar
from apps.nomina.views import listadonomina, Crearnomina, Detallenomina, NominaEditar
from apps.nomina.views import listadodetalleparafiscal, Creardetalleparafiscal, DetalleParafiscaldetalle, DetalleparafiscalEditar
from apps.nomina.views import listadoreportehoras, CrearReportehoras, DetalleReportehoras, ReportehorasEditar
from apps.nomina.views import listadohorasadicionales, Crearhorasadicionales, Detallehorasadicionales, horasadicionalesEditar
from apps.nomina.views import listadodetallehoras, Creardetallehoras, Detalledetallehoras, detallehorasEditar
from django.contrib import admin
from django.contrib.auth.decorators import login_required

urlpatterns = [
      url(r'^admin/', admin.site.urls),
      url(r'^cargo/listar/$', Cargolistado.as_view(), name='cargo_listar'),
      url(r'^cargo/editar/(?P<pk>\d+)/$', CargoEditar.as_view(), name='cargo_editar'), 
      url(r'^cargo/crear/$', CrearCargo.as_view(), name='cargo_crear'),
      url(r'^cargo/detalle/$', CargoDetalle.as_view(), name='cargo_detalle'),

      url(r'^listar_tipovinculacion/$', listadoTipo_Vinculacion.as_view(), name='listar_tipovinculacion'),
      url(r'^crear_tipovinculacion/$', creartipo_vinculacion.as_view(), name='crear_tipovinculacion'),
      url(r'^detalle_tipovinculacion/$', detalletipo_vinculacion.as_view(), name='detalle_tipovinculacion'),
      url(r'^editar_tipovinculacion/(?P<pk>\d+)/$', editartipo_vinculacion.as_view(), name='editar_tipovinculacion'),

      url(r'^listar_empleado/$', listadoempleado.as_view(), name='listar_empleado'),
      url(r'^crear_empleado/$', Crearempleado.as_view(), name='crear_empleado'),
      url(r'^detalle_empelado/$', EmpleadoDetalle.as_view(), name='detalle_empleado'),
      url(r'^empleado_editar/(?P<pk>\d+)/$', EmpleadoEditar.as_view(), name='empleado_editar'),

      url(r'^listar_parafiscal/$', listadoparafiscales.as_view(), name='listar_parafiscal'),
      url(r'^crear_parafiscal/$', Crearparafiscal.as_view(), name='crear_parafiscal'),
      url(r'^detalle_parafiscal/$', Detalleparafiscal.as_view(), name='detalle_parafiscal'),
      url(r'^editar_parafiscal/(?P<pk>\d+)/$', ParafiscalEditar.as_view(), name='editar_parafiscal'),

      url(r'^listar_periodo/$', listadoperiodo.as_view(), name='listar_periodo'),
      url(r'^crear_periodo/$', Crearperiodo.as_view(), name='crear_periodo'),
      url(r'^detalle_periodo/$', Detalleperiodo.as_view(), name='detalle_periodo'),
      url(r'^periodo_editar/(?P<pk>\d+)/$', PeriodoEditar.as_view(), name='periodo_editar'),

      url(r'^listar_nomina/$', listadonomina.as_view(), name='listar_nomina'),
      url(r'^crear_nomina/$', Crearnomina.as_view(), name='crear_nomina'),
      url(r'^detalle_nomina/$', Detallenomina.as_view(), name='detalle_nomina'),
      url(r'^editar_nomina/(?P<pk>\d+)/$', NominaEditar.as_view, name='editar_nomina'),

      url(r'^listar_detalleparafiscal/$', listadodetalleparafiscal.as_view(), name='listar_detalleparafiscal'),
      url(r'^crear_detalleparafiscal/$', Creardetalleparafiscal.as_view(), name='crear_detalleparafiscal'),
      url(r'^detalle_detalleparafiscal/$', DetalleParafiscaldetalle.as_view(), name='detalle_detalleparafiscal'),
      url(r'^editar_detalleparafiscal/(?P<pk>\d+)/$', DetalleparafiscalEditar.as_view, name='editar_detalleparafiscal'),
      
      url(r'^listar_reportehoras/$', listadoreportehoras.as_view(), name='listar_reportehoras'),
      url(r'^crear_reportehoras/$', CrearReportehoras.as_view(), name='crear_reportehoras'),
      url(r'^detalle_reportehoras/$',  DetalleReportehoras.as_view(), name='detalle_reportehoras'),
      url(r'^editar_dreportehoras/(?P<pk>\d+)/$', ReportehorasEditar.as_view, name='editar_reportehoras'),

      url(r'^listar_horasadicionales/$', listadohorasadicionales.as_view(), name='listar_horasadicionales'),
      url(r'^crear_horasadicionales/$', Crearhorasadicionales.as_view(), name='crear_horasadicionales'),
      url(r'^detalle_horasadicionales/$',  Detallehorasadicionales.as_view(), name='detalle_horasadicionales'),
      url(r'^editar_horasadicionales/(?P<pk>\d+)/$', horasadicionalesEditar.as_view, name='editar_horasadicionales'),
     
      url(r'^listar_detallehoras/$', listadodetallehoras.as_view(), name='listar_detallehoras'),
      url(r'^crear_detallehoras/$', Crearhorasadicionales.as_view(), name='crear_detallehoras'),
      url(r'^detalle_detallehoras/$',  Detalledetallehoras.as_view(), name='detalle_detallehoras'),
      url(r'^editar_detallehoras/(?P<pk>\d+)/$', detallehorasEditar.as_view, name='editar.detallehoras'),
]
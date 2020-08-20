"""bdnomipro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib import admin
from django.conf.urls import url, include
from apps.nomina.views import Cargolistado, listadoTipo_Vinculacion, listadoempleado, listadoparafiscales, listadoperiodo
from apps.nomina.views import listadonomina, listadodetalleparafiscal, listadoreportehoras, listadohorasadicionales, listadodetallehoras
from django.contrib.auth.views import LoginView, logout_then_login, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^cargo/', include('apps.nomina.urls')),
    url(r'^tipo_vinculacion/', include('apps.nomina.urls')),
    url(r'^empleado/', include('apps.nomina.urls')),
    url(r'^parafiscales/', include('apps.nomina.urls')),
    url(r'^periodo/', include('apps.nomina.urls')),
    url(r'^nomina/', include('apps.nomina.urls')),
    url(r'^detalleparafiscal/', include('apps.nomina.urls')),
    url(r'^listadoreportehoras/', include('apps.nomina.urls')),
    url(r'^listadohorasadicionales/', include('apps.nomina.urls')),
    url(r'^listadodetallehoras/', include('apps.nomina.urls')),
    url(r'^nomipro/', include('apps.nomina.urls')),
    url(r'^usuario/', include('apps.usuario.urls')),
    url(r'^$', LoginView.as_view(template_name='usuario/index.html'), name='login'),
        url(r'^logout', logout_then_login, name='logout'),
    url(r'^reset/password_reset/$', PasswordResetView.as_view(template_name='registration/password_reset_form.html',
        email_template_name='registration/password_reset_email.html'), 
        name='password_reset'),
    url(r'^reset/password_resetDone/$', PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'^reset/password_resetComplete/$', PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
        name='password_reset_complete'),
    

    
       #path('admin/', admin.site.urls),
    #creamos las rutas para listar todos los modelos de nomina
    #path('cargo/', CrearCargo.as_view(template_name = "cargo/crear.html"), name='cargo'),
    #path('cargo/listado', Cargolistado.as_view(template_name= "cargo/index.html")),
    # path('nomina/detalle', CargoDetalle.as_view(template_name= "nomina/detalle.html")),
    # path('nomina/actualizar', CargoActualizar.as_view(template_name= "nomina/actualizar.html")),
]

from django.db import models
from django.utils import timezone

# Create your models here.

class Cargos(models.Model):
    ide_cargos=models.CharField(max_length=50,primary_key=True)
    nombre=models.CharField(max_length=50) 
    estado=models.CharField( max_length=50)
    valor_cargo=models.FloatField()    


class Tipo_Vinculacion(models.Model):
    
    ide_tipovinculacion=models.CharField(max_length=50,primary_key=True)
    descripciontipo=models.CharField(max_length=50)
    estado=models.CharField(max_length=50)

class Empleado(models.Model):
    ide_empleado=models.CharField(max_length=50,primary_key=True)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    correo=models.EmailField()
    telefono=models.CharField(max_length=20)
    numero_documento=models.CharField(max_length=50)
    tipo_documento=models.CharField(max_length=50)
    ide_cargos=models.ForeignKey(Cargos,null=True,blank=True,on_delete=models.CASCADE)
    ide_tipovinculacion=models.ForeignKey(Tipo_Vinculacion,null=True,blank=True,on_delete=models.CASCADE)
    estado=models.CharField(max_length=50)

class Parafiscales(models.Model):
    ide_parafiscales=models.CharField(max_length=50,primary_key=True) 
    nombre=models.CharField( max_length=50)
    valor=models.CharField(max_length=50) 
    estado=models.CharField(max_length=50)
    ide_tipovinculacion=models.ForeignKey(Tipo_Vinculacion,null=True,blank=True,on_delete=models.CASCADE)

class Periodo(models.Model):
    ide_periodo=models.CharField(max_length=50,primary_key=True)
    anual=models.CharField(max_length=50)
    mes=models.CharField(max_length=50)

def __str__(self):
       return'{} {}'.format(str(self.ide_periodo,self.anual))

class Nomina(models.Model):
    ide_nomina=models.CharField(max_length=50,primary_key=True)
    valorapagar=models.FloatField()
    subtotal=models.FloatField()
    ide_periodo=models.ForeignKey(Periodo,null=True,blank=True,on_delete=models.CASCADE)
    ide_empleado=models.ForeignKey(Empleado,null=True,blank=True,on_delete=models.CASCADE)
    estado=models.CharField(max_length=50)

class DetalleParafiscal(models.Model):
        
    ide_detalleparafiscal=models.CharField(max_length=50,primary_key=True)
    ide_nomina=models.ForeignKey(Nomina,null=True,blank=True,on_delete=models.CASCADE)
    totalparafiscal=models.FloatField()
    ide_parafiscales=models.ForeignKey(Parafiscales,null=True,blank=True,on_delete=models.CASCADE)


class Reporte_Horas(models.Model):
    ide_reportehoras=models.CharField(max_length=50,primary_key=True)
    ide_empleado=models.ForeignKey(Empleado,null=True,blank=True,on_delete=models.CASCADE) 
    ide_periodo=models.ForeignKey(Periodo,null=True,blank=True,on_delete=models.CASCADE)
    numerohoras=models.IntegerField() 

class Horas_Adicionales(models.Model):
    ide_horasadicionales=models.CharField(max_length=50,primary_key=True)
    nombre=models.CharField(max_length=50)
    valor_porhora=models.FloatField()
    estado=models.CharField(max_length=50)
    ide_reportehoras=models.ForeignKey(Reporte_Horas,null=True,blank=True,on_delete=models.CASCADE)

class Detalle_Horas(models.Model):
    ide_detallehoras=models.CharField(max_length=50, primary_key=True) 
    ide_nomina=models.ForeignKey(Nomina,null=True,blank=True,on_delete=models.CASCADE)
    ide_horasadicionales=models.ForeignKey(Horas_Adicionales,null=True,blank=True,on_delete=models.CASCADE)
    total=models.IntegerField()
    cantidad=models.IntegerField()
    
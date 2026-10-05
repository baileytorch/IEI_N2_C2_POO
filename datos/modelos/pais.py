from peewee import SQL,Model, AutoField, CharField, IntegerField
from datos.conexion import conectar
from auxiliares.datos_app import defecto

base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos

class Pais(BaseModel):
    id_pais = AutoField()
    pais = CharField(max_length=50)
    nacionalidad = CharField(max_length=50, null=True)
    iso2 = CharField(max_length=2)
    iso3 = CharField(max_length=3)
    habilitado = IntegerField(constraints=[SQL(defecto)])

    class Meta:
        table_name = 'paises'
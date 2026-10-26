from peewee import Model,AutoField,CharField,IntegerField,SQL,DateField
from datos.conexion import conectar
from auxiliares.datos_app import defecto

base_datos = conectar()

class BaseModel(Model):
    class Meta:
        database = base_datos

class Usuario(BaseModel):
    id_usuario = AutoField()
    rut = CharField(max_length=12, unique=True)
    nombre = CharField(max_length=25, null=False)
    apellido = CharField(max_length=25, null=False)
    correo = CharField(max_length=191)
    pais = IntegerField(index=True)
    fecha_nacimiento = DateField()
    genero = IntegerField(null=False)
    fecha_incorporacion = DateField(null=False)
    habilitado = IntegerField(constraints=[SQL(defecto)])
    password = CharField(max_length=60, null=True)
    
    class Meta:
        table_name = 'usuarios'
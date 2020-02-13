from django.db import models

# Create your models here.

class Jugador(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    nick=models.CharField(max_length=50)
    email=models.EmailField()
    telefono=models.CharField(max_length=20)
    distrito=models.CharField(max_length=100,choices= 
    (('Comas','Comas'),('Los Olivos','Los Olivos'), ('San Martín de Porres','San Martín de Porres')))
    posicion=models.CharField(max_length=20,choices= 
    (('Arco','Arco'), ('Defensa','Defensa'),('Mediocampo','Mediocampo'),('Ataque','Ataque')))
    descripcion=models.TextField()
    password=models.CharField(max_length=156)
    def  __str__(self):
        return self.nick

class Cancha(models.Model):
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=200)
    distrito=models.CharField(max_length=100,choices= 
    (('Comas','Comas'),('Los Olivos','Los Olivos'), ('San Martín de Porres','San Martín de Porres')))
    telefono=models.CharField(max_length=20,name='Teléfono')
    ubicacion=models.CharField(max_length=100,name='Ubicación')
    costoHora=models.DecimalField(decimal_places=2,max_digits=6,name='Costo por hora')
    jugadoresMaximos=models.IntegerField(name='Jugadores por equipo')
    def  __str__(self):
        return self.nombre

class Juego(models.Model):
    estado=models.CharField(max_length=100,choices= 
    (('Activo','Activo'),('Realizado','Realizado'), ('Cancelado','Cancelado')))
    #organizador=models.ForeignKey(Jugador,on_delete=models.CASCADE)
    fecha=models.DateField()
    hora=models.TimeField()
    cancha=models.ForeignKey(Cancha,on_delete=models.CASCADE)
    jugador=models.ManyToManyField(Jugador)
    descripcion=models.TextField(null=True)

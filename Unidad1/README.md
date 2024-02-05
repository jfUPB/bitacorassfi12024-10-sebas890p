# Bitácora de aprendizaje
## Semana 2 
## Clase29-01

Empezamos la sesion de clase con una explicación del profesor sobre el reto de la unidad y nos brindo informacion y ayuda de como resolverlo, entre esas ayudas estan unas preguntas, las cuales realice y son las siguientes:
¿Cómo se leen los pulsadores A y B?
Cada boton se puede programar para que lea señales de entrada de forma independiente que es la forma que necesitamos para llevar a cabo el reto de la bomba, aunque si se requiere estos pulsadores A y B tambien pueden leer señales de forma simultaneas.

¿Cómo se leen el botón virtual que está en el logo del micro:bit?
Este boton funciona igual que los pulsadores A y B pero en vez de pulsar este es tactil, este boton se programara para al momento de tocarlo se arme la bomba.
![image](https://github.com/jfUPB/bitacorassfi12024-10-sebas890p/assets/110270011/adac006e-3000-4ae5-b2d1-24475c4ee730)
en esta imegen se puede tomar como un ejemplo breve de como seria la logica, cada pulsador estaria programado para realizar una funcion.

¿Cómo se lee y se envia información serial que llega al micro:bit?
investigando encontre que la informacion serial que llega al microbit se puede leer mediante la funcion On_data_received, esta funcion se puede adaptar para que lea la informacion serial cada vez que se reciba informacion y asi manejar la informacion serial de los comandos especificos para que se envien a web serial terminal.

![image](https://github.com/jfUPB/bitacorassfi12024-10-sebas890p/assets/110270011/0695913f-48f7-4e12-83f6-f61751a49282)


¿Cómo dibujar en la pantalla de LED?
en la pantalla led se puede dibujar de la suguiente forma, esta funciona con una matriz 5x5 la cual cada led tiene una ubicacion en la matriz, por ejemplo, si queremos que el primer led se prenda debemos usar la funcion Display.show y crear la matriz 5x5 y colocaremos un 9 en la primera ubicacion del lado superior de la matriz, se coloca un nueve porque esta es la intesidad de brillo del led, siendo 0 el brillo mas bajo y 9 el mas alto como lo muestro en la siguiente imagen:

![image](https://github.com/jfUPB/bitacorassfi12024-10-sebas890p/assets/110270011/d1f4d4e2-8f20-47ff-9923-964f37be1a8d)


¿Cómo hacer para producir sonidos con el speaker?
para poder reproducir musica en el speaker se debe usar la funcion Music.play, luego se puede programar de muchas formas como que emita un sonido al momento de presionar algun boton o que se produzca cuando la cuenta regresiva llegue a 0 que es la que necesito para el reto de la bomba. 
![image](https://github.com/jfUPB/bitacorassfi12024-10-sebas890p/assets/110270011/a0e6dd17-4a0b-4ceb-a5f5-0a220a7f5ad0)

¿Qué es una máquina de estados y cuales son sus eventos?
Una maquina de estado es la condicion que esta cumpliendo algo en el momento o como su palabra lo dice es el estado que esta realizando, esta maquina divide los distintos estados de comportamiento del programa en un determinado tiempo, teniendo en cuenta el reto, cada estado seria cuando :

Estado de Configuración: La bomba inicia en este estado  
Estado Armado (Armed): Cuando el pulsador ARMED es presionado  
Estado Explotado (Exploded): Cuando la cuenta regresiva llega a cero  
Estado Desactivado (Disarmed): Si el código de desarmado correcto se ingresa  



¿Qué son las acciones?

Las acciones son las funciones o operaciones que se realizan cuando se produce una transicion entre estados en la maquina de estados.


¿Cuáles son los estados, eventos y acciones en el reto propuesto?

los estados son :

Estado de Configuración: La bomba inicia en este estado  
Estado Armado (Armed): Cuando el pulsador ARMED es presionado  
Estado Explotado (Exploded): Cuando la cuenta regresiva llega a cero  
Estado Desactivado (Disarmed): Si el código de desarmado correcto se ingresa  

las acciones son:
aumentar_tiempo() y disminuir_tiempo(): Estas acciones se ejecutan cuando los pulsadores UP o DOWN son presionados en el estado de configuración  






## Clase 31-01

En esta sesion el profesor nos indico que iba a ser mas de trabajo autonomo, que aprovecharamos a trabajar en las preguntas, por lo que continuo respondiendo las preguntas que me hacian falta. 


¿Cómo es posible estructurar una aplicación usando una máquina de estados para poder atender varios eventos de manera concurrente?

Al usar una maquina de estados para estructurar una aplicacion estamos comenzando con pie derecho su realizacion, ya que la maquina de estado nos permite gestionar de una forma mas efectiva este estructuramiento de la siguiente manera:

nos permite identificar eventos, estados y acciones que pueden ocurrir en nuestra aplicacion adelantandonos a posibles errores a futuro.


¿Cuáles son los eventos que pueden ocurrir de manera simultánea en el problema planteado en el reto?

hay varios eventos que pueden ocurrir de manera simultánea debido al funcionamiento del reto y como lo maneje el usuario:

Uno podria ser cuando el usario presionar los pulsadores UP y DOWN al mismo tiempo,  es posible que se genere una entrada simultanea y esto altere el funcionamiento adecuada 


Presionar el botón ARMED mientras se configura el tiempo:


Si un usuario decide armar la bomba mientras está en el modo de configuración , ambas acciones deben ser manejadas simultáneamente para evitar conflictos en la lógica de control.


Cambios en la configuración mientras la bomba está armada:

Si la bomba está armada y el usuario decide ajustar el tiempo de configuración, estos cambios deben ser manejados de manera adecuada para evitar problemas y garantizar un correcto funcionamiento del estado de la aplicación.

Llegada de eventos seriales (u, d, a) mientras ocurren otras acciones:

Los eventos seriales pueden ocurrir en cualquier momento, incluso mientras se están llevando a cabo otras operaciones, como la cuenta regresiva o la configuración de tiempo. La aplicación debe ser capaz de procesar estos eventos de manera simultánea.

Inicio de la cuenta regresiva y configuración de tiempo al mismo tiempo:

Un usuario podría intentar armar la bomba y ajustar el tiempo al mismo tiempo.

## Trabajo autonomo 

Como trabajo autonomo en casa me plantee hacer el punto 13 que es un ejercicio propuesto por el profesor que es el siguiente:


Construye una aplicación que muestre en la pantalla de LED dos imágenes diferentes que se alternarán cada 2 segundos, pero sin usar la función bloqueante sleep(). Investiga las funciones ticks_ms() y ticks_diff() de la biblioteca utime. ¿Cómo puedes utilizar las dos funciones anteriores para resolver el problema de las imágenes que alternan?

tick_ms() funciona para devolver el tiempo en milisegundos y tick_diff() para calcular la diferencia de tiempo entre 2 momentos, con esta funcion calcularemos cuanto tiempo a pasado al iniciar y al finalizar algo. 


``` phyton
from microbit import *

def ticks_ms():
    return running_time()

def ticks_diff(tinicial, tfinal):
    return tfinal - tinicial


image1 = Image.HAPPY
image2 = Image.SAD

tiempo_entre_imagenes = 2000

tiempo_referencia = ticks_ms()

while True:
    
    tiempo_actual = ticks_ms()
    tiempo_transcurrido = ticks_diff(tiempo_referencia, tiempo_actual)

    
    if tiempo_transcurrido >= tiempo_entre_imagenes:
       
        display.show(image1)
        
        
        tiempo_referencia = ticks_ms()

       
        while ticks_diff(tiempo_actual, ticks_ms()) < tiempo_entre_imagenes / 2:
            pass

    
        display.show(image2)
        
    
        tiempo_referencia = ticks_ms()

        
        while ticks_diff(tiempo_referencia, ticks_ms()) < tiempo_entre_imagenes / 2:
            pass

```


https://github.com/jfUPB/bitacorassfi12024-10-sebas890p/assets/110270011/fa2cc2f4-9c0e-4415-a01d-63f396893ea9


## Semana 3 
##  Clase 5-02

En esta sesion el profesor se dedico la 1ra mitad de la clase a retroalimenta las bitacoras de los estudiantes, por lo que decidi tomarme esta sesion para hacer el punto de la actividad guia que se trata de analizar el siguiente ejemplo para contestar las 2 preguntas prpuestas.

Cómo funciona este ejemplo?

¿Qué relación tiene este ejemplo con las preguntas guía?


```py
from microbit import *
import utime

class Pixel:
    def __init__(self,pixelX,pixelY,initState,interval):
        self.state = "Init"
        self.startTime = 0
        self.interval = interval
        self.pixelX = pixelX
        self.pixelY = pixelY
        self.pixelState = initState

    def update(self):

        if self.state == "Init":
            self.startTime = utime.ticks_ms()
            self.state = "WaitTimeout"
            display.set_pixel(self.pixelX,self.pixelY,self.pixelState)

        elif self.state == "WaitTimeout":
            currentTime = utime.ticks_ms()
            if utime.ticks_diff(currentTime,self.startTime) > self.interval:
                self.startTime = currentTime
                if self.pixelState == 9:
                    self.pixelState = 0
                else:
                    self.pixelState = 9
                display.set_pixel(self.pixelX,self.pixelY,self.pixelState)

pixel1 = Pixel(0,0,0,1000)
pixel2 = Pixel(4,4,0,500)
while True:
    pixel1.update()
    pixel2.update()
```

En el codigo anterior me doy cuenta que inicia importando la biblioteca de funciones de Utime que sirve para medir intervalos de tiempo y retrasos, lo cual necesita este codigo para medir de forma exacta los intervalos de tiempo usando la funcion tick_diff para medirlos en milisegundos como pude observar en las ultimas lineas del codigo donde pixel1 tiene un tiempo de 1000 milisegundos y pixel2 tiene un tiempo de 500 milisegundos, tambien usa la funcion tick_ms para medir el tiempo inicial del programa y el tiempo actual.

este puntos no tiene alguna relacion directamente con las preguntas pero si con el punto 13 que es contruir una aplicacion usando funciones de Utime, al momento de resolver este punto investigue las funciones requeridas por lo que entiendo mejor su funcionamiento, a la vez tambien se pueden tener en cuenta estas funciones para programar el reto de la unidad, ya que se puede usar tick_diff para tener el tiempo en milisegundos y tick_ms para calcular el tiempo que ha pasado y asi hacer que la bomba explote cuando terminen los segundos. 



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

¿Qué es una máquina de estados?
Una maquina de estado es la condicion que esta cumpliendo algo en el momento o como su palabra lo dice es el estado que esta realizando, esta maquina divide los distintos estados de comportamiento del programa en un determinado tiempo, teniendo en cuenta el reto, cada estado seria cuando :

Estado de Configuración: La bomba inicia en este estado  
Estado Armado (Armed): Cuando el pulsador ARMED es presionado  
Estado Explotado (Exploded): Cuando la cuenta regresiva llega a cero  
Estado Desactivado (Disarmed): Si el código de desarmado correcto se ingresa  

¿Qué son eventos en una máquina de estados?

¿Qué son las acciones?

¿Cuáles son los estados, eventos y acciones en el reto propuesto?

¿Cómo es posible estructurar una aplicación usando una máquina de estados para poder atender varios eventos de manera concurrente?

¿Cuáles son los eventos que pueden ocurrir de manera simultánea en el problema planteado en el reto?

Construye una aplicación que muestre en la pantalla de LED dos imágenes diferentes que se alternarán cada 2 segundos, pero sin usar la función bloqueante sleep(). Investiga las funciones `ticks_ms()` y ticks_diff() de la biblioteca utime. ¿Cómo puedes utilizar las dos funciones anteriores para resolver el problema de las imágenes que alternan?

Ejemplo de un código en python:

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



## Clase 31-01

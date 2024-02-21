|# Bitácora de aprendizaje

## SEMANA 2 

### Sesión 1: lunes enero 29

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

### Sesión 2 miércoles enero 31

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

### Sesión 3 fecha?

Como trabajo autonomo en casa me plantee hacer el punto 13 que es un ejercicio propuesto por el profesor que es el siguiente:

Construye una aplicación que muestre en la pantalla de LED dos imágenes diferentes que se alternarán cada 2 segundos, pero sin usar la función bloqueante sleep(). Investiga las funciones ticks_ms() y ticks_diff() de la biblioteca utime. ¿Cómo puedes utilizar las dos funciones anteriores para resolver el problema de las imágenes que alternan?

tick_ms() funciona para devolver el tiempo en milisegundos y tick_diff() para calcular la diferencia de tiempo entre 2 momentos, con esta funcion calcularemos cuanto tiempo a pasado al iniciar y al finalizar algo. 


```py
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

Esto es un video mostrando el resultado del código:

https://github.com/jfUPB/bitacorassfi12024-10-sebas890p/assets/110270011/fa2cc2f4-9c0e-4415-a01d-63f396893ea9


## SEMANA 3

### Sesión 1 lunes febrero 2

#### Micro-sesión 1: apertura.

En esta sesion el profesor se dedico la clase a retroalimenta las bitacoras de los estudiantes, por lo que decidi tomarme esta sesion para hacer el punto de la actividad guia que se trata de analizar el siguiente ejemplo para contestar las 2 preguntas propuestas.

#### Micro-sesión 2

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

#### Micro-sesión 3

En el codigo anterior me doy cuenta que inicia importando la biblioteca de funciones de Utime que sirve para medir intervalos de tiempo y retrasos, lo cual necesita este codigo para medir de forma exacta los intervalos de tiempo usando la funcion tick_diff para medirlos en milisegundos como pude observar en las ultimas lineas del codigo donde pixel1 tiene un tiempo de 1000 milisegundos y pixel2 tiene un tiempo de 500 milisegundos, tambien usa la funcion tick_ms para medir el tiempo inicial del programa y el tiempo actual.

este puntos no tiene alguna relacion directamente con las preguntas pero si con el punto 13 que es contruir una aplicacion usando funciones de Utime, al momento de resolver este punto investigue las funciones requeridas por lo que entiendo mejor su funcionamiento, a la vez tambien se pueden tener en cuenta estas funciones para programar el reto de la unidad, ya que se puede usar tick_diff para tener el tiempo en milisegundos y tick_ms para calcular el tiempo que ha pasado y asi hacer que la bomba explote cuando terminen los segundos. 

#### Micro-sesión 4: cierre 

Con el analisis de como funciona el tiempo en este ejemplo pude llegar a la conclusion de que este metodo de usar la libreria de Utime podria ser una buena aternativa para implementar en el reto final Sin embargo no se si seria la mas adecuada para dar una buena experiencia al usuario ya que este metodo convierte el tiempo en milisegundos y un usuario promedio no esta acostumbrado a colocar el tiempo en ese formato por lo que en las siguientes sesiones seguire investigando otras alternativas de como controlar tiempo. 

### Sesión 2 miércoles febrero 7


#### Micro-sesión 1: apertura.

En esta sesion el profesor inicio mostrandonos un tipo de emprendimiento nuevo que combina la virtualidad con la realidad llamada JUMP, luego continuo con la retroalimentacion de las bitacoras faltantes, por lo que esta sesion me propuse a investigar alternativas de funciones de manejo del tiempo para el codigo del reto final. 

#### Micro-sesión 2

estuve viendo algunas paginas y videos de cuentas regresivas para ver que funcionen manejan esta es una 
https://microbit.org/es-es/projects/make-it-code-it/counter/
y algunos videos como este 
https://www.youtube.com/watch?v=tPLK0aw2ftc

#### Micro-sesión 3

luego segui en microbit phyton editor para experimentar un poco, tome el codigo de la pagina ya ostrada anteriormente de microbit 
que es este ![image](https://github.com/jfUPB/bitacorassfi12024-10-sebas890p/assets/110270011/212e0f2e-9ef6-40b8-84e6-c5643838e2f5)

y lo converti en un contador que en vez de aumentar disminuya la cuenta y asi me quedo

![image](https://github.com/jfUPB/bitacorassfi12024-10-sebas890p/assets/110270011/b56e49cb-e54e-4e9c-bf51-55f07cb76bb0)


#### Micro-sesión 4: cierre 

En esta sesion me doy cuenta que puede ser posible encontrar una solucion para hacer una cuenta regresiva mas comoda al usuario sin enbargon debo seguir investigando aun mas. 

### Sesión 3 martes 6 de febrero y 8

#### Micro-sesión 1: apertura.

En la casa continue con el punto de la actividad guia que me propuse en clase, tome el tiempo para investigar cada linea del codigo que podria ser gran beneficio para cumplir el reto de la unidad.

#### Micro-sesión 2

Me doy cuenta que el código utiliza una clase llamada pixel que la utiliza para representar un pixel en la pantalla led.

luego esta def __init este metodo inicia la clase pixel el cual tiene 4 instancias pixel x y pixel y, luego esta initState que representa el estado inicial del píxel, y interval que es el intervalo de tiempo en milisegundos para cambiar el estado del píxel.
self.state = "Init": este inicia el atributo state de la instancia a "Init". Este atributo se utiliza para controlar el estado actual del píxel
self.startTime = 0: Inicia el atributo startTime a 0. Se utilizará para medir el tiempo transcurrido
self.interval = interval: se encarga de almacenar el intervalo proporcionado como parámetro en el atributo interval
self.pixelX = pixelX y self.pixelY = pixelY: Almacenan las coordenadas X e Y del píxel en los atributos correspondientes

#### Micro-sesión 3

def update(self): Define el método update de la clase Pixel, que se utiliza para actualizar el estado del píxel.
if self.state == "Init":: Comprueba si el estado actual es "Init".
self.startTime = utime.ticks_ms(): Guarda el tiempo actual en el atributo startTime. Esto marca el inicio del intervalo de tiempo.
self.state = "WaitTimeout": Cambia el estado a "WaitTimeout". Este estado indica que el píxel está esperando hasta que transcurra el intervalo de tiempo.
display.set_pixel(self.pixelX, self.pixelY, self.pixelState): Configura el píxel en la posición especificada con el estado actual.


#### Micro-sesión 4
elif self.state == "WaitTimeout":: Si el estado es "WaitTimeout", ejecuta las siguientes líneas.
currentTime = utime.ticks_ms(): Obtiene el tiempo actual en milisegundos.
if utime.ticks_diff(currentTime, self.startTime) > self.interval:: Comprueba si ha transcurrido el intervalo de tiempo desde la última actualización.
self.startTime = currentTime: Actualiza el tiempo de inicio al tiempo actual.
if self.pixelState == 9: y else:: Cambia el estado del píxel alternando entre 9 y 0.

while True:
    pixel1.update()
    pixel2.update()
Es un bucle infinito que llama al método update de cada instancia en cada iteración. Esto hará que los píxeles cambien de estado según sus intervalos de tiempo especificados.

display.set_pixel(self.pixelX, self.pixelY, self.pixelState): Configura el píxel en la posición especificada con el nuevo estado.

#### Micro-sesión 5: cierre 

Con el analizis de este codigo me doy cuenta que hay varios atributos y metodos que puedo usar para la realizacion del reto final, uno de ellos es el metodo update que se puede usar para actualizar el tiempo en la cuenta regresiva de la bomba, otro seria hacer una clase para definir los parametros de los botones y otra para el de la clave. 


## SEMANA 4

### Sesión 1 lunes febrero 12

#### Micro-sesión 1: apertura.

En esta sesion iniciamos con una introduccion breve del profesor explicando un poco de lo que haremos hoy guiados por el, en esta sesion se planea analizar un codigo c++ similar al reto final de esta unidad el codigo es el siguiente : 

```c++
#include "SSD1306Wire.h"

#define BOMB_OUT 25
#define LED_COUNT 26
#define UP_BTN 13
#define DOWN_BTN 32
#define ARM_BTN 33

void taskSerial();
void taskButtons();
void taskBomb();

void setup() {
  taskSerial();
  taskButtons();
  taskBomb();
}

bool evButtons = false;
uint8_t evButtonsData = 0;

void loop() {
  taskSerial();
  taskButtons();
  taskBomb();
}

void taskSerial() {
  enum class SerialStates {INIT, WAITING_COMMANDS};
  static SerialStates serialState =  SerialStates::INIT;

  switch (serialState) {
    case SerialStates::INIT: {
        Serial.begin(115200);
        serialState = SerialStates::WAITING_COMMANDS;
        break;
      }
    case SerialStates::WAITING_COMMANDS: {

        if (Serial.available() > 0) {
          int dataIn = Serial.read();
          if (dataIn == 'u') {
            Serial.println("UP_BTN");
            evButtons = true;
            evButtonsData = UP_BTN;
          }
          else if (dataIn == 'd') {
            Serial.println("DOWN_BTN");
            evButtons = true;
            evButtonsData = DOWN_BTN;
          }
          else if (dataIn == 'a') {
            Serial.println("ARM_BTN");
            evButtons = true;
            evButtonsData = ARM_BTN;
          }

        }

        break;
      }
    default:
      break;


  }


}

void taskButtons() {
  enum class ButtonsStates {INIT, WAITING_PRESS, WAITING_STABLE, WAITING_RELEASE};
  static ButtonsStates buttonsState =  ButtonsStates::INIT;
  static uint8_t lastButton = 0;
  static uint32_t referenceTime;
  const uint32_t STABLETIMEOUT = 100;

  switch (buttonsState) {
    case ButtonsStates::INIT: {
        pinMode(UP_BTN, INPUT_PULLUP);
        pinMode(DOWN_BTN, INPUT_PULLUP);
        pinMode(ARM_BTN, INPUT_PULLUP);
        buttonsState = ButtonsStates::WAITING_PRESS;
        break;
      }
    case ButtonsStates::WAITING_PRESS: {
        if (digitalRead(UP_BTN) == LOW) {
          buttonsState = ButtonsStates::WAITING_STABLE;
          lastButton = UP_BTN;
          referenceTime = millis();
        }
        else if (digitalRead(DOWN_BTN) == LOW) {
          buttonsState = ButtonsStates::WAITING_STABLE;
          lastButton = DOWN_BTN;
          referenceTime = millis();
        }
        else if (digitalRead(ARM_BTN) == LOW) {
          buttonsState = ButtonsStates::WAITING_STABLE;
          lastButton = ARM_BTN;
          referenceTime = millis();
        }
        break;
      }

    case ButtonsStates::WAITING_STABLE: {
        if (digitalRead(lastButton) == HIGH) {
          buttonsState = ButtonsStates::WAITING_PRESS;
        }
        else if ( (millis() - referenceTime) >= STABLETIMEOUT ) {
          buttonsState = ButtonsStates::WAITING_RELEASE;
        }
        break;
      }

    case ButtonsStates::WAITING_RELEASE: {
        if (digitalRead(lastButton) == HIGH) {
          buttonsState = ButtonsStates::WAITING_PRESS;
          evButtons = true;
          evButtonsData = lastButton;
          printf("Btn press: %d\n", lastButton);
        }

        break;
      }
    default:
      break;

  }

}

void taskBomb() {
  static SSD1306Wire display(0x3c, SDA, SCL, GEOMETRY_64_48);
  enum class BombStates {INIT, WAITING_CONFIG, COUNTING};
  static BombStates bombState =  BombStates::INIT;
  static uint8_t bombCounter = 20;
  static uint8_t secret[7] = {UP_BTN, UP_BTN, DOWN_BTN, DOWN_BTN, UP_BTN, DOWN_BTN, ARM_BTN};
  static uint8_t password[7] = {0};
  static uint8_t passwordCounter = 0;

  static uint32_t referenceTimeBombCounter;
  const uint32_t BOMBINTERVAL = 1000;
  static uint32_t referenceTimeLEDBombCounter;
  const uint32_t LEDBOMBINTERVAL = 500;
  static uint8_t ledBombCountState = LOW;


  switch (bombState) {
    case BombStates::INIT: {
        pinMode(BOMB_OUT, OUTPUT);
        pinMode(LED_COUNT, OUTPUT);

        display.init();
        display.setContrast(255);
        display.clear();

        display.setTextAlignment(TEXT_ALIGN_LEFT);
        display.setFont(ArialMT_Plain_16);
        display.clear();
        display.drawString(10, 20, String(bombCounter));
        display.display();

        digitalWrite(BOMB_OUT, LOW);
        ledBombCountState = HIGH;
        digitalWrite(LED_COUNT, ledBombCountState);


        bombState = BombStates::WAITING_CONFIG;

        break;
      }
    case BombStates::WAITING_CONFIG: {

        if (evButtons == true) {
          evButtons = false;

          if (evButtonsData == UP_BTN) {
            if (bombCounter < 60) {
              bombCounter++;
            }
            display.clear();
            display.drawString(10, 20, String(bombCounter));
            display.display();
          }
          else if (evButtonsData == DOWN_BTN) {
            if (bombCounter > 10) {
              bombCounter--;
            }
            display.clear();
            display.drawString(10, 20, String(bombCounter));
            display.display();
          }
          else if (evButtonsData == ARM_BTN) {
            referenceTimeBombCounter = millis();
            referenceTimeLEDBombCounter = millis();
            passwordCounter = 0;
            bombState = BombStates::COUNTING;
          }
        }

        break;
      }
    case BombStates::COUNTING: {

        if (evButtons == true) {
          evButtons = false;

          password[passwordCounter] = evButtonsData;
          passwordCounter++;

          if (passwordCounter == 7) {
            bool disarm = true;
            for (int i = 0; i < 7; i++) {
              if (password[i] != secret[i]) {
                passwordCounter = 0;
                disarm = false;
                break;
              }
            }
            if (disarm == true) {
              bombCounter = 20;
              display.clear();
              display.drawString(10, 20, String(bombCounter));
              display.display();
              digitalWrite(BOMB_OUT, LOW);
              ledBombCountState = HIGH;
              digitalWrite(LED_COUNT, ledBombCountState);
              bombState = BombStates::WAITING_CONFIG;
            }
          }
        }

        if ( (millis() - referenceTimeLEDBombCounter) >= LEDBOMBINTERVAL ) {
          referenceTimeLEDBombCounter = millis();
          ledBombCountState = !ledBombCountState;
          digitalWrite(LED_COUNT, ledBombCountState);
        }

        if ( (millis() - referenceTimeBombCounter) >= BOMBINTERVAL) {
          referenceTimeBombCounter = millis();
          bombCounter--;
          if (bombCounter > 0 ) {
            display.clear();
            display.drawString(10, 20, String(bombCounter));
            display.display();
          }
          else {
            bombCounter = 20;
            digitalWrite(BOMB_OUT, HIGH);
            display.clear();
            display.drawString(10, 20, "BOOM");
            display.display();
            delay(3000);
            bombCounter = 20;
            display.clear();
            display.drawString(10, 20, String(bombCounter));
            display.display();
            digitalWrite(BOMB_OUT, LOW);
            ledBombCountState = HIGH;
            digitalWrite(LED_COUNT, ledBombCountState);
            bombState = BombStates::WAITING_CONFIG;
          }
        }

        break;
      }

    default:
      break;
  }
}
```

#### Micro-sesión 2
empezamos comparando el codigo de arriba en c++ con la estructura del reto final con c# y phyton utilizado la tecncica de hacer maquinas de estados, sus funciones equivalentes y una posible solucion al problema de la bomba, no se puede usar codigo bloqueante en los estados porque luego va a bloquear las demas variables, se reconoce que es un estado cuando esperamos que suceda algo para eso usamos los if y dentro de los estados hay eventos, las acciones pueden tener o no condiciones de guarda.


#### Micro-sesión 3

podemos hacer los eventos independientes o si lo quiero se pueden hacer dependientes del otro, en phyton para la estructura de la clave hay que hacer una lista y ir añadiendo cada tecla o pulsador que se precione para saber si la clave es correcta, para añadir el serial una logica buena es colocar que en el codigo se sepa si se presiona un boton y si si es asi lo lea tambien se puede añadir una tarea serial que puede tener 2 estados 1 de inicializacion y otro de esperar los comandos, no hay que leer el serial sin datos porque puede tirar errores y bloquear, por lo tanto hay que preguntar antes si si hay datos en el puertos serial antes de leerlo  


#### Micro-sesión 4: cierre 

Para concluir la sesion debo decir que fue una sesion muy buena para tener ideas nuevas que se puedan implementar en el reto final como la utilizacion de las maquinas de estados, que puede ser excelente para iniciar el codigo ya que muchas no se sabe por donde empezar y de esta forma podemos empezar definiendos los estados en el codigo y luego pasar a los eventos y acciones, otra de las cosas que me quedaros es almacenar todas estas acciones en if para mantener un mejor control del programa. 


### Sesión 2 miercoles febrero 14

#### Micro-sesión 1: apertura.


#### Micro-sesión 2

Estuve de forma autonoma haciendo pruebas con la ayuda de chatgpt para el reto final, comence teniendo en cuenta un tip del profesor el cual es pedirle a chatgpt que traduzca el codigo proporcionado en c++ 
a microphyton sin embargo este no lo traduce muy bien por lo que al momento de querer hacer pruebas no pude por lo que este daba error.

![image](https://github.com/jfUPB/bitacorassfi12024-10-sebas890p/assets/110270011/bb1652b4-cc90-4588-adbd-afa5ee452e2b)

por lo tanto con la ayuda de chatgpt empece a hacer pruebas y hacer cambio y por el momento el codigo va asi 

```py

from microbit import display, button_a, button_b, pin_logo, sleep

# Definiciones de pines
BOMB_OUT = pin_logo
LED_COUNT = display
UP_BTN = button_a
DOWN_BTN = button_b
ARM_BTN = button_b

# Estados de la máquina de bomba
class BombStates:
    CONFIGURATION = 0
    ARMED = 1
    EXPLODED = 2
    DISARMED = 3

# Variables globales
current_state = BombStates.CONFIGURATION
countdown_timer = 20
disarm_code = [UP_BTN, DOWN_BTN, UP_BTN, DOWN_BTN, UP_BTN, UP_BTN, ARM_BTN]
entered_code = []

# Función para actualizar la pantalla de LED con el tiempo restante
def update_display():
    global countdown_timer
    display.show(str(countdown_timer))

# Función para iniciar la cuenta regresiva
def start_countdown():
    global current_state, countdown_timer
    current_state = BombStates.ARMED
    while countdown_timer > 0:
        update_display()
        sleep(1000)
        countdown_timer -= 1
    current_state = BombStates.EXPLODED
    display.show("B")

# Función para verificar el código de desarmado
def check_disarm_code():
    global entered_code, disarm_code, current_state, countdown_timer
    if entered_code == disarm_code:
        current_state = BombStates.CONFIGURATION
        countdown_timer = 20
        update_display()
        return True
    else:
        return False

# Bucle principal
while True:
    if current_state == BombStates.CONFIGURATION:
        if UP_BTN.is_pressed():
            if countdown_timer < 60:
                countdown_timer += 1
            update_display()
        elif DOWN_BTN.is_pressed():
            if countdown_timer > 10:
                countdown_timer -= 1
            update_display()
        elif ARM_BTN.is_pressed():
            start_countdown()

    elif current_state == BombStates.ARMED:
        update_display()
        if ARM_BTN.is_pressed():
            entered_code.append(ARM_BTN)
            if len(entered_code) == 7:
                if check_disarm_code():
                    entered_code = []
                else:
                    current_state = BombStates.EXPLODED
        elif UP_BTN.is_pressed():
            entered_code.append(UP_BTN)
            if len(entered_code) == 7:
                if check_disarm_code():
                    entered_code = []
                else:
                    current_state = BombStates.EXPLODED
        elif DOWN_BTN.is_pressed():
            entered_code.append(DOWN_BTN)
            if len(entered_code) == 7:
                if check_disarm_code():
                    entered_code = []
                else:
                    current_state = BombStates.EXPLODED

    elif current_state == BombStates.EXPLODED:
        display.show("B")
        sleep(2000)
        current_state = BombStates.CONFIGURATION
        countdown_timer = 20
        entered_code = []
        update_display()
```

#### Micro-sesión 3

En esta micro sesion empece a hacer las pruebas usando ya el micro:bit para ver como se comportaba, me paso algo inusual, en el programa de microbit phyton el codigo me dejaba armar la bomba y empezar la cuenta regresiva
sin embargo al momento de conectar el microbit este no me deja armar la bomba, me deja subir y bajar el tiempo, tambien debo implentar el serial que por el momento lo que investigue podria incluirlo usando la siguiente funcion : "uart.onDataReceived"

![Imagen de WhatsApp 2024-02-15 a las 12 34 13_79a1a328](https://github.com/jfUPB/bitacorassfi12024-10-sebas890p/assets/110270011/2bf40ff7-d240-423f-88b4-5aa76a7d9660)




#### Micro-sesión 4: cierre 

De esta sesion aprendi como estructurar el codigo y entender un poco mas con las pruebas que implemente, debo es investigar y hacer mas pruebas en clase con el microbit para poner en uso el web serial terminal.


### Sesión 3 jueves 15 de febrero

#### Micro-sesión 1: apertura.

En esta sesion autonoma en casa mi objetivo es seguir con el codigo que empece en clase y hacer algunas correciones y mejoras 


#### Micro-sesión 2

En esta micro sesion estuve revisando para mejorar el codigo que para el reto final, pude hacer que la cuenta regresiva funcione mejor y no tenga errores, sin embargo al momento de colocar la clave esta no pasa al estado desarmado.
el codigo es el siguiente

```py
from microbit import display, button_a, button_b, pin_logo, sleep

# Definiciones de pines
BOMB_OUT = pin_logo
LED_COUNT = display
UP_BTN = button_a
DOWN_BTN = button_b
ARM_BTN = pin_logo 

# Estados de la máquina de bomba
class BombStates:
    CONFIGURATION = 0
    ARMED = 1
    EXPLODED = 2
    DISARMED = 3

# Variables globales
current_state = BombStates.CONFIGURATION
countdown_timer = 20
disarm_code = ['UP', 'DOWN', 'UP', 'DOWN', 'UP', 'UP', 'ARM']
entered_code = []

# Función para actualizar la pantalla de LED con el tiempo restante
def update_display():
    global countdown_timer
    LED_COUNT.show(str(countdown_timer))

# Función para iniciar la cuenta regresiva
def start_countdown():
    global current_state, countdown_timer
    current_state = BombStates.ARMED
    while countdown_timer > 0:
        update_display()
        sleep(1000)
        countdown_timer -= 1
    current_state = BombStates.EXPLODED
    LED_COUNT.show("B")

# Función para verificar el código de desarmado
def check_disarm_code():
    global entered_code, disarm_code, current_state, countdown_timer
    if entered_code == disarm_code:
        current_state = BombStates.DISARMED
        countdown_timer = 20
        update_display()
        return True
    else:
        return False

# Bucle principal
while True:
    if current_state == BombStates.CONFIGURATION:
        if UP_BTN.is_pressed():
            if countdown_timer < 60:
                countdown_timer += 1
            update_display()
        elif DOWN_BTN.is_pressed():
            if countdown_timer > 10:
                countdown_timer -= 1
            update_display()
        elif ARM_BTN.is_touched():
            start_countdown()

    elif current_state == BombStates.ARMED:
        update_display()
        if ARM_BTN.is_touched():
            entered_code.append('ARM')
            if len(entered_code) == 7:
                if check_disarm_code():
                    entered_code = []
                else:
                    current_state = BombStates.EXPLODED
        elif UP_BTN.is_pressed():
            entered_code.append('UP')
            if len(entered_code) == 7:
                if check_disarm_code():
                    entered_code = []
                else:
                    current_state = BombStates.EXPLODED
        elif DOWN_BTN.is_pressed():
            entered_code.append('DOWN')
            if len(entered_code) == 7:
                if check_disarm_code():
                    entered_code = []
                    current_state = BombStates.DISARMED
                else:
                    current_state = BombStates.EXPLODED

    elif current_state == BombStates.EXPLODED:
        LED_COUNT.show("B")
        sleep(2000)
        current_state = BombStates.CONFIGURATION
        countdown_timer = 20
        entered_code = []
        update_display()

    elif current_state == BombStates.DISARMED:
        # Agrega acciones específicas cuando la bomba ha sido desactivada
        LED_COUNT.show("D")  # Muestra una D para indicar que la bomba está desactivada
        sleep(2000)
        current_state = BombStates.CONFIGURATION
        countdown_timer = 20
        entered_code = []
        update_display()
```


#### Micro-sesión 3

Estuve revisando el codigo y relizando algunos cambios para que se pueda desarmar la bomba, entre estos cuando se desarme mostrar una D en los leds, que la cuenta regresiva se reinicie a 20, el codigo quedo asi 

```py
from microbit import display, button_a, button_b, pin_logo, sleep

# Definiciones de pines
LED_COUNT = display
UP_BTN = button_a
DOWN_BTN = button_b
ARM_BTN = pin_logo

# Estados de la máquina de bomba
class BombStates:
    CONFIGURATION = 0
    ARMED = 1
    EXPLODED = 2
    DISARMED = 3

# Variables globales
current_state = BombStates.CONFIGURATION
countdown_timer = 20
disarm_code = ['UP', 'DOWN', 'UP', 'DOWN', 'UP', 'UP', 'ARM']
entered_code = []

# Función para actualizar la pantalla de LED con el tiempo restante
def update_display():
    global countdown_timer
    LED_COUNT.show(str(countdown_timer))

# Bucle principal
while True:
    if current_state == BombStates.CONFIGURATION:
        if UP_BTN.is_pressed():
            if countdown_timer < 60:
                countdown_timer += 1
            update_display()
        elif DOWN_BTN.is_pressed():
            if countdown_timer > 10:
                countdown_timer -= 1
            update_display()
        elif ARM_BTN.is_touched():
            current_state = BombStates.ARMED
            entered_code = []

    elif current_state == BombStates.ARMED:
        update_display()
        if countdown_timer > 0:
            sleep(1000)
            countdown_timer -= 1
            update_display()

        if ARM_BTN.is_touched():
            entered_code.append('ARM')
            if len(entered_code) == 7 and entered_code == disarm_code:
                current_state = BombStates.DISARMED
                countdown_timer = 20  # Reinicia el temporizador al desactivar
            elif len(entered_code) == 7:
                current_state = BombStates.EXPLODED
            sleep(500)  # Asegurarse de que no se detecten múltiples toques

        elif countdown_timer == 0:
            current_state = BombStates.EXPLODED

    elif current_state == BombStates.EXPLODED:
        LED_COUNT.show("B")
        sleep(2000)
        current_state = BombStates.CONFIGURATION
        countdown_timer = 20
        update_display()

    elif current_state == BombStates.DISARMED:
        LED_COUNT.show("D")
        sleep(2000)
        current_state = BombStates.CONFIGURATION
        countdown_timer = 20
        update_display()
```

sin embargo dentro del programa de micrbit phyton sigue sin funcionar al momento de ingresar la clave, por lo que me debo hacer pruebas en el salon con el controlador microbit.


#### Micro-sesión 4: 

Realmenta esta micro sesion no hice mucho ya que no sabia que hacer porque debo implemtar el codigo en clase usando el microbit para ver su funcionamiento por lo que estuve viendo un video tutorial del microbit donde hablablan de sus funciones y que cosas se pueden hacer en el dando ejemplos sencillos, el video es el siguiente:

https://www.youtube.com/watch?v=MY4jDrN9_cc


#### Micro-sesión 5: cierre 

Como clonclusion siento que voy por buen camino debo seguir haciendo pruebas tanto en el programa como en el controlador para corroborar que todo funcione correctamente.


## SEMANA 5

### Sesión 1 lunes febrero 19

#### Micro-sesión 1: apertura.

En esta sesion tengo como proposito ver como funciona el codigo del reto final usando el controlador microbit prestado por el profesor .


#### Micro-sesión 2:

Estuve haciendo pruebas para poder solucionar el problema con el desarmo de la bomba, lo que se me ocurrio fue quitar el bucle y conformar el codigo de puros IF y ELSE por si en el bucle algo bloqueaba el desarmo, el codigo quedo asi:

```py
from microbit import display, button_a, button_b, pin_logo, sleep

# Definiciones de pines
LED_COUNT = display
UP_BTN = button_a
DOWN_BTN = button_b
ARM_BTN = pin_logo

# Estados de la máquina de bomba
class BombStates:
    CONFIGURATION = 0
    ARMED = 1
    EXPLODED = 2
    DISARMED = 3

# Variables globales
current_state = BombStates.CONFIGURATION
countdown_timer = 20
disarm_code = ['UP', 'DOWN', 'UP', 'DOWN', 'UP', 'UP', 'UP']
entered_code = [UP_BTN , DOWN_BTN , UP_BTN , DOWN_BTN , UP_BTN, UP_BTN , ARM_BTN]

# Función para actualizar la pantalla de LED con el tiempo restante
def update_display():
    global countdown_timer
    LED_COUNT.show(str(countdown_timer))

# Función para manejar la lógica de la bomba 
def bomb_logic():
    global current_state, countdown_timer, entered_code

    if current_state == BombStates.CONFIGURATION:
        if UP_BTN.is_pressed():
            if countdown_timer < 60:
                countdown_timer += 1
            update_display()
        elif DOWN_BTN.is_pressed():
            if countdown_timer > 10:
                countdown_timer -= 1
            update_display()
        elif ARM_BTN.is_touched():
            current_state = BombStates.ARMED
            entered_code = [UP_BTN , DOWN_BTN , UP_BTN , DOWN_BTN , UP_BTN, UP_BTN , ARM_BTN]
            update_display()  
    elif current_state == BombStates.ARMED:
        if countdown_timer > 0:
            sleep(1000)
            countdown_timer -= 1
            update_display()

        if ARM_BTN.is_touched():
            entered_code.append('ARM')
            if len(entered_code) == 7:
                if entered_code == disarm_code:
                    current_state = BombStates.DISARMED
                else:
                    current_state = BombStates.EXPLODED
            sleep(500)  
            update_display()  
        elif countdown_timer == 0:
            current_state = BombStates.EXPLODED
            update_display()  

    elif current_state == BombStates.EXPLODED:
        LED_COUNT.show("B")
        sleep(2000)
        current_state = BombStates.CONFIGURATION
        countdown_timer = 20
        update_display()

    elif current_state == BombStates.DISARMED:
        LED_COUNT.show("D")
        sleep(2000)
        current_state = BombStates.CONFIGURATION
        countdown_timer = 20
        update_display()

# Bucle principal
while True:
    bomb_logic()
```

Lo que hice fue poner un while al final para que maneja la logica de la bomba y haya un bucle para actualizar la pantalla, sin embargo no funciona el estado de desarmar la bomba.

#### Micro-sesión 3:

En esta micro sesion lo que hice fue añadir el sonido al momento de que la bomba explote, guiandome de la siguiente pagina:
https://microbit.org/es-es/projects/make-it-code-it/make-some-noise/

![image](https://github.com/jfUPB/bitacorassfi12024-10-sebas890p/assets/110270011/8264f0d8-5c29-4cc0-a058-346631a64de2)

```py
from microbit import display, button_a, button_b, pin_logo, sleep 
import music

# Definiciones de pines
LED_COUNT = display
UP_BTN = button_a
DOWN_BTN = button_b
ARM_BTN = pin_logo

# Estados de la máquina de bomba
class BombStates:
    CONFIGURATION = 0
    ARMED = 1
    EXPLODED = 2
    DISARMED = 3

# Variables globales
current_state = BombStates.CONFIGURATION
countdown_timer = 20
disarm_code = ['UP', 'DOWN', 'UP', 'DOWN', 'UP', 'UP', 'UP']
entered_code = [UP_BTN , DOWN_BTN , UP_BTN , DOWN_BTN , UP_BTN, UP_BTN , ARM_BTN]

# Función para actualizar la pantalla de LED con el tiempo restante
def update_display():
    global countdown_timer
    LED_COUNT.show(str(countdown_timer))

# Función para manejar la lógica de la bomba 
def bomb_logic():
    global current_state, countdown_timer, entered_code

    if current_state == BombStates.CONFIGURATION:
        if UP_BTN.is_pressed():
            if countdown_timer < 60:
                countdown_timer += 1
            update_display()
        elif DOWN_BTN.is_pressed():
            if countdown_timer > 10:
                countdown_timer -= 1
            update_display()
        elif ARM_BTN.is_touched():
            current_state = BombStates.ARMED
            entered_code = [UP_BTN , DOWN_BTN , UP_BTN , DOWN_BTN , UP_BTN, UP_BTN , ARM_BTN]
            update_display()  
    elif current_state == BombStates.ARMED:
        if countdown_timer > 0:
            sleep(1000)
            countdown_timer -= 1
            update_display()

        if ARM_BTN.is_touched():
            entered_code.append('ARM')
            if len(entered_code) == 7:
                if entered_code == disarm_code:
                    current_state = BombStates.DISARMED
                else:
                    current_state = BombStates.EXPLODED
            sleep(500)  
            update_display()  
        elif countdown_timer == 0:
            current_state = BombStates.EXPLODED
            music.play(music.BA_DING)
            update_display()  

    elif current_state == BombStates.EXPLODED:
        LED_COUNT.show("B")
        sleep(2000)
        current_state = BombStates.CONFIGURATION
        countdown_timer = 20
        update_display()

    elif current_state == BombStates.DISARMED:
        LED_COUNT.show("D")
        sleep(2000)
        current_state = BombStates.CONFIGURATION
        countdown_timer = 20
        update_display()

# Bucle principal
while True:
    bomb_logic()
```

Este es el codigo con el sonido.

Insero video de la prueba del microbit con el sonido.



https://github.com/jfUPB/bitacorassfi12024-10-sebas890p/assets/110270011/6c690c50-91a1-49ba-9b0d-8d386cf4016e





#### Micro-sesión 4: cierre

De esta sesion concluyo que me debo seguir buscando soluciones para que el estado de desarmo funcione, sin embargo en el resto del codigo voy bien.

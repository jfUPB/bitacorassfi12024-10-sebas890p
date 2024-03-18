# Bitácora de aprendizaje

> [!IMPORTANT]  
> RETO PERSONALIZADO
> 
> Personaliza el reto cambiando los signos ¿? por tu personalización. ¿Qué interés vas a explorar? ¿En qué consiste la aplicación
> ¿Qué sensores y actuadores usarás
> 
> Diseñaré e implementaré una aplicación interactiva para explorar ¿? mediante la integración de los siguientes sensores: ¿? y estos actuadores ¿?. La integración se realizará mediante protocolos ASCII utilizando una
> arquitectura cliente-servidor.

## SEMANA 6

### Sesión 1: lunes febrero 26


#### micro sesion 1: apertura

En esta sesion trabajaremos guiados del profesor, nos planteo que haremos un repaso de la unidad 1 y de como podemos implementar la estructura del codigo de la bomba en otros codigos.

#### micro sesion 2: 

En esta micro sesion estamos revisando el codigo de la bomba en c++ que nos compartio el profesor para guiarnos, con este codigo el profesor esta explicandonos como con esta estructura de maquinas de estados la podemos implementar en muchos proyectos. a la vez nos hizo la introduccion a la unidad 2, la cual se va a tratar de empezar a hacer aplicaciones interactivas, usando los protocolos ASCII, con cual haremos una aplicacion para la final de la unidad, tambien nos explico sobre los 4 momentos en esta unidad que son: Comprometerse, Investigar, aplicar, compartir. 


#### micro sesion 3: 

En esta micro sesion estuve viendo algunos de los ejemplos que estan en el documento para inspirarme y tener ideas para el reto final, por el momento se me surgio una idea con la deteccion de movimientos que se trata de leer los gestos mediante una camara y pintarlos en los leds del microbit como emojis, por ejemplo si sonrio en la camara se pintaria en los leds una cara feliz, sin embargo debo investigar a ver que tan posible pueda ser esta idea 

#### micro sesion 4: cierre 

Esta unidad me parece muy interesante e importante ya que vamos a aprender a usar comunicaciones mediante ASCII que es algo muy importante para realizar proyectos propios, a la vez el poder realizar una aplcacion que nos sirva para el portafolio lo hace aun mas interesante.


### Sesión 2: miercoles febrero 28

#### micro sesion 1: apertura

Para esta sesion planeo trabajar en esta unidad 2 con una idea que traje que se trata de mediante reconocimiento facial detectar gestos y que estos se pinten en los leds del microbit, le pregunte sobre esta idea al profesor para saber que tan posible puede ser y el me dio algunos materiales donde puedo guiarme para realizarlo por lo que en esta sesion estare revisando este material. 

#### micro sesion 2:

Estuve mirando algunos videos y entendi la teoria de como hacerlo sin embargo aun no se comose integra por lo que veo pertinente realizar el apartado investigativo que esta propuesto en el documento de la clase para asi entender un poco como se integra cada programa

#### micro sesion 3:

En esta micro sesion estuve haciendo algunos modelos en teachable machine para ver su funcionalidad, el link a la pagina es el siguiente:
https://teachablemachine.withgoogle.com/train/image

entre estos modelos como ejemplo adjuntare el modelo de ok y de mal
![image](https://github.com/jfUPB/bitacorassfi12024-10-sebas890p/assets/110270011/631019c7-23b8-4980-aac6-8f49db0fcaec)


#### micro sesion 4: cierre 

En esta sesion me di cuenta que si es posible hacer el reconomiento de gestos mediante la camara como tenia pensado, en las sesion autonoma debo mirar mas a fondo como unir los codigos que me genera teachable machine. 


### Sesión 3: autonoma jueves febrero 29


#### micro sesion 1: apertura

En esta sesion autonoma me dedicare a investigar en que proyecto trabajar para la entrega final porque el que tenia pensado me queda dificil llevarlo a cabo ya que no cuento con webcam en mi computador personal por lo que solo podria hacer pruebas en clases. 


#### micro sesion 2:

En los ejemplos dados por el profesor sobre proyectos que usan p5.js y microbit hay uno que me intereso mucho que es el siguiente 


https://youtube.com/shorts/WsIhLJInnio?si=w2KeS0Q2XJo3kIf7


![image](https://github.com/jfUPB/bitacorassfi12024-10-sebas890p/assets/110270011/76d88948-350c-4f60-8319-4f2db89f7ca9)


en este video podemos observar como se usa el acelerometro del microbit para dibujar en p5.js, este proyecto me intereso bastante, sin embargo para no hacerlo igual al del ejemplo pense que en implementar un laberinto en p5.js y usar el acelerometro del microbit para controlar un punto el cual pasara el laberinto. 


#### micro sesion 3:

Para entender un poco mas como llevarlo a cabo con la ayuda de chatgpt respondere la pregunta esencial que esta planteada por el profesor que es la siguiente:

¿Cómo conectar el mundo físicos con mundos virtuales mediante la construcción de aplicaciones interactivas?

Sensores en el Mundo Físico:

Utiliza sensores físicos (como sensores de temperatura, de luz, de movimiento, etc.) para recopilar datos del entorno real.
Convierte los datos recopilados por los sensores en valores numéricos ASCII que representen las lecturas de los sensores.
Comunicación con el Mundo Virtual:

Establece una conexión entre el mundo físico y el mundo virtual, por ejemplo, utilizando un microcontrolador como Arduino o un dispositivo IoT.
Envía los datos ASCII recopilados por los sensores a través de la conexión al mundo virtual.
Aplicaciones Interactivas en el Mundo Virtual:

En el mundo virtual (por ejemplo, una aplicación web o una aplicación de escritorio), crea una interfaz que reciba y procese los datos ASCII enviados desde el mundo físico.
Utiliza los datos recibidos para generar respuestas interactivas en la aplicación virtual, como mostrar visualizaciones de datos, controlar objetos virtuales, o realizar acciones específicas basadas en las entradas del mundo físico.
Respuesta del Mundo Virtual al Mundo Físico:

También puedes diseñar la aplicación virtual para enviar datos ASCII de vuelta al mundo físico en respuesta a las interacciones del usuario en el mundo virtual.
Por ejemplo, podrías activar actuadores físicos (como LEDs, motores, etc.) basados en las acciones realizadas por el usuario en la aplicación virtual.


#### micro sesion 4:

Este es un ejemplo bueno que me dio chatgpt para entender mejor como conectar el mundo real con el virtual:

Supongamos que tienes un sensor de temperatura conectado a un microcontrolador Arduino en el mundo físico. Este sensor recopila la temperatura ambiente y la convierte en un valor numérico. Luego, el microcontrolador envía este valor numérico como una cadena ASCII a una aplicación web en el mundo virtual. En la aplicación web, este valor se utiliza para actualizar un gráfico de temperatura en tiempo real, permitiendo a los usuarios monitorear la temperatura ambiente desde cualquier lugar con acceso a internet.

Esta integración de dispositivos físicos con aplicaciones interactivas en el mundo virtual a través del protocolo ASCII proporciona una forma poderosa de crear experiencias interactivas que combinan lo físico y lo digital.

#### micro sesion 5: 

Me gusto mucho la idea que surgio de esta sesion sobre el laberinto, me inspire del proyecto de dibujar controlandolo desde el microbit pero le hice unos cambios para que sea diferente, en las siguientes sesiones debo investigar como llevarlo a cabo.



## SEMANA 7

### Sesión 1: lunes marzo 4


#### micro sesion 1: apertura

Comenzamos la sesion con una explicacion del profesor sobre el codigo que esta en la unidad 2 para el microbit donde una hay tecnica para hacer la comunicacion ASCII

este es el codigo que estuvimos revisando junto al profesor 

![image](https://github.com/jfUPB/bitacorassfi12024-10-sebas890p/assets/110270011/2207f7b5-5e93-45d8-a0b9-d6c210ce1184)




#### micro sesion 2:

Luego de revisar el codigo me dedicare a responder las preguntas sobre este codigo que planteo el profesor:

¿Cuántos y cuáles estados tiene este programa?

Este tiene varios estados que son los iguientes:

Espera de Shake: En este estado, el programa espera que el acelerómetro detecte un movimiento de sacudida. Cuando se detecta una sacudida, el programa cambia al estado de envío de mensaje a través de UART.

Envío de Mensaje a través de UART: Una vez que se detecta una sacudida, el programa cambia a este estado. En este estado, muestra una cara feliz en la pantalla LED, envía el mensaje "hello world" a través de la interfaz UART y luego muestra un corazón en la pantalla LED. Después de esto, el programa vuelve al estado de espera de sacudida.

Espera de Recepción UART: Este estado ocurre cuando el programa está esperando recibir datos a través de la interfaz UART. Si se recibe algún dato, el programa cambia al estado de procesamiento de datos UART.

Procesamiento de Datos UART: Cuando se reciben datos a través de la interfaz UART, el programa entra en este estado. Aquí, lee los datos uno por uno hasta que encuentra un carácter de nueva línea ('\n'). Luego procesa el mensaje recibido mostrándolo en la pantalla LED, seguido por el número de caracteres en el mensaje. Una vez que se ha procesado el mensaje, el programa vuelve al estado de espera de recepción UART.


¿Cuántos y cuáles son los eventos que tiene este programa?

Este tiene 2 eventos:



Detección de Sacudida (Shake Detection): Este evento ocurre cuando el acelerómetro detecta un movimiento de sacudida. Desencadena el cambio de estado del programa desde el estado de espera de sacudida al estado de envío de mensaje a través de UART.

Recepción de Datos UART (UART Data Reception): Este evento ocurre cuando se reciben datos a través de la interfaz UART. Desencadena el cambio de estado del programa desde el estado de espera de recepción UART al estado de procesamiento de datos UART.

#### micro sesion 3:

¿Hay condiciones guarda? ¿Cuáles son esas condiciones de guarda?


Sí, hay condiciones de guarda en este programa. Las condiciones de guarda son las expresiones que se evalúan para determinar si una determinada sección del código debe ejecutarse o no. En este caso, las condiciones de guarda están asociadas con las estructuras de control if y while. Aquí están las condiciones de guarda en el código proporcionado:

Condición de Guarda en el Bucle Principal (while True):

sta es una condición de guarda perpetua que asegura que el bucle se ejecute continuamente mientras la expresión True (verdadero) sea verdadera. Esto significa que el programa se ejecutará indefinidamente, ya que True es siempre verdadero.



Condición de Guarda para la Detección de Sacudida (Shake Detection):

Esta condición de guarda se evalúa para determinar si se ha detectado una sacudida en el dispositivo Micro:bit utilizando el acelerómetro. Si esta condición es verdadera (es decir, si se detecta una sacudida), el bloque de código dentro del if se ejecuta.


Condición de Guarda para la Recepción de Datos UART (UART Data Reception):


Esta condición de guarda verifica si hay datos disponibles para ser leídos a través de la interfaz UART. Si la condición es verdadera (es decir, si hay datos disponibles), el bloque de código dentro del if se ejecuta.


#### micro sesion 4:cierre

En esta sesion aprendi y entendi sobre el codigo que nos dio el profesor, el cual me puede ayudar para emplear las conexiones uart para el reto final.


### Sesión 2: miercoles marzo 6



#### micro sesion 1: apertura

En esta sesion tengo planeado hacer la sesion de exprimentación, para esto voy a empezar usando los codigos propuestos por el profesor el cual uno es para el microbit y otro para p5.js los cuales son:

```py  microbit
from microbit import *

uart.init(baudrate=115200)
display.show(Image.BUTTERFLY)

while True:
    if button_a.is_pressed():
        uart.write('A')
        sleep(500)
    if button_b.is_pressed():
        uart.write('B')
        sleep(500)
    if accelerometer.was_gesture('shake'):
        uart.write('C')
        sleep(500)
    if uart.any():
        data = uart.read(1)
        if data:
            if data[0] == ord('h'):
                display.show(Image.HEART)
                sleep(500)
                display.show(Image.HAPPY)
```


```p5.js
let port;
let connectBtn;

function setup() {
    createCanvas(400, 400);
    background(220);
    port = createSerial();
    connectBtn = createButton('Connect to micro:bit');
    connectBtn.position(80, 300);
    connectBtn.mousePressed(connectBtnClick);
    let sendBtn = createButton('Send Love');
    sendBtn.position(220, 300);
    sendBtn.mousePressed(sendBtnClick);
    fill('white');
    ellipse(width / 2, height / 2, 100, 100);
}

function draw() {

    if(port.availableBytes() > 0){
        let dataRx = port.read(1);
        if(dataRx == 'A'){
            fill('red');
        }
        else if(dataRx == 'B'){
            fill('yellow');
        }
        else{
            fill('green');
        }
        background(220);
        ellipse(width / 2, height / 2, 100, 100);
        fill('black');
        text(dataRx, width / 2, height / 2);
    }


    if (!port.opened()) {
        connectBtn.html('Connect to micro:bit');
    }
    else {
        connectBtn.html('Disconnect');
    }
}

function connectBtnClick() {
    if (!port.opened()) {
        port.open('MicroPython', 115200);
    } else {
        port.close();
    }
}

function sendBtnClick() {
    port.write('h');
}
```




#### micro sesion 2:

Empece a expirementar con estos dos codigos pero en p5.js me arroja un error que es el siguiente:

![image](https://github.com/jfUPB/bitacorassfi12024-10-sebas890p/assets/110270011/310d0c11-93cd-488c-b131-67f52031b485)

Al ver el error decidi empezara a responder las preguntas que estan debajo del codigo para ver si con eso podia entender y solucionar el error.


¿Qué es p5.webserial.js?



p5.webserial.js es una biblioteca para el entorno de programación creativa p5.js. Esta biblioteca proporciona una interfaz entre p5.js y la API Web Serial, permitiendo a los desarrolladores interactuar con dispositivos serie desde el navegador web.

La API Web Serial es una tecnología que permite a los navegadores web comunicarse con dispositivos serie conectados al sistema, como Arduino u otros microcontroladores. p5.webserial.js simplifica el proceso de comunicación serie en p5.js, lo que facilita a los desarrolladores la creación de aplicaciones interactivas que interactúan con dispositivos físicos a través de la comunicación serie.

Al utilizar p5.webserial.js, los desarrolladores pueden enviar y recibir datos serie desde y hacia dispositivos conectados, lo que amplía las posibilidades de creación de aplicaciones web interactivas que involucren hardware físico.



#### micro sesion 3:


¿Cómo hago para incluir en mi proyecto de p5.js a p5.webserial.js?


Descarga p5.webserial.js: Primero, necesitas descargar la biblioteca p5.webserial.js desde su repositorio en GitHub o desde la fuente oficial.

Agrega el archivo a tu proyecto: Una vez que hayas descargado p5.webserial.js, agrega el archivo a la carpeta de tu proyecto de p5.js. Asegúrate de que esté en la misma carpeta que tu archivo HTML principal.

Incluye el script en tu HTML: Abre tu archivo HTML principal y agrega una etiqueta de script para incluir p5.webserial.js antes de la etiqueta de cierre </body>. Debería verse algo así:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Tu proyecto p5.js con p5.webserial.js</title>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.4.0/p5.js"></script>
  <!-- Agrega p5.webserial.js -->
  <script src="p5.webserial.js"></script>
</head>
<body>
  <!-- Aquí va tu código p5.js -->
  <script>
    function setup() {
      createCanvas(400, 400);
      // Tu código de configuración
    }
    
    function draw() {
      background(220);
      // Tu código de dibujo
    }
  </script>
</body>
</html>
```




#### micro sesion 4: cierre

En esta sesion no pude realizar los experimentos como hubiera querido por el error que me aparecio, sin embargo a raiz de esto respondi 2 preguntas las cuales me serviran mucho para la comunicacion serial. 




### Sesión 3: jueves marzo 7

#### micro sesion 1: apertura

En esta sesion autonoma tengo planeado seguir respondiendo las preguntas que me hicieron falta por reponder de la sesion 2 

que son las siguientes:

¿Cómo se crea un objeto que represente el puerto serial?

¿Es necesario abrir y cerrar el puerto serial? ¿Por qué? ¿Qué pasa si no lo hago?

¿Cómo hago para enviar datos el micro:bit desde p5.js y desde p5.js a micro:bit?



#### micro sesion 2:

¿Cómo se crea un objeto que represente el puerto serial?


Incluye la biblioteca p5.webserial.js en tu proyecto.

Utiliza la función serial.getPorts() para obtener una lista de puertos disponibles. Esta función devuelve una promesa que resuelve en una matriz de objetos que representan los puertos serie disponibles.

Selecciona el puerto serie que deseas utilizar. Puedes mostrar la lista de puertos disponibles y permitir que el usuario seleccione uno, o puedes seleccionar automáticamente el puerto si sabes cuál es el que necesitas.

Crea un objeto Serial utilizando el puerto seleccionado. Este objeto te permite comunicarte con el dispositivo conectado al puerto serie.

este es un ejemplo de como hacerlo:


```js
let serial; // Variable para almacenar el objeto Serial

async function setup() {
  createCanvas(400, 400);
  
  // Obtiene una lista de puertos disponibles
  const portList = await serial.getPorts();

  // Selecciona el primer puerto de la lista (puedes implementar lógica para permitir que el usuario seleccione uno)
  const selectedPort = portList[0];

  // Crea el objeto Serial utilizando el puerto seleccionado
  serial = new Serial(selectedPort);

  // Configura la tasa de baudios (opcional, dependiendo del dispositivo)
  serial.baudrate = 9600;

  // Abre el puerto serie
  await serial.open();
}

function draw() {
  background(220);
  // Tu código de dibujo
}

// Función para manejar los datos recibidos del puerto serie
function serialEvent() {
  // Lee los datos disponibles del puerto serie
  const data = serial.read();
  // Realiza el procesamiento necesario con los datos recibidos
  // Por ejemplo, puedes mostrarlos en la consola del navegador
  console.log(data);
}
```


¿Es necesario abrir y cerrar el puerto serial? ¿Por qué? ¿Qué pasa si no lo hago?


En el contexto de la comunicación serie utilizando p5.webserial.js, es importante abrir y cerrar el puerto serial por varias razones:

Inicialización y configuración del puerto: Al abrir el puerto serial, se establece la conexión entre tu aplicación web y el dispositivo conectado al puerto serie. Esto permite configurar parámetros importantes como la velocidad de transmisión (baudrate) u otros ajustes necesarios para la comunicación efectiva.

Inicio de la comunicación: Al abrir el puerto serial, se inicia la comunicación entre tu aplicación y el dispositivo. Esto permite que tu aplicación envíe y reciba datos del dispositivo conectado.

Liberación de recursos: Al cerrar el puerto serial, se liberan los recursos utilizados por la conexión serie, lo que puede ser importante para evitar problemas de memoria o interferencias con otras operaciones de comunicación serie en el sistema.

Si no abres el puerto serial, tu aplicación no podrá comunicarse con el dispositivo conectado. Es similar a intentar enviar un mensaje a través de un canal de comunicación que no está abierto: no se establecerá la conexión y no se podrán intercambiar datos.

Del mismo modo, si no cierras el puerto serial después de haber terminado de utilizarlo, podrías dejar recursos del sistema ocupados innecesariamente, lo que podría llevar a problemas de rendimiento o interferencias con otras aplicaciones que necesiten utilizar el puerto serie.




#### micro sesion 3:


¿Cómo hago para enviar datos el micro:bit desde p5.js y desde p5.js a micro:bit?

Configuración del Microbit:
Programa tu micro:bit para que actúe como un dispositivo serie. Puedes usar MakeCode o MicroPython para escribir un código que lea y escriba datos a través del puerto serie.

Ejemplo de código para MicroPython:

```py
from microbit import *
import radio

radio.off()
uart.init(baudrate=115200)

while True:
    if uart.any():
        incoming = uart.read()
        display.scroll(incoming)
```

Este código espera recibir datos por el puerto serie y luego los muestra en el display LED del microbit.

Configuración de p5.js:
Incluye la biblioteca p5.webserial.js en tu proyecto, como se explicó anteriormente.

Escribe el código en p5.js para enviar y recibir datos. un ejemplo básico:


```js
let serial;

async function setup() {
  createCanvas(400, 400);
  
  // Obtiene una lista de puertos disponibles
  const portList = await serial.getPorts();

  // Selecciona el primer puerto de la lista (puedes implementar lógica para permitir que el usuario seleccione uno)
  const selectedPort = portList[0];

  // Crea el objeto Serial utilizando el puerto seleccionado
  serial = new Serial(selectedPort);

  // Abre el puerto serie
  await serial.open();

  // Configura la tasa de baudios para que coincida con la configuración del micro:bit
  serial.baudrate = 115200;
}

function draw() {
  background(220);
  // Tu código de dibujo
}

// Función para manejar los datos recibidos del puerto serie
function serialEvent() {
  // Lee los datos disponibles del puerto serie
  const data = serial.read();
  // Realiza el procesamiento necesario con los datos recibidos
  // Por ejemplo, puedes mostrarlos en la consola del navegador
  console.log(data);
}

// Función para enviar datos al micro:bit
function enviarDatosMicroBit(datos) {
  serial.write(datos);
}
```








#### micro sesion 4: 


En esta micro sesion voy a trabajar las preguntas relacionadas a la cadena de numeros que dicta mi tia ya que no he trabajado en este eejercicio y me servira como investigacion

el caso es el seguiente:

Estas hablando con tu tía por celular y ella te está dice que te va a dictar una cadena de números. ¿Cómo haces para saber que tu tía ya terminó de dictarte toda la cadena de números?

¿Qué relación tiene el caso de tu tía con la siguiente línea de código?

if uart.any():
    data = uart.read(1)
    if data:
        if data[0] == ord('\n'):


La relacion que tiene este codigo es que podemos decir que mientras la tia esta dictando una cadena de numeros en este caso nosotros estamos actuando como la funcion uart.read que es la encargada de leer las cadenas de datos siempre y cuando tenga alguna para leer, vemos que si la informacion en este caso data es 0 esto es igual a que ya no hay mas datos para la cadena y esta saltara a otra o dejara un espacio con \n

luego de este caso tambien hay pregunta que es la siguiente:

¿Para qué sirve esta línea de código?

line = bytes(buffer[:end]).decode('utf-8').strip



Esta línea de código sirve para convertir una porción de datos de tipo bytes en una cadena de caracteres Unicode utilizando la codificación UTF-8 y luego eliminar los espacios en blanco al principio y al final de la cadena resultante.

Aquí hay una explicación detallada de lo que hace cada parte de la línea:

bytes(buffer[:end]): Toma una porción de datos desde el inicio hasta la posición end del buffer y lo convierte en un objeto de tipo bytes.

.decode('utf-8'): Decodifica los bytes utilizando la codificación UTF-8 para convertirlos en una cadena de caracteres Unicode. La codificación UTF-8 es una de las más comunes y permite representar caracteres de múltiples idiomas.

.strip(): Elimina los espacios en blanco al principio y al final de la cadena resultante. Esto es útil para limpiar los datos y eliminar cualquier espacio adicional que pueda haber sido introducido durante la transmisión o manipulación de los datos.







#### micro sesion 5: cierre


Con esta sesion que fue de investigacion a raiz de las preguntas propuestas por el profesor he podido comprender mejor varios conceptos y funcionalidades de lineas del codigo las cuales se pueden implementar para el reto final propuesto, la idea es en las siguientes sesiones empezara a trabajar mas enfocado en mi reto final. 





## SEMANA 8



### Sesión 1: lunes marzo 13


#### micro sesion 1: apertura

En esta sesion tengo planeado terminar la investigacion y empezar a experimentar un poco en el reto final.



#### micro sesion 2:



Ahora es momento de recordar a tu tía. Ella te dictó una cadena de número. Ahora es tu turno. Le debes dictar tres cadenas números a ella. Además, tu tía debe tener claro cuando terminaste de dictar la tercer cadena.

¿Cómo solucionarías esto haciendo incluyendo entre cada cadena una palabra especial?

¿Cómo harías para hacerle saber a tu tía que ya terminaste con la última cadena?



Para resolver este problema, podemos dictar las tres cadenas de números a nuestra tía, incluyendo una palabra especial entre cada una para separarlas. Además, al final de la tercera cadena, podemos decir otra palabra especial para indicar que hemos terminado de dictar todas las cadenas. Aquí hay un ejemplo de cómo podríamos hacerlo:

"La primera cadena es: [cadena de números]. La palabra especial es 'banana'."
"Ahora la segunda cadena: [cadena de números]. La palabra especial es 'manzana'."
"Y por último, la tercera cadena: [cadena de números]. La palabra especial es 'naranja'."
"Listo, eso es todo. La palabra especial para indicar que terminé es 'final'."
Entonces, en este ejemplo, estamos usando las palabras 'banana', 'manzana' y 'naranja' como palabras especiales para separar cada cadena de números, y la palabra 'final' para indicar que hemos terminado de dictar todas las cadenas.

Este enfoque permite que nuestra tía identifique claramente cada cadena de números y sepa cuándo hemos terminado de dictar todas las cadenas.



#### micro sesion 3:

En esta sesion empece a experimentar un poco en p5.js en crear el laberinto el resultado es el siguiente:

![image](https://github.com/jfUPB/bitacorassfi12024-10-sebas890p/assets/110270011/5abdb8c5-eacb-4f22-968e-7748932d541e)


Debo crear mas muros como los que se aprecian en la imagen y la pelotica es la que se movera con el microbit.


#### micro sesion 4: cierre

En esta sesion ya termino con la investigacion por lo que me puse a experimentar un poco, ya en las siguientes sesion seran de experimentacion. 

 

### Sesión 2: miercoles marzo 11



#### micro sesion 1: apertura

En esta sesion tengo planeado seguir con el experimentando en el laberinto.


#### micro sesion 2:

En esta micro sesion me dedique a crear paredes para intentar recrear un laberinto, despues de varios intentos este es el resultado:

![image](https://github.com/jfUPB/bitacorassfi12024-10-sebas890p/assets/110270011/c8fc6943-dde5-4736-a880-308e7eaff2cb)

no es el laberinto final pero es un avance ya que se puede apreciar que consegui hacer un camino por el cual tendra paso la pelota


#### micro sesion 3:


En esta micro sesion segui experimentando con las paredes del laberinto y hice la version final que es la siguiente:

![image](https://github.com/jfUPB/bitacorassfi12024-10-sebas890p/assets/110270011/ad91e5dc-3b22-498b-8af4-8f695fdba936)

no es el laberinto mas bonito pero me servira para lo que necesito, el codigo del canvas del laberinto es el siguiente:


```js
function setup() {
  createCanvas(400, 400);
  // Definir las paredes del laberinto
  mazeWalls.push(new Wall(0, 0, 400, 10)); // Pared superior
  mazeWalls.push(new Wall(0, 390, 400, 10)); // Pared inferior
  mazeWalls.push(new Wall(0, 0, 10, 400)); // Pared izquierda
  mazeWalls.push(new Wall(390, 0, 10, 400)); // Pared derecha
  mazeWalls.push(new Wall(50, 50, 100, 10));
  mazeWalls.push(new Wall(50, 200, 100, 10));
  mazeWalls.push(new Wall(150, 50, 10, 150));
  mazeWalls.push(new Wall(200, 50, 10, 100));
  mazeWalls.push(new Wall(200, 50, 100, 10));
  mazeWalls.push(new Wall(300, 50, 10, 150));
  mazeWalls.push(new Wall(240, 150, 60, 10));
  mazeWalls.push(new Wall(300, 150, 10, 90));
  mazeWalls.push(new Wall(250, 240, 60, 10));
  mazeWalls.push(new Wall(250, 240, 10, 100));
  mazeWalls.push(new Wall(250, 340, 100, 10));
  mazeWalls.push(new Wall(150, 200, 10, 60));
  mazeWalls.push(new Wall(150, 200, 90, 10));
  mazeWalls.push(new Wall(150, 290, 10, 100));
  mazeWalls.push(new Wall(50, 290, 10, 100));
  mazeWalls.push(new Wall(200, 290, 10, 100));
}
```


#### micro sesion 4: cierre

En esta sesion pude finalizar la experimentacion de las paredes del laberinto y ya dejar listo el canvas del mismo. 






## SEMANA 9



### Sesión 1: lunes marzo 18


#### micro sesion 1: apertura

En esta sesion tengo planeado empezar a hacer pruebas con el micro bit y experimentar un poco en el proceso. 



#### micro sesion 2:

Estuve haciendo pruebas con el microbot en clase con el codigo que tengo documentado en mi bitacora de la microsesion 3 de la sesion 3 de la semana 7 pero me sale un error que no entiendo cual es 

![image](https://github.com/jfUPB/bitacorassfi12024-10-sebas890p/assets/110270011/b8be0ec4-071b-4cbb-b8d5-98d032866e85)

Estuve buscando la solucion de este error en la pagina suferida por p5.js y en otras que busque por mi cuenta pero no encontre solucion. 



#### micro sesion 3:

siguiendo con la microseion anterior entonces intento hacerlo con el codigo que esta propuesto por el profesor en la documentacion de la unidad 2 pero me aparece el mismo error 


![image](https://github.com/jfUPB/bitacorassfi12024-10-sebas890p/assets/110270011/9d9592e7-baac-4cc7-9939-57f3b6ed0572)






#### micro sesion 4: cierre






### Sesión 2: miercoles marzo 20




#### micro sesion 1: apertura




#### micro sesion 2:





#### micro sesion 3:





#### micro sesion 4: cierre

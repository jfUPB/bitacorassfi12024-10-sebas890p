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



#### micro sesion 3:




#### micro sesion 4:cierre




### Sesión 2: miercoles marzo 6



#### micro sesion 1: apertura


#### micro sesion 2:


#### micro sesion 3:



#### micro sesion 4: cierre






### Sesión 3: jueves marzo 7

#### micro sesion 1: apertura


#### micro sesion 2:


#### micro sesion 3:



#### micro sesion 4: cierre







## SEMANA 8



### Sesión 1: lunes marzo 11


#### micro sesion 1: apertura



#### micro sesion 2:



#### micro sesion 3:



#### micro sesion 4: cierre
 

### Sesión 2: miercoles marzo 11



#### micro sesion 1: apertura


#### micro sesion 2:


#### micro sesion 3:



#### micro sesion 4: cierre

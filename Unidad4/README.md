# Bitácora de aprendizaje

## Comprometerse

**¿Qué quieres lograr con la aplicación?**

> Con la aplicacion busco lograr que se pueda crear arte pintando el lienzo de p5.js de una forma interactiva usando el microbit como controlador medianto movimientos, de una forma mas detallada busco lograr que al mover el controlador microbit funcione como un pincel.
> 

**¿Qué tipo de interacción con el usuario deseas que tenga la aplicación?**

> El usuario va a interactuar con la aplicacion mediante el microbit, que lo usara como controlador presionando los botones para cambiar de color y moviendolo para pintar en el lienzo.
> 

**¿Qué tipo de sensores y actuadores del micro:bit deseas usar?**

> Deseo usar el ecelerometro para asi poder pintar moviendo el microbit y usar los actuadores A y B para asi cambiar de color.
> 

**¿Qué tipo de protocolo de comunicación deseas usar?**

>  Por eventos 
> 


**¿Cómo será la arquitectura de la comunicación entre el micro:bit y p5.js?**

> ASCII
> 


**¿Qué tipo de algoritmo deseas implementar en el hilo secundario?**

> En el hilo secundario se implemtaria el poder cambiar de color.
> 

**¿Qué tipo de animación deseas mostrar en el hilo principal?**

> El hilo principal se mostraria la animacion de como va pintando el pincel mientras el usuario lo va moviendo.
> 

## Investigar 

* Enlace a una animación interactiva en p5.js, propuesta por ti y diferente a los ejemplos que te mostré, que se bloquee debido a una operación computacionalmente intensiva.

Enlace: https://editor.p5js.org/sebas890p/sketches/2VGxRL_0c

Esta operacion computacional intensiva realiza operaciones de potenciación entre números aleatorios, se está calculando la potencia de un número aleatorio elevado a otra potencia aleatoria, lo que implica operaciones exponenciales y aleatorias




* Enlace a una animación interactiva en p5.js que solucione la aplicación anterior utilizando un hilo (web worker).


Enlace: https://editor.p5js.org/sebas890p/sketches/2VGxRL_0c


cuando se hace clic en el círculo se inicia un Web Worker que ejecuta la función HeavyComputation lo que permite que la animación siga funcionando sin bloqueos cuando la computación del Web Worker ha terminado se envía un mensaje al hilo principal para indicar que ya termino y la variable isProcessing se establece en false, lo que permite que se realicen más cálculos si es necesario


* Enlace a una aplicación en p5.js que modifique el hilo secundario del **caso de estudio** de la actividad 7 que permite cambiar de manera aleatoria el color y tamaño de cada partícula.

enlace: https://editor.p5js.org/sebas890p/sketches/IilqwsvDf


En el código del sketch, agrege dos nuevas propiedades a la clase Particle color y size. Estas propiedades se inicializan con valores predeterminados en el constructor.
En el método display() de la clase Particle, se utiliza la propiedad color para establecer el color de la partícula y la propiedad size para determinar el tamaño de la elipse.
En el código del worker (Tarea.js), agrege dos nuevas líneas dentro del bucle forEach en la función calculateForces. La primera línea establece un color aleatorio para cada partícula utilizando la función color de p5.js y valores aleatorios para rojo, verde y azul. La segunda línea establece un tamaño aleatorio para cada partícula entre 10 y 30

Sin embargo no se que puede estar fallando que al hacer click sobre el lienzo no se esta cambiando de color



## Aplicar

* Enlace a la aplicación interativa en p5.js que resuelve el reto

## Compartir

**¿En qué consiste la aplicación que diseñaste e implementaste?**

> Escribe aquí
> 

**Explica el protocolo de integración entre p5.js y el micro:bit.**

> Escribe aquí
> 

**Explica la arquitectura de la comunicación entre el micro:bit y p5.js.**

> Escribe aquí
> 

**Explica el algoritmo que implementaste en el hilo secundario.**

> Escribe aquí
> 


**Enlace a un video en youtube con la demostración de tu aplicación**


**¿Qué aprendiste en esta unidad?**

> Escribe aquí
> 

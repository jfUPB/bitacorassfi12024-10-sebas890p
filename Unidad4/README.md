# Bitácora de aprendizaje

## Comprometerse

**¿Qué quieres lograr con la aplicación?**

> Escribe aquí
> 

**¿Qué tipo de interacción con el usuario deseas que tenga la aplicación?**

> Escribe aquí
> 

**¿Qué tipo de sensores y actuadores del micro:bit deseas usar?**

> Escribe aquí
> 

**¿Qué tipo de protocolo de comunicación deseas usar?**

> Escribe aquí
> 


**¿Cómo será la arquitectura de la comunicación entre el micro:bit y p5.js?**

> Escribe aquí
> 


**¿Qué tipo de algoritmo deseas implementar en el hilo secundario?**

> Escribe aquí
> 

**¿Qué tipo de animación deseas mostrar en el hilo principal?**

> Escribe aquí
> 

## Investigar 

* Enlace a una animación interactiva en p5.js, propuesta por ti y diferente a los ejemplos que te mostré, que se bloquee debido a una operación computacionalmente intensiva.

Enlace: https://editor.p5js.org/sebas890p/sketches/2VGxRL_0c

Esta operacion computacional intensiva realiza operaciones de potenciación entre números aleatorios, se está calculando la potencia de un número aleatorio elevado a otra potencia aleatoria, lo que implica operaciones exponenciales y aleatorias




* Enlace a una animación interactiva en p5.js que solucione la aplicación anterior utilizando un hilo (web worker).


Enlace: https://editor.p5js.org/sebas890p/sketches/2VGxRL_0c


cuando se hace clic en el círculo se inicia un Web Worker que ejecuta la función HeavyComputation lo que permite que la animación siga funcionando sin bloqueos cuando la computación del Web Worker ha terminado se envía un mensaje al hilo principal para indicar que ya termino y la variable isProcessing se establece en false, lo que permite que se realicen más cálculos si es necesario


* Enlace a una aplicación en p5.js que modifique el hilo secundario del **caso de estudio** de la actividad 7 que permite cambiar de manera aleatoria el color y tamaño de cada partícula.

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

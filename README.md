Hay dos prácticas en el repositorio:

----------------------------------Prácticas de hilos----------------------------------
que incluye dos archivos:
1.- practica1.py, el cual es la práctica de hilos incluyendo los locks.
  el resultado de correr este archivo debe ser un saldo positivo.

2.- practica1a mostrando qué hilo tiene lock.py, el cual es el mismo archivo, pero editado para responder esta pregunta:
    Ejercicios para el Estudiante: Modificar el código para que muestre qué hilo obtiene el lock
=====================================================================
Los archivos proceso.py, proceso2.py, proceso3.py son otros arhivos de las actividades en clase, no tiene nada que ver con las prácticas 1 o 2.
=====================================================================

----------------------------------Práctica de procesos------------------------------------

PRÁCTICA 2: PROCESOS E HILOS – PROCESAMIENTO DE IMÁGENES DISTRIBUIDO
=====================================================================

DESCRIPCIÓN GENERAL
-------------------
Este proyecto tiene como objetivo entender cómo los procesos y los hilos trabajan en paralelo y cómo se comunican entre sí en Python. 
Se simula el procesamiento de varias imágenes al mismo tiempo, aplicando tres enfoques distintos:
1. Procesos individuales con multiprocessing.Process
2. Pool de procesos con multiprocessing.Pool
3. Hilos con threading.Thread

Cada versión mide el tiempo total, los PIDs de los procesos o hilos y muestra una barra de progreso compartida actualizada conforme se procesan las imágenes.

---------------------------------------------------------------------

ESTRUCTURA DEL PROYECTO
------------------------
Practica2
├── practica2.py     → Versión con procesos individuales y barra compartida
├── proc_pool.py             → Versión con multiprocessing.Pool
├── proc_threads.py          → Versión con hilos

---------------------------------------------------------------------

FUNCIONAMIENTO
---------------
Cada script procesa una lista de imágenes simuladas, calculando un “tamaño resultante” en función del nombre del archivo y un tiempo de espera proporcional (simulando carga de CPU o I/O).

El objetivo es observar:
- Los PIDs diferentes generados por los procesos.
- Cómo los procesos comparten datos mediante multiprocessing.Value.
- La diferencia entre procesos y hilos en rendimiento y uso de memoria.

La barra de progreso usa un contador compartido (Value o diccionario con Lock) que todos los procesos o hilos actualizan a medida que completan una imagen.

---------------------------------------------------------------------

CÓMO EJECUTAR
--------------
Abre una terminal dentro de la carpeta del proyecto y ejecuta:

python practica2.py     # Versión con procesos individuales
python proc_pool.py             # Versión con Pool de procesos
python proc_threads.py          # Versión con hilos

---------------------------------------------------------------------

RESULTADOS ESPERADOS
--------------------
- Se imprimirán los PIDs de los procesos creados.
- La barra de progreso irá avanzando conforme se completan las tareas.
- Se mostrará un resumen final con:
  * Número total de imágenes procesadas
  * Tiempo total vs estimado secuencial
  * Tamaño resultante de cada imagen

---------------------------------------------------------------------

CONCLUSIONES
-------------
En tareas con esperas (time.sleep), los hilos suelen rendir igual o mejor que los procesos porque comparten memoria y no requieren comunicación entre espacios de memoria separados.
Sin embargo, para tareas intensivas en CPU, los procesos son más eficientes ya que no están limitados por el GIL (Global Interpreter Lock).
Este ejercicio demuestra las ventajas y costos de cada modelo de concurrencia en Python.

---------------------------------------------------------------------

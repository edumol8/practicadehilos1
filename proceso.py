import multiprocessing
import threading
import time
from threading import Lock
lock = Lock()
# Variable Global
contador = 0

def incrementar_con_hilo():
    global contador
    for _ in range(100000):
        with lock: #para evitar condiciones de carrera
            contador += 1
    print(f"Hilo - Contador final: {contador}")

def ejecutar_hilos():
    global contador
    contador = 0 # Reiniciar
    t1 = threading.Thread(target=incrementar_con_hilo)
    t2 = threading.Thread(target=incrementar_con_hilo)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(f"\nResultado de HILOS (Compartido): {contador} (¡Error de Concurrencia!)")

# ---

def incrementar_con_proceso(contador_local):
    # La variable local es una COPIA, no la global
    for _ in range(100000):
        contador_local += 1
    # print(f"Proceso - Contador final (local): {contador_local}") 
    # Para el ejercicio, solo devolveremos el resultado para demostrar el aislamiento.
    return contador_local

def ejecutar_procesos():
    global contador
    contador = 0 # La variable global NO será afectada
    
    # Pool para gestionar los procesos (simplemente los iniciamos)
    p1 = multiprocessing.Process(target=incrementar_con_proceso, args=(contador,))
    p2 = multiprocessing.Process(target=incrementar_con_proceso, args=(contador,))
    
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    
    print(f"\nResultado de PROCESOS (Aislado): {contador} (La variable original NO cambió)")
    print("Nota: Cada proceso trabajó en su propia copia de 'contador'.")


if __name__ == '__main__':
    ejecutar_hilos()
    ejecutar_procesos()
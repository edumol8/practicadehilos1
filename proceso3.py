import multiprocessing
import threading
import time
import math

def tarea_cpu(n):
    # Cálculo intensivo (ej. encontrar la raíz cuadrada)
    _ = [math.sqrt(i) for i in range(n)]

if __name__ == '__main__':
    N_ITERACIONES = 10000000 
    
    # 1. Ejecución con Hilos (threading)
    inicio_hilos = time.perf_counter()
    t1 = threading.Thread(target=tarea_cpu, args=(N_ITERACIONES,))
    t2 = threading.Thread(target=tarea_cpu, args=(N_ITERACIONES,))
    t1.start(); t2.start()
    t1.join(); t2.join()
    fin_hilos = time.perf_counter()
    
    # 2. Ejecución con Procesos (multiprocessing)
    inicio_proc = time.perf_counter()
    p1 = multiprocessing.Process(target=tarea_cpu, args=(N_ITERACIONES,))
    p2 = multiprocessing.Process(target=tarea_cpu, args=(N_ITERACIONES,))
    p1.start(); p2.start()
    p1.join(); p2.join()
    fin_proc = time.perf_counter()
    
    print(f"\nTiempo HILOS (CPU-Bound): {fin_hilos - inicio_hilos:.2f} segundos")
    print(f"Tiempo PROCESOS (CPU-Bound): {fin_proc - inicio_proc:.2f} segundos")
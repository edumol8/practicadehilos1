import threading
import time

def tarea_io(id_tarea):
    print(f"Tarea {id_tarea}: Iniciando I/O...")
    time.sleep(2) # Simula espera de red o disco
    print(f"Tarea {id_tarea}: I/O completada.")

if __name__ == '__main__':
    tareas = [1, 2, 3, 4]
    inicio = time.perf_counter()
    
    hilos = []
    for t in tareas:
        h = threading.Thread(target=tarea_io, args=(t,))
        hilos.append(h)
        h.start()
        
    for h in hilos:
        h.join()
        
    fin = time.perf_counter()
    print(f"\nTiempo total (HILOS en I/O): {fin - inicio:.2f} segundos")
import multiprocessing as mp
import threading
import time
import os
import sys

class ProcesadorImagenes:
    def __init__(self, contador_compartido):
        self.imagenes_procesadas = contador_compartido  # mp.Value('i', 0)

    def procesar_imagen(self, nombre_imagen, resultado_compartido):
        print(f"Procesando {nombre_imagen} en proceso {os.getpid()}")
        # Simular trabajo intensivo (CPU/I-O simulado)
        tiempo_procesamiento = len(nombre_imagen) * 0.2
        time.sleep(tiempo_procesamiento)

        # Resultado del procesamiento (simulado)
        tam_resultante = len(nombre_imagen) * 100
        resultado_compartido.value = tam_resultante

        # Contador compartido entre procesos
        with self.imagenes_procesadas.get_lock():
            self.imagenes_procesadas.value += 1

        print(f"{nombre_imagen} procesada. Tamaño: {tam_resultante}KB")
        return tam_resultante

def worker_procesar(procesador, nombre_imagen, resultado):
    procesador.procesar_imagen(nombre_imagen, resultado)

def barra_progreso(hechas_value, total):
    # Dibuja una barra leyendo el Value compartido
    ancho = 30
    while hechas_value.value < total:
        hechas = hechas_value.value
        llenos = int(ancho * hechas / total)
        barra = "█" * llenos + "-" * (ancho - llenos)
        print(f"\rProgreso: [{barra}] {hechas}/{total}", end="", flush=True)
        time.sleep(0.1)
    # cierre al llegar al total
    barra = "█" * ancho
    print(f"\rProgreso: [{barra}] {total}/{total}")

def main():
    print(f"PID padre (main): {os.getpid()}")
    imagenes = ["foto_familia.jpg", "selfie.png", "paisaje.tiff", "documento.pdf", "captura_pantalla.png", "memes.jpg"]
    total = len(imagenes)

    contador = mp.Value('i', 0)
    procesador = ProcesadorImagenes(contador)

    procesos = []
    resultados = []
    pids_hijos = []

    print("Iniciando procesamiento distribuido de imágenes...")
    inicio = time.time()

    # Hilo que pinta barra leyendo el Value compartido
    t_barra = threading.Thread(target=barra_progreso, args=(contador, total), daemon=True)
    t_barra.start()

    # Crear procesos para cada imagen
    for i, imagen in enumerate(imagenes):
        resultado = mp.Value('i', 0)
        resultados.append(resultado)
        p = mp.Process(target=worker_procesar, args=(procesador, imagen, resultado))
        procesos.append(p)
        p.start()
        pids_hijos.append(p.pid)

    # Mostrar PIDs hijos
    print("PIDs hijos lanzados:", pids_hijos)

    # Esperar a que todos terminen
    for p in procesos:
        p.join()

    tiempo_total = time.time() - inicio

    # Recopilar resultados
    print(f"\nRESUMEN FINAL:")
    print(f"Imágenes procesadas: {contador.value}")
    print(f"Tiempo total: {tiempo_total:.2f} s")
    print(f"Tiempo secuencial estimado: {sum(len(img) for img in imagenes) * 0.2:.2f} s")
    for imagen, resultado in zip(imagenes, resultados):
        print(f"  {imagen}: {resultado.value}KB")

if __name__ == '__main__':
    # En Windows es clave mantener este guard
    mp.set_start_method("spawn", force=True)
    main()

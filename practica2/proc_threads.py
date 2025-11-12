import threading
import time
import os

def _print_bar(done, total, width=30):
    filled = int(width * done / total)
    bar = "█" * filled + "-" * (width - filled)
    print(f"\rProgreso (threads): [{bar}] {done}/{total}", end="", flush=True)

def worker_thread(nombre_imagen, contador, lock, resultados):
    # Simulación
    time.sleep(len(nombre_imagen) * 0.2)
    tam = len(nombre_imagen) * 100
    with lock:
        resultados[nombre_imagen] = tam
        contador["hechas"] += 1
        _print_bar(contador["hechas"], contador["total"])
    print(f"\n{nombre_imagen} procesada en hilo (PID proceso {os.getpid()}). Tamaño: {tam}KB")

def main():
    imagenes = ["foto_familia.jpg", "selfie.png", "paisaje.tiff", "documento.pdf", "captura_pantalla.png", "memes.jpg"]
    total = len(imagenes)

    lock = threading.Lock()
    resultados = {}
    contador = {"hechas": 0, "total": total}

    print(f"PID único (threads corren dentro del mismo proceso): {os.getpid()}")
    print("Iniciando hilos...")
    inicio = time.time()

    hilos = []
    for img in imagenes:
        t = threading.Thread(target=worker_thread, args=(img, contador, lock, resultados))
        t.start()
        hilos.append(t)

    for t in hilos:
        t.join()

    tiempo_total = time.time() - inicio
    print()  # salto línea barra
    print("\nRESUMEN FINAL (Threads):")
    print(f"Imágenes procesadas: {len(resultados)}")
    print(f"Tiempo total: {tiempo_total:.2f} s")
    for img in imagenes:
        print(f"  {img}: {resultados[img]}KB")

if __name__ == "__main__":
    main()

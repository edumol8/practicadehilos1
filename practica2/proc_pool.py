import multiprocessing as mp
import time
import os

# Globals que inicializa el Pool
_g_contador = None

def _init_pool(contador):
    global _g_contador
    _g_contador = contador

def _pool_worker(nombre_imagen):
    pid = os.getpid()
    # Simulación
    time.sleep(len(nombre_imagen) * 0.2)
    tam = len(nombre_imagen) * 100
    # Actualizar contador compartido entre procesos del Pool
    with _g_contador.get_lock():
        _g_contador.value += 1
    print(f"Procesando {nombre_imagen} en proceso {pid}")
    print(f"{nombre_imagen} procesada. Tamaño: {tam}KB")
    return (nombre_imagen, tam, pid)

def _print_bar(done, total, width=30):
    filled = int(width * done / total)
    bar = "█" * filled + "-" * (width - filled)
    print(f"\rProgreso: [{bar}] {done}/{total}", end="", flush=True)

def main():
    imagenes = ["foto_familia.jpg", "selfie.png", "paisaje.tiff", "documento.pdf", "captura_pantalla.png", "memes.jpg"]
    total = len(imagenes)

    contador = mp.Value('i', 0)

    print(f"PID padre (main): {os.getpid()}")
    print("Iniciando Pool...")
    inicio = time.time()

    resultados = []
    done_local = 0

    with mp.Pool(processes=os.cpu_count(), initializer=_init_pool, initargs=(contador,)) as pool:
        for nombre, tam, pid in pool.imap_unordered(_pool_worker, imagenes):
            resultados.append((nombre, tam, pid))
            done_local += 1
            # Barra basada en el contador compartido (o en done_local si prefieres)
            _print_bar(contador.value, total)

    tiempo_total = time.time() - inicio
    print()  # salto línea barra

    print("\nRESUMEN FINAL (Pool):")
    print(f"Imágenes procesadas: {contador.value}")
    print(f"Tiempo total: {tiempo_total:.2f} s")
    print(f"PIDs usados: {sorted({pid for _, _, pid in resultados})}")
    for nombre, tam, _ in resultados:
        print(f"  {nombre}: {tam}KB")

if __name__ == "__main__":
    mp.set_start_method("spawn", force=True)
    main()

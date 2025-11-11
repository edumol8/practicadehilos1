import threading
import time
import random
from threading import Lock
lock = Lock()

class Banco:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial
        self.lock = threading.Lock()

    def retirar(self, cantidad):
        hilo = threading.current_thread().name
        print(f"{hilo} intentando obtener el lock...")

        t0 = time.time()
        self.lock.acquire()
        print(f"[LOCK ✅] {hilo} obtuvo el lock")

        try:
            print(f"{hilo} intenta retirar ${cantidad}")
            if self.saldo >= cantidad:
                # Simular procesamiento
                time.sleep(0.1)
                self.saldo -= cantidad
                print(f"{hilo} retiró ${cantidad}. Saldo restante: ${self.saldo}")
                return True
            else:
                print(f"{hilo} - Fondos insuficientes")
                return False
        finally:
            dt = time.time() - t0
            self.lock.release()
            print(f"[UNLOCK 🔓] {hilo} liberó el lock (lo tuvo {dt:.3f}s)\n")

def cliente(banco, retiros):
    for _ in range(retiros):
        cantidad = random.randint(50, 200)
        banco.retirar(cantidad)
        time.sleep(random.uniform(0.1, 0.3))

# Configuración
saldo_inicial = 1000
num_clientes = 5
retiros_por_cliente = 4

banco = Banco(saldo_inicial)
hilos = []

print(f"Saldo inicial: ${saldo_inicial}")

# Crear hilos con nombre legible
for i in range(num_clientes):
    hilo = threading.Thread(
        target=cliente,
        args=(banco, retiros_por_cliente),
        name=f"Cliente-{i+1}"
    )
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()

print(f"\nSaldo final: ${banco.saldo}")
promedio = 125  # promedio usado para referencia
print(f"Saldo teórico esperado: ${saldo_inicial - (num_clientes * retiros_por_cliente * promedio)}")

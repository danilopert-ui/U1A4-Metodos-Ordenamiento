import timeit
import random
import statistics
from algoritmos import bubble_sort, quicksort

def generar_datos(tamano, tipo):
    """Genera listas de prueba según el escenario."""
    if tipo == "aleatoria":
        return [random.randint(0, 100000) for _ in range(tamano)]
    elif tipo == "invertida":
        # Lista ordenada inversamente (el peor caso para muchos algoritmos)
        return list(range(tamano, 0, -1))

def evaluar_rendimiento():
    tamanos = [100, 1000, 5000, 10000] # Tamaños solicitados
    escenarios = ["aleatoria", "invertida"]
    repeticiones = 5

    print(f"{'Tamaño':<10} | {'Escenario':<10} | {'Algoritmo':<12} | {'Tiempo Promedio (s)':<20} | {'Desviación Estándar':<20}")
    print("-" * 85)

    for tamano in tamanos:
        for escenario in escenarios:
            # Generamos la lista base
            lista_base = generar_datos(tamano, escenario)

            # --- Evaluar Bubble Sort ---
            # Nota: Para 10,000 datos, Bubble Sort tardará bastante. Ten paciencia.
            if tamano <= 10000: # Proteccion: Bubble sort en 10k puede tardar mucho
                tiempos_bubble = timeit.repeat(lambda: bubble_sort(lista_base), repeat=repeticiones, number=1)
                promedio_bubble = statistics.mean(tiempos_bubble)
                std_bubble = statistics.stdev(tiempos_bubble)
                print(f"{tamano:<10} | {escenario:<10} | {'Burbuja':<12} | {promedio_bubble:.6f} s           | {std_bubble:.6f}")
            
            # --- Evaluar Quicksort ---
            tiempos_quick = timeit.repeat(lambda: quicksort(lista_base), repeat=repeticiones, number=1)
            promedio_quick = statistics.mean(tiempos_quick)
            std_quick = statistics.stdev(tiempos_quick)
            print(f"{tamano:<10} | {escenario:<10} | {'Quicksort':<12} | {promedio_quick:.6f} s           | {std_quick:.6f}")

if __name__ == "__main__":
    print("Iniciando pruebas de rendimiento... (Esto puede tardar unos minutos)")
    evaluar_rendimiento()
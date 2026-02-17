import sys

# Aumentamos el límite de recursión para listas grandes (necesario para Quicksort en listas de 10,000 items)
sys.setrecursionlimit(20000)

def bubble_sort(lista):
    """
    Implementación del método de Burbuja.
    Complejidad: O(n^2).
    Compara elementos adyacentes y los intercambia si están en el orden incorrecto.
    """
    n = len(lista)
    # Hacemos una copia para no modificar la lista original fuera de la función
    lista_ordenada = lista.copy()
    
    for i in range(n):
        # Optimización: Si no hubo intercambios en una pasada, ya está ordenado
        intercambio = False
        for j in range(0, n - i - 1):
            if lista_ordenada[j] > lista_ordenada[j + 1]:
                lista_ordenada[j], lista_ordenada[j + 1] = lista_ordenada[j + 1], lista_ordenada[j]
                intercambio = True
        if not intercambio:
            break
            
    return lista_ordenada

def quicksort(lista):
    """
    Implementación de Quicksort (Recursivo).
    Complejidad promedio: O(n log n).
    Justificación de elección recursiva: 
    Es más legible y matemáticamente inductiva ("divide y vencerás").
    Aunque consume memoria de pila (stack), es eficiente para los tamaños solicitados.
    """
    if len(lista) <= 1:
        return lista
    else:
        # Elegimos el primer elemento como pivote (simple, aunque mejorable con pivote aleatorio)
        pivote = lista[0]
        menores = [x for x in lista[1:] if x <= pivote]
        mayores = [x for x in lista[1:] if x > pivote]
        return quicksort(menores) + [pivote] + quicksort(mayores)
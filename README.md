# U1A4 – Evaluación de Métodos de Ordenamiento en Python

**Autor:** Angel Daniel Cisneros Perez  
**Carrera:** Ingeniería Mecatrónica  
**Asignatura:** Programación Avanzada  
**Actividad:** U1A4 – Reporte de Programa (Evaluación de Métodos de Ordenamiento)

---

## 📌 Descripción del Proyecto

Este proyecto implementa y evalúa empíricamente dos algoritmos clásicos de ordenamiento en Python:

- 🔵 **Bubble Sort (Burbuja)**
- 🟢 **Quicksort (Recursivo)**

El propósito principal es comparar su rendimiento bajo diferentes tamaños de entrada y escenarios de datos, validando experimentalmente la complejidad algorítmica teórica:

- **Bubble Sort → O(n²)**
- **Quicksort → O(n log n)** (en promedio)

Las pruebas se realizaron utilizando la librería estándar `timeit` para medir tiempos de ejecución, promedio y desviación estándar, permitiendo un análisis cuantitativo y reproducible.

---

## Objetivos Técnicos

- Implementar algoritmos de ordenamiento desde cero.
- Medir rendimiento con metodología experimental controlada.
- Analizar escalabilidad empírica.
- Relacionar resultados con la complejidad teórica.
- Aplicar buenas prácticas de organización y documentación en GitHub.

---

## 🗂️ Estructura del Repositorio

```
U1A4_ORDENAMIENTO/
│
├── src/
│   ├── algoritmos.py      # Implementaciones de Bubble Sort y Quicksort
│   ├── main.py            # Script principal de pruebas de rendimiento
│
├── docs/
│   ├── U1A4_Cisneros_AngelDaniel.pdf   # Reporte final
│   
│
├── README.md
└── .gitignore
```

Esta estructura separa claramente código fuente y documentación, facilitando mantenibilidad y publicación profesional.

---

## ⚙️ Requisitos

- Python **3.10 o superior**
- Librerías estándar:
  - `timeit`
  - `random`
  - `statistics`
  - `sys`

No se requieren dependencias externas adicionales.

---

## Cómo Ejecutar el Programa

Desde la carpeta raíz del proyecto:

```bash
python src/main.py
```

El programa:

- Genera listas de distintos tamaños.
- Ejecuta 5 repeticiones por tamaño y escenario.
- Calcula tiempo promedio y desviación estándar.
- Muestra los resultados en consola en formato tabular.

---

## 📊 Configuración de Pruebas

### Tamaños evaluados

- 100
- 1 000
- 5 000
- 10 000

### Escenarios considerados

- 🔹 Lista aleatoria  
- 🔹 Lista invertida (caso estructural desfavorable)

### Metodología

- 5 repeticiones por combinación.
- Medición con `timeit.repeat`.
- Cálculo de promedio y desviación estándar.
- Mismos datos base por algoritmo para garantizar comparabilidad.

---

## 📈 Resumen de Resultados

### 🔹 Escenario Aleatorio (10 000 elementos)

| Algoritmo  | Tiempo Promedio |
|------------|----------------|
| Burbuja    | ~5.5 s         |
| Quicksort  | ~0.019 s       |

**Quicksort es aproximadamente 280 veces más rápido en este escenario.**

---

### 🔹 Escenario Invertido (10 000 elementos)

| Algoritmo  | Tiempo Promedio |
|------------|----------------|
| Burbuja    | ~6.65 s        |
| Quicksort  | ~3.69 s        |

En lista invertida, Quicksort se degrada debido a la selección del primer elemento como pivote, acercándose a su peor caso teórico O(n²).

---

## 🔬 Análisis Técnico

### 1️⃣ Escalabilidad

Bubble Sort presenta crecimiento cuadrático O(n²), lo que provoca un incremento significativo del tiempo conforme aumenta el tamaño de la lista.

Quicksort mantiene un comportamiento cercano a O(n log n) en escenarios promedio, lo que explica su superioridad en conjuntos grandes.

### 2️⃣ Influencia del Pivote en Quicksort

La implementación utiliza el primer elemento como pivote.  
En listas invertidas, esta decisión produce particiones desbalanceadas, lo que incrementa considerablemente el tiempo de ejecución.

**Posibles mejoras futuras:**

- Pivote aleatorio.
- Estrategia mediana de tres.
- Implementación híbrida con Insertion Sort para sublistas pequeñas.

---

## Aplicación en Robótica

En sistemas robóticos y aplicaciones en tiempo real:

- Mayor eficiencia → menor latencia.
- Mejor tiempo de respuesta → decisiones más rápidas.
- Procesamiento eficiente de sensores → mayor frecuencia de actualización.

Elegir algoritmos adecuados impacta directamente el desempeño del sistema y la estabilidad del control.

---

## Posibles Mejoras Futuras

- Implementar Quicksort con pivote aleatorio.
- Comparar con Merge Sort o TimSort.
- Generar gráficas automáticas con matplotlib.
- Exportar resultados a CSV para análisis adicional.

---

## Evidencias Incluidas

- Captura de estructura del proyecto en VS Code.
- Captura de ejecución en consola.
- Tabla completa de resultados.
- Reporte formal en PDF dentro de `docs/`.

---

## Conclusión General

Los resultados experimentales confirman que Quicksort supera ampliamente a Bubble Sort en escenarios promedio, validando la teoría de complejidad algorítmica. Sin embargo, la selección del pivote influye significativamente en el rendimiento, pudiendo provocar degradaciones en entradas estructuradas.

Esta práctica refuerza la importancia del análisis empírico como complemento del análisis teórico y demuestra cómo decisiones algorítmicas impactan directamente en el rendimiento de sistemas reales, especialmente en aplicaciones de ingeniería y robótica.

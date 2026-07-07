# TPE_4-GRUPO-M-
# Simulador de Señales U3 - UNEMI

## Descripción

Este proyecto consiste en un simulador desarrollado en Python que representa el proceso de transmisión de información en la capa física de una red de comunicaciones. La aplicación permite visualizar cómo un mensaje de texto es convertido en datos digitales y posteriormente representado mediante una señal analógica, relacionando cada etapa con ejemplos de aplicaciones reales de las telecomunicaciones.

El simulador fue desarrollado como parte del Proyecto Integrador de la asignatura **Comunicación de Datos** de la **Universidad Estatal de Milagro (UNEMI)**.

---

## Características

- Interfaz gráfica desarrollada con Tkinter.
- Conversión de caracteres a representación binaria (ASCII).
- Visualización de la señal digital.
- Simulación de una señal analógica mediante ondas sinusoidales.
- Registro de eventos y procesamiento en una consola integrada.
- Relación de cada transmisión con casos reales de comunicación.
- Validación de la entrada del usuario.
- Reinicio completo de la simulación.

---

## Tecnologías utilizadas

- Python 3
- Tkinter
- Matplotlib
- NumPy

---

## Requisitos

Antes de ejecutar el proyecto es necesario instalar las dependencias.

```bash
pip install matplotlib numpy
```

Tkinter normalmente viene instalado con Python.

---

## Ejecución

Descargue o clone el repositorio y ejecute el archivo principal.

```bash
python "TPE_4 GRUPO M.py"
```

---

## Funcionamiento

1. Ingresar un mensaje de texto.
2. Presionar el botón **Iniciar Transmisión**.
3. El sistema convierte cada carácter a código binario.
4. Se muestra la representación digital del carácter.
5. Se genera una representación analógica de la señal.
6. La consola presenta información sobre aplicaciones reales y fundamentos teóricos relacionados con la transmisión de datos.
7. Al finalizar, el sistema informa que la transmisión fue completada correctamente.

---

## Estructura del proyecto

```
Proyecto/
│
├── TPE_4 GRUPO M.py
└── README.md
```

---

## Conceptos aplicados

El simulador implementa conceptos fundamentales de la asignatura Comunicación de Datos, entre ellos:

- Representación digital de la información.
- Conversión de caracteres ASCII a binario.
- Señales digitales y analógicas.
- Transmisión de datos.
- Capa Física del modelo OSI.
- Teorema de Nyquist.
- Ancho de banda.
- Relación Señal/Ruido (SNR).
- Codificación de información.

---

## Equipo de desarrollo

- Calderón Ramón A. I.
- Franco Echeverría J. R.
- Ortega Taza W. J.
- Ramón Valiente M. F.
- Reyes Quijije R. A.
- Valarezo Ruíz G. C.
- Villamar Suárez J. L.

---

## Universidad

**Universidad Estatal de Milagro (UNEMI)**

Asignatura: Comunicación de Datos  
Unidad 3

---

## Licencia

Este proyecto fue desarrollado con fines académicos y educativos.

# 🥗 Buscador de Recetas por Ingredientes
## 👥 Integrantes del proyecto

Rubén Castro Álvarez
María Benedicta Fernández Rodríguez
Mireia Ramón Verdera
Sergio Fernández

---

## 📌 Descripción del proyecto

Este proyecto es una herramienta en Python que permite:

✔️ Buscar recetas a partir de ingredientes introducidos por el usuario
✔️ Seleccionar la receta deseada
✔️ Visualizar los ingredientes necesarios
✔️ Obtener información nutricional completa de la receta
✔️ Obtener información nutricional por ingrediente usando una segunda API
✔️ Integrar dos servicios distintos:

Spoonacular API → Para recetas e información nutricional general

API Ninjas Nutrition → Para nutrición específica de cada ingrediente

El programa funciona por consola y guía al usuario paso a paso desde la búsqueda hasta el análisis nutricional final.

---

## 🚀 Cómo funciona

El usuario introduce una lista de ingredientes (ej: pollo, arroz, tomate).

El programa consulta la API de Spoonacular y devuelve recetas posibles.

El usuario elige una receta.

Se obtiene:

  - Lista de ingredientes

  - Información nutricional completa

  - Información nutricional individual de cada ingrediente

Todo se muestra en formato limpio y ordenado.

---

## 🛠️ Tecnologías utilizadas

Python

requests (librería para peticiones HTTP)

Spoonacular API

API Ninjas Nutrition

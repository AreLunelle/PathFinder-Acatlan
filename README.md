# PathFinder Acatlán  
**Chatbot de rutas internas para estudiantes de nuevo ingreso — Proyecto académico**

Este proyecto fue desarrollado como parte de una actividad escolar para la materia de **Matemáticas Discretas**, con el propósito de aplicar conceptos de grafos mediante la creación de un sistema sencillo de rutas dentro de la FES Acatlán.

El objetivo es ayudar a estudiantes de nuevo ingreso a encontrar caminos entre distintos puntos de la facultad, utilizando una interfaz amigable y un chatbot básico.

---

## Objetivo del proyecto
Implementar un **grafo manual** que represente diversos puntos dentro de la FES Acatlán, y permitir al usuario seleccionar un punto de inicio y destino para obtener una ruta sugerida.

Este proyecto:
- Representa los lugares como **vértices**.  
- Conecta cada punto mediante **aristas** según su cercanía real.  
- Calcula rutas simples basadas en las conexiones definidas por el creador.  
- Utiliza Flask para montar la interfaz y manejar la interacción.

Las rutas se definen a partir de conexiones previamente establecidas, dado que este proyecto tiene fines educativos y de práctica inicial.

---

## Tecnologías utilizadas
- **Python 3**
- **Flask**
- **HTML5**
- **CSS3**
- **Renderizado de plantillas (Jinja2)**
- **Estructuras básicas de grafos en Python**

---

## Estructura del proyecto
PathFinder-Acatlan/
│
├── app.py # Servidor Flask y lógica principal
├── pathfinder_acatlan.py # Grafo y cálculo de rutas
│
├── static/
│ ├── style.css # Estilos del proyecto
│ └── img.jpg # Imagen del robot
│
├── templates/
│ └── index.html # Interfaz principal del chatbot
│
└── README.md

## Autora

Areli Sánchez Alonso
Estudiante de Matemáticas Aplicadas y Computación
FES Acatlán — UNAM

# Trabajo Integrador

Este trabajo integrador muestra la conexión y manejo de tres bases de datos usando Docker y Python: MongoDB, Redis y Neo4j.

## 🔹 Qué es Docker
Docker permite ejecutar aplicaciones en contenedores aislados, con todo lo necesario para que funcionen sin depender de la configuración de la computadora.

## 🔹 Bases de datos usadas
- **MongoDB**: base de datos documental (almacena documentos JSON).  
  Puerto: `27017`
- **Redis**: base de datos clave-valor en memoria, rápida para cache o datos temporales.  
  Puerto: `6379`
- **Neo4j**: base de datos de grafos, útil para relaciones entre nodos.  
  Puertos: `7474` (interfaz web), `7687` (conexión Python)

## 🔹 Estructura del Proyecto
TRABAJO_INTEGRADOR/
│
├── notebooks/                 
│   ├── test_connections.ipynb     # Pruebas de conexión a las bases
│   ├── trabajo_integrador.ipynb   # Desarrollo principal: consultas y gráficos
│   └── data/                      # Archivos JSON con datos iniciales
│       ├── usuarios.json
│       ├── destinos.json
│       ├── hoteles.json
│       ├── actividades.json
│       └── reservas.json
│
├── python/                    
│   ├── Dockerfile               # Imagen base para el entorno
│   └── requirements.txt         # Librerías necesarias para Python
│
├── .env                         # Variables de entorno (usuarios, contraseñas, URIs)
├── .gitignore                   # Exclusiones para control de versiones
├── docker-compose.yml           # Orquestación de servicios (MongoDB, Neo4j, Redis, Jupyter)
└── README.md                    # Documentación inicial     

## 🔹 ¿Cómo levantar el entorno?
- Ejecutar en la raíz del proyecto: docker-compose up

## 🔹 Autores
- Julieta Lujan Iberra Erro
- Daiana Valdez
Fecha de entrega: 29/10/2025

# Tienda Online - Proyecto de Python

## Autor
**Fernando Galán**

## Descripción del Proyecto
Este proyecto implementa una aplicación en Python que simula una tienda online.  
Permite gestionar usuarios (clientes y administradores), manejar inventario, crear pedidos, y ejecutar la lógica del negocio mediante un servicio central (`TiendaService`).  
El archivo `main.py` permite probar las funcionalidades principales como registrar usuarios, crear productos y simular pedidos.

---

#  Uso con Docker

Este proyecto incluye soporte para ejecutar la aplicación dentro de un contenedor Docker.

##  1. Construir la imagen

Desde el directorio raíz del proyecto (donde está el Dockerfile):

```bash
docker build -t tienda-online .

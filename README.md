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
# Construccion de imagen
docker build -t tienda-online 
# Ejecucion Basica
docker run --rm tienda-online
# Salida esperada
Usuarios registrados:
Cliente(id=..., nombre=Ana Pérez, email=ana@example.com)
Cliente(id=..., nombre=Carlos Ruiz, email=carlos@example.com)
Cliente(id=..., nombre=María Gómez, email=maria@example.com)
Administrador(id=..., nombre=Admin Tienda, email=admin@example.com)
------------------------------------------------------------

Inventario inicial:
ProductoElectronico(id=..., nombre=Teléfono X100, stock=10, ...)
ProductoElectronico(id=..., nombre=Portátil Z5, stock=5, ...)
ProductoRopa(id=..., nombre=Camiseta Básica, stock=50, ...)
...
------------------------------------------------------------

Pedido 1 creado:
Pedido(id=..., cliente=Ana Pérez, total=...)
...

from __future__ import annotations
from typing import Dict, List, Optional
from datetime import datetime

from ..models.Producto import Producto, ProductoElectronico, ProductoRopa
from ..models.Usuario import Usuario, Cliente, Administrador
from ..models.Pedido import Pedido


class TiendaService:
    
    def __init__(self) -> None:
        self.usuarios: Dict[str, Usuario] = {}     
        self.productos: Dict[str, Producto] = {}   
        self.pedidos: List[Pedido] = []            
    def registrar_usuario(self, tipo: str, nombre: str, email: str, direccion: Optional[str] = None) -> Usuario:
        tipo = tipo.lower()
        if tipo == "cliente":
            if direccion is None:
                raise ValueError("Para registrar un cliente se requiere 'direccion'.")
            usuario = Cliente(nombre=nombre, email=email, direccion=direccion)
        elif tipo in ("admin", "administrador"):
            usuario = Administrador(nombre=nombre, email=email)
        else:
            raise ValueError("Tipo de usuario no reconocido. Use 'cliente' o 'admin'.")
        self.usuarios[usuario.id] = usuario
        return usuario

    def obtener_usuario(self, usuario_id: str) -> Optional[Usuario]:
        return self.usuarios.get(usuario_id)

    #Productos 
    def anadir_producto(self, producto: Producto) -> None:
        self.productos[producto.id] = producto

    def eliminar_producto(self, producto_id: str) -> bool:
        if producto_id in self.productos:
            del self.productos[producto_id]
            return True
        return False

    def listar_productos(self) -> List[Producto]:
       return list(self.productos.values())

    def obtener_producto(self, producto_id: str) -> Optional[Producto]:
        return self.productos.get(producto_id)

    # ---------- Pedidos ----------
    def realizar_pedido(self, usuario_id: str, items: Dict[str, int]) -> Pedido:
      
        usuario = self.obtener_usuario(usuario_id)
        if usuario is None:
            raise ValueError("El usuario indicado no existe.")
        if not isinstance(usuario, Cliente):
            raise ValueError("Sólo los clientes pueden realizar pedidos.")

        # Preparar diccionario Producto -> cantidad
        prod_items: Dict[Producto, int] = {}
        for pid, cantidad in items.items():
            producto = self.obtener_producto(pid)
            if producto is None:
                raise ValueError(f"Producto con id {pid} no existe.")
            if cantidad <= 0:
                raise ValueError("La cantidad debe ser positiva.")
            if not producto.hay_stock(cantidad):
                raise ValueError(f"No hay suficiente stock para {producto.nombre}. Disponible: {producto.stock}, solicitado: {cantidad}")
            prod_items[producto] = cantidad

        # Si todo OK, descontar stock
        for producto, cantidad in prod_items.items():
            producto.actualizar_stock(cantidad)

        # Crear pedido y guardarlo
        pedido = Pedido(cliente=usuario, items=prod_items)
        self.pedidos.append(pedido)
        self.pedidos.sort(key=lambda p: p.fecha)
        return pedido

    def listar_pedidos_por_usuario(self, usuario_id: str) -> List[Pedido]:
        return [p for p in self.pedidos if p.cliente.id == usuario_id]

    #  Métodos auxiliares para crear productos rápidos 
    def crear_producto_electronico(self, nombre: str, precio: float, stock: int, garantia_meses: int) -> ProductoElectronico:
        p = ProductoElectronico(nombre=nombre, precio=precio, stock=stock, garantia_meses=garantia_meses)
        self.anadir_producto(p)
        return p

    def crear_producto_ropa(self, nombre: str, precio: float, stock: int, talla: str, color: str) -> ProductoRopa:
        p = ProductoRopa(nombre=nombre, precio=precio, stock=stock, talla=talla, color=color)
        self.anadir_producto(p)
        return p

    def crear_producto_generico(self, nombre: str, precio: float, stock: int) -> Producto:
        p = Producto(nombre=nombre, precio=precio, stock=stock)
        self.anadir_producto(p)
        return p

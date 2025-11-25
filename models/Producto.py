from __future__ import annotations
from typing import Any
import uuid
class Producto:
    def __init__(self, nombre: str, precio: float, stock: int) -> None:
        self.id: str = uuid.uuid4().hex
        self.nombre: str = nombre
        self.precio: float = float(precio)
        self.stock: int = int(stock)
    def hay_stock(self, cantidad: int) -> bool:
        return self.stock >= cantidad

    def actualizar_stock(self, cantidad: int) -> None:
       nuevo_stock = self.stock - cantidad
       if nuevo_stock < 0:
            raise ValueError(f"No hay suficiente stock para {self.nombre} (solicitado {cantidad}, disponible {self.stock})")
       self.stock = nuevo_stock

    def __str__(self) -> str:
        return f"[{self.id}] {self.nombre} - Precio: {self.precio:.2f}€ - Stock: {self.stock}"
class ProductoElectronico(Producto):
    def __init__(self, nombre: str, precio: float, stock: int, garantia_meses: int) -> None:
        super().__init__(nombre, precio, stock)
        self.garantia_meses: int = int(garantia_meses)

    def __str__(self) -> str:
        return (f"[{self.id}] {self.nombre} (Electrónico) - Precio: {self.precio:.2f}€ - "
                f"Stock: {self.stock} - Garantía: {self.garantia_meses} meses")
class ProductoRopa(Producto):
    def __init__(self, nombre: str, precio: float, stock: int, talla: str, color: str) -> None:
        super().__init__(nombre, precio, stock)
        self.talla: str = talla
        self.color: str = color
    def __str__(self) -> str:
        return (f"[{self.id}] {self.nombre} (Ropa) - Precio: {self.precio:.2f}€ - "
                f"Stock: {self.stock} - Talla: {self.talla} - Color: {self.color}")
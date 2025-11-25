from __future__ import annotations
from typing import Dict, List, Tuple
from datetime import datetime
import uuid
from .Usuario import Cliente
from .Producto import Producto
class Pedido:
    def __init__(self, cliente: Cliente, items: Dict[Producto, int]) -> None:
        self.id: str = uuid.uuid4().hex
        self.cliente: Cliente = cliente
        self.items: Dict[Producto, int] = dict(items)
        self.fecha: datetime = datetime.now()

    def total(self) -> float:
        total = 0.0
        for producto, cantidad in self.items.items():
            total += producto.precio * cantidad
        return float(total)
    def resumen_items(self) -> str:
        lineas = []
        for producto, cantidad in self.items.items():
            lineas.append(f"{producto.nombre} x{cantidad} - {producto.precio:.2f}€ c/u => {producto.precio * cantidad:.2f}€")
        return "\n".join(lineas)
    def __str__(self) -> str:
        fecha_str = self.fecha.strftime("%Y-%m-%d %H:%M:%S")
        return (
            f"Pedido [{self.id}] - Fecha: {fecha_str}\n"
            f"Cliente: {self.cliente.nombre} ({self.cliente.id})\n"
            f"Total: {self.total():.2f}€\n"
            f"Items:\n{self.resumen_items()}"
        )

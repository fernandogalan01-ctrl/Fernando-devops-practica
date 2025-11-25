
from __future__ import annotations
from typing import Optional
import uuid


class Usuario:
   def __init__(self, nombre: str, email: str) -> None:
        self.id: str = uuid.uuid4().hex
        self.nombre: str = nombre
        self.email: str = email
   def is_admin(self) -> bool:
        return False

   def __str__(self) -> str:
        rol = "Administrador" if self.is_admin() else "Cliente/Usuario"
        return f"[{self.id}] {self.nombre} <{self.email}> - {rol}"


class Cliente(Usuario):
    def __init__(self, nombre: str, email: str, direccion: str) -> None:
        super().__init__(nombre, email)
        self.direccion: str = direccion

    def __str__(self) -> str:
        return f"[{self.id}] {self.nombre} <{self.email}> - Dirección: {self.direccion}"


class Administrador(Usuario):
    
    def __init__(self, nombre: str, email: str) -> None:
        super().__init__(nombre, email)

    def is_admin(self) -> bool:
        return True

    def __str__(self) -> str:
        return f"[{self.id}] {self.nombre} <{self.email}> - Administrador"
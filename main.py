

from Tienda_online.Services.Tienda_service import TiendaService
def main() -> None:
    tienda = TiendaService()

    # Registrar usuarios: 3 clientes y 1 admin
    c1 = tienda.registrar_usuario(tipo="cliente", nombre="Ana Pérez", email="ana@example.com", direccion="Calle Falsa 1")
    c2 = tienda.registrar_usuario(tipo="cliente", nombre="Carlos Ruiz", email="carlos@example.com", direccion="Av. Libertad 5")
    c3 = tienda.registrar_usuario(tipo="cliente", nombre="María Gómez", email="maria@example.com", direccion="Plaza Mayor 3")
    admin = tienda.registrar_usuario(tipo="admin", nombre="Admin Tienda", email="admin@example.com")

    print("Usuarios registrados:")
    print(c1)
    print(c2)
    print(c3)
    print(admin)
    print("-" * 60)

    # Crear 5 productos de diferentes categorías
    p1 = tienda.crear_producto_electronico(nombre="Teléfono X100", precio=399.99, stock=10, garantia_meses=24)
    p2 = tienda.crear_producto_electronico(nombre="Portátil Z5", precio=899.90, stock=5, garantia_meses=12)
    p3 = tienda.crear_producto_ropa(nombre="Camiseta Básica", precio=19.99, stock=50, talla="M", color="Blanco")
    p4 = tienda.crear_producto_ropa(nombre="Chaqueta Invierno", precio=129.50, stock=8, talla="L", color="Negro")
    p5 = tienda.crear_producto_generico(nombre="Tarjeta Regalo 50€", precio=50.0, stock=100)

    print("Inventario inicial:")
    for prod in tienda.listar_productos():
        print(prod)
    print("-" * 60)

    # Simular 3 pedidos de distintos clientes
    # Pedido 1: Ana compra 1 Teléfono X100 y 2 Camisetas
    try:
        pedido1 = tienda.realizar_pedido(usuario_id=c1.id, items={p1.id: 1, p3.id: 2})
        print("Pedido 1 creado:")
        print(pedido1)
    except Exception as e:
        print("Error creando pedido 1:", e)
    print("-" * 60)

    # Pedido 2: Carlos compra 1 Portátil Z5 y 1 Chaqueta
    try:
        pedido2 = tienda.realizar_pedido(usuario_id=c2.id, items={p2.id: 1, p4.id: 1})
        print("Pedido 2 creado:")
        print(pedido2)
    except Exception as e:
        print("Error creando pedido 2:", e)
    print("-" * 60)

    # Pedido 3: María compra 3 Tarjetas Regalo y 1 Camiseta
    try:
        pedido3 = tienda.realizar_pedido(usuario_id=c3.id, items={p5.id: 3, p3.id: 1})
        print("Pedido 3 creado:")
        print(pedido3)
    except Exception as e:
        print("Error creando pedido 3:", e)
    print("-" * 60)

    # Mostrar histórico de pedidos de Ana
    pedidos_ana = tienda.listar_pedidos_por_usuario(c1.id)
    print(f"Histórico de pedidos de {c1.nombre}:")
    for p in pedidos_ana:
        print(p)
    print("-" * 60)

    # Mostrar inventario actualizado
    print("Inventario actualizado:")
    for prod in tienda.listar_productos():
        print(prod)
    print("-" * 60)

if __name__ == "__main__":
    main()
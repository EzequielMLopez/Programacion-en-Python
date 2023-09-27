stock_productos= {"Manzana": 10, "Leche": 5, "Pan": 3, "Factura": 0}
precio_productos= {"Manzana": 3.5, "Leche": 5.5, "Pan": 3.5, "Factura": 2.75}

def pedidos_procesados(pedidos):


    for a in pedidos:
        print(a)


if __name__ == "__main__":
    pedidos=[
        {
            "id": 21,
            "cliente": "Gabriela",
            "productos": {"Manzana": 2}
        },{
            "id": 1,
            "cliente": "Juan",
            "productos": {"Manzanas": 2, "Pan": 4, "Factura": 6}
        }
    ]

    pedidos_procesados(pedidos)
    
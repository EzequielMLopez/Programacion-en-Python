stock_productos= {"Manzana": 10, "Leche": 5, "Pan": 3, "Factura": 0}
precio_productos= {"Manzana": 3.5, "Leche": 5.5, "Pan": 3.5, "Factura": 2.75}

def pedidos_procesados(pedidos):

    for a in pedidos:
        #print(a)
        for value in a.values():
            if type(value) == dict: 
                for key, valor in value.items():
                    print(type(valor))
                    #if valor < stock_productos.get(key):
                    #    print("SIIII")
                    #    stock_productos.update({key: stock_productos.get(key) - valor})
                    #    print(stock_productos)
                    #else:
                    #    print("BASTA")


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
            
    print(type(stock_productos.get("Manzana")))
    pedidos_procesados(pedidos)
    
stock_productos= {"Manzana": 10, "Leche": 5, "Pan": 3, "Factura": 0}
precio_productos= {"Manzana": 3.5, "Leche": 5.5, "Pan": 3.5, "Factura": 2.75}

def procesar_pedidos(pedidos):
    precio_total= 0
    estado= None
    pedidos_procesados= []

    for pedido in pedidos:
        #print(pedido)
        for value in pedido.values():
            if type(value) == dict: 
                #print(value.keys())
                for key, valor in value.items():
                #    print(type(valor))
                #    print(key)
                #    print(stock_productos.get(key))
                    if valor < stock_productos.get(key):
                        #print("SIIII")
                        stock_productos.update({key: stock_productos.get(key) - valor})
                        print(stock_productos)
                        precio_total += precio_productos.get(key)
                        estado= "completo"
                    else:
                        stock_productos.update({key: 0})
                        estado= "incompleto"

        pedidos_procesados.append(pedido.update({"estado": estado}))
    
    
        print(pedidos_procesados)

    return pedidos_procesados

if __name__ == "__main__":
    pedidos=[
        {
            "id": 21,
            "cliente": "Gabriela",
            "productos": {"Manzana": 2}
        },{
            "id": 1,
            "cliente": "Juan",
            "productos": {"Manzana": 2, "Pan": 4, "Factura": 6}
        }
    ]
            
    #print(type(stock_productos.get("Manzana")))
    print(procesar_pedidos(pedidos))
    
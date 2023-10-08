stock_productos= {"Manzana": 10, "Leche": 5, "Pan": 3, "Factura": 0}
precio_productos= {"Manzana": 3.5, "Leche": 5.5, "Pan": 3.5, "Factura": 2.75}

def procesar_pedidos(pedidos):
    pedidos_procesados= []

    for pedido in pedidos:
        precio_total= 0
        estado= None
        for value in pedido.values():
            if type(value) == dict: 
                for key, valor in value.items():
                            if valor < stock_productos.get(key):
                        stock_productos.update({key: stock_productos.get(key) - valor})
                        precio_total += (precio_productos.get(key) * valor)
                        estado= "completo"
                    else:
                        if stock_productos.get(key) > 0:
                            print(precio_total)
                            print(precio_productos.get(key))
                            print(valor)
                            precio_total += (precio_productos.get(key) * valor)
                            #print(valor)
                            #print(precio_total)
                            stock_productos.update({key: 0})
                            estado= "incompleto"
                        

        pedido.update({"estado": estado})
        pedido.update({"precio_total": precio_total})
        pedidos_procesados.append(pedido)
        #pedidos_procesados.append(pedido.update({"estado": estado}))
        #pedidos_procesados.append(pedido.update({"precio_total": precio_total}))
        #print(pedidos_procesados)
        #return pedidos
        #pedidos_procesados.append(pedido.update({"estado": f"{estado}))
    
    print(stock_productos)
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
            "productos": {"Manzana": 2, "Pan": 3, "Factura": 6}
        }
    ]
            
    #print(type(stock_productos.get("Manzana")))
    print(procesar_pedidos(pedidos))
    
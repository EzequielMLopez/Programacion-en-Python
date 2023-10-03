def min_to_may(palabra):
    nueva_palabra= ""
    
    for letra in palabra:
        if letra in "abcdefghijklmnopqrstuvwxyz":
            nueva_palabra+= letra.upper()
        else:
            nueva_palabra+= letra
            continue
    
    return nueva_palabra


palabrita= "Estocolmo es lo mEJor"
print(min_to_may(palabrita))
print("Cambio de prueba")

def cifrado_cesar():
    
    lista_abecedario="abcdefghijklmnopqrstuvwxyz"
    contador = 0

    condicion = True
    while condicion:

        palabra= input("ingrese tu mensaje que empiece con c...: ")
        primer_caracter = ord(palabra[0]) - ord("c")
        decodificado = ""
        contador = 0
        for c in palabra[1:]:
            if c in lista_abecedario:
                decodificado += lista_abecedario[(lista_abecedario.index(c) + primer_caracter) % 26]
                if c == "g":
                    contador += 1
            else:
                decodificado += c
        if palabra =="end":
            condicion = False
        else:
            print(decodificado)
            print(f"La letra g aparece {contador} veces en el mensaje.")


    

cifrado_cesar()
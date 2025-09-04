listaNombres=["Ernesto", "Alan", "Angel", "Pedro", "Manuel", "Santiago", "Alexis", "Alesio", None, ""]
filtroDePalabras=list(filter(lambda palabra: palabra !=None and palabra!="" and palabra[0].upper()=="A", listaNombres))
print(filtroDePalabras)


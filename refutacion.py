
base_conocimiento_LogicaPrimerOrden = []
base_conocimiento_FormaNormalCopnjuntiva = []

# Poner la base de conocimiento en forma normal conjuntiva
# Programar reglas :) 
def convertir_sentencia_FNC(sentencia : str):
    sentencia_temp = sentencia
    # Regla 1
    if "<=>" in sentencia_temp: 
        temp = sentencia_temp.split("<=>")
        sentencia_temp = temp[0] + "=>" + temp[1] + "∧" + temp[1] + "=>" + temp[0]
    # Eoi 

    # Regla 2 
    if "=>" in sentencia_temp:
        temp = ""
        union = ""
        result = [] # s1 (union) s2
        if "∧" in sentencia_temp: 
            temp = sentencia_temp.split("∧")
            union = "∧" 
        if "v" in sentencia_temp: 
            temp = sentencia_temp.split("v")
            union = "v" 
        if union == "": 
            temp = [sentencia_temp]
    
        for sentence in temp: 
            s = sentence.split("=>") 
            result.append("¬" + s[0] + "v" + s[1])

        if union == "": 
            sentencia_temp = result[0]
        else: 
            sentencia_temp = union.join(result)
    # Eoi

    return sentencia_temp

print(convertir_sentencia_FNC("Pompeyano(x) <=> Romano(x)"))
print(convertir_sentencia_FNC("a => b"))
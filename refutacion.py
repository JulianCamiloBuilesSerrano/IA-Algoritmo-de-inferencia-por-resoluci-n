import re
bc_LogicaPrimerOrden = []
bc_FormaNormalConjuntiva = []

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
            temp = sentencia_temp.split("V")
            union = "V" 
        if union == "": 
            temp = [sentencia_temp]
    
        for sentence in temp: 
            s = sentence.split("=>") 
            result.append("¬" + s[0] + "V" + s[1])

        if union == "": 
            sentencia_temp = result[0]
        else: 
            sentencia_temp = union.join(result)
    # Eoi
    # Regla 3
    pattern = r"¬\(¬(.[^\(\)]*\(?[a-zA-Z]*\)?)\)" # ¬(¬𝝰)
    regex_match = re.search(pattern, sentencia_temp)
    if regex_match != None:
        sentencia_temp = regex_match.group(1)
    # Eoi
    pattern = r"¬\((.*)∧(.*)\)" # ¬(𝝰∧𝝱)
    regex_match = re.search(pattern, sentencia_temp)
    if regex_match != None: 
        sentencia_temp = "¬" + regex_match.group(1) + "v" + "¬" + regex_match.group(2)
    # Eoi
    pattern = r"¬\((.*)v(.*)\)" # ¬(𝝰∨𝝱)
    regex_match = re.search(pattern, sentencia_temp)
    if regex_match != None: 
        sentencia_temp = "¬" + regex_match.group(1) + "∧" + "¬" + regex_match.group(2)
    # Eoi
    pattern = r"¬∀x ?(.*\((.*)\))" # ¬∀x P(x)
    regex_match = re.search(pattern, sentencia_temp)
    if regex_match != None: 
        sentencia_temp = "∃" + regex_match.group(2) + "¬" + regex_match.group(1)
    # Eoi
    pattern = r"¬∃x ?(.*\((.*)\))" # ¬∃x P(x)
    regex_match = re.search(pattern, sentencia_temp)
    if regex_match != None: 
        sentencia_temp = "∀" + regex_match.group(2) + "¬" + regex_match.group(1)
    # Eoi
    # Regla 4 
    pattern = r"∀(\w*) ?\w*\((\w*)\) ? ∨ ?∀(\w*) ?\w*\((\w*)\)" # ∀x P(x) ∨ ∀x Q(x)
    regex_match = re.search(pattern, sentencia_temp)
    if regex_match != None: 
        
        if regex_match.group(1) == regex_match.group(2) and regex_match.group(2) == regex_match.group(3) and regex_match.group(3) == regex_match.group(4):
            s_t = sentencia_temp.split("∨")
            sentencia_ = re.sub(regex_match.group(1), "y", s_t[1])
            sentencia_temp = s_t[0] + "∨" + sentencia_
        # Eoi
    # Eoi

    # Regla 5 
    pattern = r"∀[a-z]|∃[a-z]"
    regex_findall = re.findall(pattern, sentencia_temp)
    if len(regex_findall) > 1: 
        
        sentence_splitted = re.split(pattern, sentencia_temp)
        sentencia_temp = "".join(regex_findall) + "".join(sentence_splitted)

    #Regla 6
    if "∃" in sentencia_temp:
        
        letras = []
        sentencia_eliminda= []
        temp =[]
        for i in range(len(sentencia_temp)):
            if sentencia_temp[i] == "∃":
                letras.append(sentencia_temp[i+1])
            elif sentencia_temp[i -1] != "∃":
                sentencia_eliminda.append(sentencia_temp[i])
        for i in range(len(letras)):
            var = "s"+str(i)
            for j in range(len(sentencia_eliminda)):
                if sentencia_eliminda[j] == letras[i]:
                    sentencia_temp = "".join(sentencia_eliminda[:j]) + var + "".join(sentencia_eliminda[j+1:])
                    sentencia_eliminda = list(sentencia_temp)
    #Regla 7
    if "∀" in sentencia_temp:
        letras = []
        sentencia_eliminda= []
        
        for i in range(len(sentencia_temp)):
            if sentencia_temp[i] == "∀":
                pass
            elif sentencia_temp[i -1] != "∀":
                sentencia_eliminda.append(sentencia_temp[i])
        sentencia_temp = "".join(sentencia_eliminda)
        print(sentencia_temp)
    #regla 8
    patron  = r"\((.*)∧(.*)\)V(.*)"
    match = re.search(patron, sentencia_temp)
    if match != None:
        
        sentencia_temp = "(" + match.group(1) + "V" + match.group(3) +")∧("+match.group(2) + "V" +match.group(3) + ")"
        
    #regla 9
    if "∧" in sentencia_temp:
        x = sentencia_temp.split("∧")
        temp = []
        for i in x:
            print(i[1:-1])
            temp.append( i[1:-1])
        
        return temp

        
    return sentencia_temp

def negar(c1):
    if c1[0] == "¬":
        return c1[1:]
    else:
        return "¬" + c1

def comparacionClausulas(cla1,cla2):
    #print(cla1,"--",cla2)
    c1 = cla1.split("V")
    c2 = cla2.split("V")
    copia1 = c1.copy()
    copia2 = c2.copy()
    entra = False
    for j in c1:
        indice = j.index("(")
        subcadena = j[0:indice]
        for k in c2:
            indice2 = k.index("(")
            subcadena2 = k[0:indice2]
            if subcadena == negar(subcadena2):
                copia1.remove(j)
                copia2.remove(k)
                entra = True
            #end if
        #end for
    #end for
    clausula = copia1+copia2
    return ["V".join(clausula),entra]


def inferencia(pregunta):
    clausula1 = negar(pregunta)
    clausula2 = ""
    copiaBc= bc_FormaNormalConjuntiva.copy()
    aux= 0
    verdad =False
    while len(copiaBc) != 0 and aux != len(copiaBc) :
        for i in range(len(bc_FormaNormalConjuntiva)):
            clausula2 = bc_FormaNormalConjuntiva[i]
            nueva,estado = comparacionClausulas(clausula1,clausula2)
            if estado == True:
                #print( clausula1,"---",clausula2)
                clausula1 = nueva
                copiaBc.remove(clausula2)
            if clausula1 == "":
                verdad = True
                break
    print(verdad)


#print(convertir_sentencia_FNC("¬(gits(c))"))
# print(convertir_sentencia_FNC("a => b"))
# print(convertir_sentencia_FNC("∃y∃x∃zP(y)C(x)Q(z)"))
print(convertir_sentencia_FNC("∀x Romano(x) => Leal(x, Cesar)V Odia(x, Cesar)"))

def agregarPrimerOrden():
    p = str(input("ingrese la frase en primer orden"))
    r = convertir_sentencia_FNC("Hombre(Marco)")
    bc_LogicaPrimerOrden = bc_LogicaPrimerOrden + r
    r = convertir_sentencia_FNC("Pompeyano(Marco)")
    bc_LogicaPrimerOrden = bc_LogicaPrimerOrden + r
    r = convertir_sentencia_FNC("∀x Pompeyano(x)=>Romano(x)")
    bc_LogicaPrimerOrden = bc_LogicaPrimerOrden + r
    r = convertir_sentencia_FNC("Gobernante(Cesar)")
    bc_LogicaPrimerOrden = bc_LogicaPrimerOrden + r

    
    
# bc_FormaNormalConjuntiva.append("Hombre(Marco)")
# bc_FormaNormalConjuntiva.append("Pompeyano(Marco)")
# bc_FormaNormalConjuntiva.append("¬Pompeyano(x3)VRomano(x3)")
# bc_FormaNormalConjuntiva.append("Gobernante(Cesar)")
# bc_FormaNormalConjuntiva.append("¬Romano(x5)VLeal(x5,Cesar)VOdia(x5,Cesar)")
# bc_FormaNormalConjuntiva.append("¬Hombre(x7)V¬Gobernante(y7)V¬IntentaAsesinar(x7,y7)V¬Leal(x7,y7)")
# bc_FormaNormalConjuntiva.append("IntentaAsesinar(Marco,Cesar)")
# inferencia("Odia(Marco,Cesar)")



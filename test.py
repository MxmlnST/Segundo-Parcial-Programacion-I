def simplificar_fraccion(num1:int,num2:int):
    factores_num1 = []
    factores_num2 = []
    mcd = []
    fraccion = [0,0]
    for i in range(num1):
        i += 1
        if num1 % i == 0:
            factores_num1.append(i)
    for i in range(num2):
        i += 1
        if num2 % i == 0:
            factores_num2.append(i)
    for e in factores_num1:
        if e in factores_num2:
            mcd.append(e)
    fraccion[0] = int(num1 / max(mcd))
    fraccion[1] = int(num2 / max(mcd))
    return fraccion

def simplificar_fraccion2(numerador:int,denominador:int)->list:
    "Simplifica una fracción. Retorna una lista con el numerador(lista[0]) y el denominador(lista[1]) reducidos"
    factores_num1 = list(filter(lambda num: numerador % (num) == 0, range(1,numerador+1)))
    factores_num2 = list(filter(lambda num: denominador % (num) == 0, range(1,denominador+1)))
    mcd = max((filter(lambda num: num in factores_num2,factores_num1)))
    fraccion = [int(numerador/mcd),int(denominador/mcd)]
    return fraccion



def simplificar_fraccion3(numerador:int,denominador:int)->list:
    """Simplifica una fracción. Retorna una lista con el numerador(lista[0]) y el
    denominador(lista[1]) reducidos"""
    factores = lambda posicion:filter(lambda num: posicion % (num) == 0, range(1,posicion+1))
    mcd = max(filter(lambda num: num in factores(denominador),factores(numerador)))
    return int(numerador/mcd),int(denominador/mcd)

# print(simplificar_fraccion(244,36))
# print(simplificar_fraccion2(244,36))
# print(simplificar_fraccion3(244,36))


i = 5
while i > 1:
    print("entre")
    if i == True:
        print("por break")
        break
    else:
        i -= 1
else:
    print("else")


lista = [1,1,2,2,3,3,4,4,5,5,6,6,7,7]

"""  SS
   XX  XXXXXXXXXXXXXXXXXX
   XX D                AX
   XXD                A X
   XXXXXXXXXXXXXXXXXXX  X
   XXA                I X
   XX A                IX
   XX  XXXXXXXXXXXXXXXXXX
   XX D               AXX
   XXD               A XX
   XXXXXXXXXXXXXXXXXX  XX
   XXA            IXX  XX
   XX A          I XX  XX
   XX  XXXXXXXXXX  XX  XX
   XX  XXXXXXXXXX U  I XX
   XX  XXXXXXXXXXU    IXX
   XX  XXXXXXXXXXXXXXXXXX
   XX  XXXXXXXXXXXXXXXXXX
   XX  XXXXXD            F
   XX  XXXXX D           F
   XX D     U XXXXXXXXXXX
   XXD       UXXXXXXXXXXX
   XXXXXXXXXXXXXXXXXXXXXX

"""

dic = [{"a":1},{"b":2},{"c":3}]

for i in range(len(dic)):
    print(list(dic[i].keys()))
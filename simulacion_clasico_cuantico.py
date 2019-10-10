import calculadora.cnyt_Calculadora as cal
##Programa simulación de lo clásico a lo cuántico

################# MULTIPLE RENDIJA CLASICO ######################
def transpuestaM(matrizA):
    matrizR=[]
    for i in range(len(matrizA[0])):
        matrizR.append([])
        for j in range(len(matrizA)):
            matrizR[i].append((0,0))
    for i in range(len(matrizA[0])):
        for j in range(len(matrizA)):
            matrizR[i][j]=matrizA[j][i]
    return matrizR

def mainClasic(matriz,estInicial):
    matrizR=multMClasic(matriz,matriz)
    return matrizR,multMClasic(matrizR,transpuestaM([estInicial]))
    
def multMClasic(matrizA,matrizB):
    matrizR=[]
    for i in range(len(matrizA)):
        matrizR.append([])
        for j in range(len(matrizB[0])):
            matrizR[i].append(0)
    for i in range(len(matrizA)):
        for j in range(len(matrizB[0])):
            valor=(0,1)
            for k in range(len(matrizB)):
                valor=sumClasic(multClasic(matrizA[i][k],matrizB[k][j]),valor)
            matrizR[i][j]=valor
    return matrizR

def sumClasic(frac1,frac2):
    rta=(0,0)
    if (frac1[1]==frac2[1]): rta=(frac1[0]+frac2[0],frac1[1])
    else: rta=(frac1[0]*frac2[1]+frac2[0]*frac1[1],frac1[1]*frac2[1])
    return rta

def multClasic(frac1,frac2):
    rta=(0,0)
    if (frac1[0]==0 or frac2[0]==0): rta=(0,1)
    else: rta=(frac1[0]*frac2[0],frac1[1]*frac2[1])
    return rta
##############  CANICAS  ################
def MainCanicas(estInicial,matriz,numClicks):
    matriz=clicks(matriz,numClicks)
    estFinal=multiplicacionMatrizB(matriz,transpuestaM([estInicial]))
    return estFinal

def clicks(matriz,numClicks):
    for i in range(0,numClicks):
        matriz=multiplicacionMatrizB(matriz,matriz)
    return matriz

def multiplicacionMatrizB(matrizA,matrizB):
    matrizR=[]
    for i in range(len(matrizA)):
        matrizR.append([])
        for j in range(len(matrizB[0])):
            matrizR[i].append(0)
            
    for i in range(len(matrizA)):
        for j in range(len(matrizB[0])):
            resultado=0
            for k in range(len(matrizB)):
                resultado+=matrizA[i][k]*matrizB[k][j]
            matrizR[i][j]=resultado
    return matrizR

###################  MULTIPLE RENDIJA  #########################
def mainCuantico(matriz,vector):
    return (multMCuantica(matriz,matriz)[vector])

def multMCuantica(matrizA,matrizB):
    matrizR=[]
    for i in range(len(matrizA)):
        matrizR.append([])
        for j in range(len(matrizB[0])):
            matrizR[i].append(0)
    for i in range(len(matrizA)):
        for j in range(len(matrizB[0])):
            valor=((0,0),1)
            for k in range(len(matrizB)):
                valor=sumCuantica(multCuantica(matrizA[i][k],matrizB[k][j]),valor)
            matrizR[i][j]=valor
    return matrizR

def multCuantica(comp1,comp2):
    return (cal.multiplicacionC(comp1[0],comp2[0]),comp1[1]*comp2[1])

def sumCuantica(comp1,comp2):
    return (cal.sumaC(comp1[0],comp2[0]),comp1[1]+comp2[1])
    
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

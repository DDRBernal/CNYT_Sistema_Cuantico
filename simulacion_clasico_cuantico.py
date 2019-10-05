##Programa simulación de lo clásico a lo cuántico

def simulacionMain(estInicial,matriz,numClicks):
    matriz=clicks(matriz,numClicks)
    estFinal=multiplicacionMatrizB(matriz,[estInicial])
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


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

print(simulacionMain([1,2],[[1,1],[1,3]],5))

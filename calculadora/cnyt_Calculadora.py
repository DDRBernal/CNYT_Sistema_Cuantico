from sys import stdin
import math
from math import atan

def restaC(tuplaA,tuplaB):
    if (type(tuplaA)==int or type(tuplaA)==float):num=tuplaA;tuplaA=(num,0)
    if (type(tuplaB)==int or type(tuplaB)==float):num=tuplaB;tuplaB=(num,0)    
    tuplaFinal=(tuplaA[0]-tuplaB[0],tuplaA[1]-tuplaB[1])
    return(tuplaFinal)
    
def sumaC(tuplaA,tuplaB):
    if (type(tuplaA)==int or type(tuplaA)==float):num=tuplaA;tuplaA=(num,0)
    if (type(tuplaB)==int or type(tuplaB)==float):num=tuplaB;tuplaB=(num,0)
    tuplaFinal=(tuplaA[0]+tuplaB[0],tuplaA[1]+tuplaB[1])
    return(tuplaFinal)

def multiplicacionC(tuplaA,tuplaB):
    if (type(tuplaA)!=tuple):num=tuplaA;tuplaA=(num,0)
    if (type(tuplaB)!=tuple):num=tuplaB;tuplaB=(num,0)
    tuplaFinal1=((tuplaA[0]*tuplaB[0]),-(tuplaA[1]*tuplaB[1]))
    tuplaFinal2=(tuplaA[0]*tuplaB[1]),(tuplaA[1]*tuplaB[0])
    return (tuplaFinal1[0]+tuplaFinal1[1],tuplaFinal2[0]+tuplaFinal2[1])

def divisionC(tuplaA,tuplaB):
    if (type(tuplaA)==int or type(tuplaA)==float):num=tuplaA;tuplaA=(num,0)
    if (type(tuplaB)==int or type(tuplaB)==float):num=tuplaB;tuplaB=(num,0)    
    valor1=(tuplaA[0]*tuplaB[0]) ##sin i
    valor2=((tuplaA[0]*-tuplaB[1])+(tuplaA[1]*tuplaB[0])) ## con i
    valor22=(tuplaA[1]*tuplaB[1]) ## con i**2
    tuplaF=(valor1,valor2,valor22)
    ##denomidador
    valor3=tuplaB[0]**2 ## sin i
    valor4=(tuplaB[1]**2) ##con i
    tuplaFinal=((tuplaF[0]+tuplaF[2])/(valor3+valor4),tuplaF[1]/(valor3+valor4))
    return(tuplaFinal)

def moduloC(tuplaA):
    if (type(tuplaA)==int or type(tuplaA)==float):num=tuplaA;tuplaA=(num,0)    
    tuplaFinal=((tuplaA[0]**2)+(tuplaA[1]**2))**0.5
    return tuplaFinal

def conjugadoC(tuplaA):
    if (type(tuplaA)==int or type(tuplaA)==float):num=tuplaA;tuplaA=(num,0)    
    tuplaFinal=(tuplaA[0],-tuplaA[1])
    return(tuplaFinal)

def polarC(tuplaA):
    if (type(tuplaA)==int or type(tuplaA)==float):num=tuplaA;tuplaA=(num,0)    
    tupla1=((tuplaA[0]**2)+(tuplaA[1]**2))**0.5
    tuplaFinal=(tupla1,atan(tuplaA[1]/tuplaA[0]))
    return(tuplaFinal)

def cartesianoC(tuplaA):
    if (type(tuplaA)==int or type(tuplaA)==float):num=tuplaA;tuplaA=(num,0)    
    tuplaFinal=(tuplaA[0]*math.cos(tuplaA[1]),tuplaA[0]*math.sin(tuplaA[1]))
    return(tuplaFinal)

def faseC(tuplaA):
    if (type(tuplaA)==int or type(tuplaA)==float):num=tuplaA;tuplaA=(num,0)    
    tuplaFinal=(math.atan(tuplaA[1]/tuplaA[0]))
    return(tuplaFinal)

#---------------------------------- calculadora matriz ----------------------------------------#


def multiplicacionEV(vector,c):
    for i in range(len(vector)):
        vector[i]= c*vector[i]
    return vector

def sumaV(vectorA,vectorB):
    if (len(vectorA)==len(vectorB)):
        vectorR=[]
        for i in range(len(vectorA)):
            vectorR.append(sumaC(vectorA[0],vectorB[0]))
        return vectorR
    else:
        print("Los tamaños de los vectores deben ser iguales")

def inversaV(vector):
    for i in range(len(vector)):
        vector[i]=vector[i]*-1
    return vector

def sumaM(matrizA,matrizB):
    matrizR=[]
    if ((len(matrizA)==len(matrizB)) and (len(matrizA[0])==len(matrizB[0]))):            
        for q in range(len(matrizA)):
            matrizR.append([])
            for k in range(len(matrizA[0])):matrizR[q].append(0)
        for i in range(0,len(matrizA)):
            for j in range(len(matrizA[0])):matrizR[i][j]=sumaC(matrizA[i][j],matrizB[i][j])    
        return matrizR
    else:
        print("Los tamaños de las matrices deben ser iguales")

def restaM(matrizA,matrizB):
    matrizR=[]
    if ((len(matrizA)==len(matrizB)) and (len(matrizA[0])==len(matrizB[0]))):
        for q in range(len(matrizA)):
            matrizR.append([])
            for k in range(len(matrizA[0])):matrizR[q].append(0)
        for i in range(0,len(matrizA)):
            for j in range(len(matrizA[0])):matrizR[i][j]=restaC(matrizA[i][j],matrizB[i][j])
        return matrizR
    else:
        print("Los tamaños de las matrices deben ser iguales")

def multiplicacionM(matrizA,matrizB):
    if (len(matrizB)==1 and (len(matrizB[0])==len(matrizA[0]))):
        return multiplicacionMV(matrizA,matrizB[0])
    matrizR=[]
    posA=0
    posB=0
    if (len(matrizA[0])==len(matrizB)):
        for algo in range(len(matrizA)):
            matrizR.append([i for i in range(len(matrizB[0]))])
        while (posA<len(matrizA)):
            for i in range(0,len(matrizA)):
                suma=0
                for j in range(len(matrizB)):
                    suma=sumaC(suma,multiplicacionC(matrizA[posA][j],matrizB[j][posB]))
                matrizR[posA][posB]=suma
                suma=0
                posB+=1
            posA+=1
            posB=0
    if (matrizR==[]):print("El numero de columnas de A debe ser igual al numero de filas de B")
    return matrizR

def multiplicacionMV(matriz,vector):
    if (len(matriz)==len(vector)):
        matrizR=[]
        for i in range(0,len(matriz)):
            suma=0
            for j in range(0,len(matriz[i])):
                suma= sumaC(suma,multiplicacionC(matriz[i][j],vector[j]))
            matrizR.append(suma)
            suma=0
        return matrizR
    else:
        print("El tamaño de el vector debe ser igual al numero de filas de la matriz")

def inversaM(matriz):
    matrizR=[]
    for i in range(0,len(matriz)):
        matrizR.append([int(i) for i in range(0,len(matriz[0]))]);
        for j in range(0,len(matriz[0])):
            matrizR[i][j]=matriz[i][j]*-1
    return matrizR

def multiplicacionME(matriz,c):
    matrizR=[]
    for i in range(0,len(matriz)):
        matrizR.append([int(i) for i in range(0,len(matriz[0]))]);
        for j in range(0,len(matriz[0])):
            matrizR[i][j]= c*matriz[i][j]
    return matrizR

def transpuestaM(matriz):
    matrizR=[]
    posi=0
    for i in range(0,len(matriz[0])):
            matrizR.append([])
            for j in range(0,len(matriz)):
                matrizR[i].append(matriz[j][posi])
            posi+=1
    return matrizR
    
def conjugadaM(matriz):
    matrizR=[]
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[i])):
            tup=matriz[i][j]
            if (type(tup)!=int):matriz[i][j]=(matriz[i][j][0]*-1,matriz[i][j][1]*-1)
    return matriz

def adjuntaM(matriz):
    return conjugadaM(transpuestaM(matriz))
                
def distanciaM(matrizA,matrizB):
    return normaM(sumaM(matrizA,inversaM(matrizB)))
    
def normaM(matriz):
    suma=0
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[0])):
            if (type(matriz[i][j])!=int):
                tupla = matriz[i][j]
                tupla2 = (matriz[i][j][0],-matriz[i][j][1])
                tuplaF = (multiplicacionC(tupla,tupla2))
                suma+= (tuplaF[0]**1)
            else:
                suma+= (matriz[i][j]**2)
    return (suma**0.5)


def checkHermitian(matriz):
    matrizR=transpuestaM(conjugadaM(matriz))
    return(conjugadaM(matriz)==matrizR)

def checkUnitaria(matriz):
    #selfcheckUnitaria([[(0,0),(0,1)],[(0,-1),(0,0)]])
    matrizB=conjugadaM(transpuestaM(matriz))
    if ((len(matriz)==len(matriz[0]))):
        return esUnitaria(multiplicacionM(matriz,matrizB))
    
def esUnitaria(matriz):
    rta=True
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if (type(matriz[i][j])==int): matriz[i][j]=(matriz[i][j],0)
            if (i==j):
                if (matriz[i][j]!=(1,0)):rta=False
            else:
                if (matriz[i][j]!=(0,0)):rta=False
    return rta

        
def productoTensor(matrizA,matrizB):
    matrizR=[]
    for k in range(len(matrizA)*len(matrizB)):
        matrizR.append([]);
        for u in range(len(matrizA)*len(matrizB)):matrizR[k].append(-9999)
    for i in range(len(matrizR)):
        for j in range(len(matrizR[i])):
            matrizR[i][j]=multiplicacionC(matrizA[i//len(matrizB)][j//len(matrizA)],matrizB[i%len(matrizB)][j%len(matrizA)])
    return matrizR

    
def accionM(matriz,vector):
    print("Ingrese una operacion")
    print('');print ('////// suma //////');print ('////// resta //////')
    print ('////// multiplicacion //////')
    print ('////// division //////');print()
    a=input()
    a=a.lower().strip()
    print(a)
    if (a=='*'): return multiplicacionMV(matriz,vector)
    

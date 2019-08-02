#!/usr/bin/python3

import numpy as np
import cv2

def LerImagem(caminhoImagem):
    img = cv2.imread(caminhoImagem, cv2.IMREAD_ANYCOLOR)
    return img;

def MostrasImagem(imagem, tituloJanela):
    cv2.imshow(tituloJanela, imagem);
    cv2.waitKey(0);
    cv2.destroyAllWindows();

def CriaMatriz(linha, coluna):
    matriz = []
    for i in range(linha):
        linha = []
        for j in range(coluna):
            linha.append(0)
        matriz.append(linha)
    return matriz

def NumeroDeLinhas(img):
    return img.shape[0]

def NumeroDeColunas(img):
    return img.shape[1]

def ValorDoByte(imagem, linha, coluna, cor):
    if(linha < 0 or linha > (NumeroDeLinhas(imagem) - 1)):
        print("Linha Invalida : Out of Range")
        exit(0)
    elif(coluna < 0 or coluna > (NumeroDeColunas(imagem) - 1)):
        print("Coluna Invalida : Out of Range")
        exit(0)
    elif(cor != "blue" and cor != "red" and cor != "green"):
        print("Cor Invalida")
        exit(0)
    elif(cor == "blue"):
        return imagem[linha, coluna, 0]
    elif(cor == "green"):
        return imagem[linha, coluna, 1]
    elif(cor == "red"):
        return imagem[linha, coluna, 2]

def MudarValorByte(imagem, linha, coluna, cor, novoValor):
    if(novoValor > 255 or novoValor < 0):
        print("Valor não está entre 0 e 255 : Out of Range")
        exit(0)
    elif(linha < 0 or linha > (NumeroDeLinhas(imagem) - 1)):
        print("Linha Invalida : Out of Range")
        exit(0)
    elif(coluna < 0 or coluna > (NumeroDeColunas(imagem) - 1)):
        print("Coluna Invalida : Out of Range")
        exit(0)
    elif(cor != "blue" and cor != "red" and cor != "green"):
        print("Cor Invalida")
        exit(0)
    elif(cor == "blue"):
        imagem.itemset((linha, coluna, 0), novoValor)
    elif(cor == "red"):
        imagem.itemset((linha, coluna, 2), novoValor)
    elif(cor == "green"):
        imagem.itemset((linha, coluna, 1), novoValor)

def Luiz():
    return 0

def Thiago():
    return 0

def Thales():
    return 0

def Pepe():
    return 0

def Jonas():
    return 0



def main():
    #Lendo Imagem e obtendo a Matriz
    img = LerImagem("aguia.jpg");
    
    #Acessando o pixel da linha e coluna (0,0)
    print(img[0, 0])
    
    #Acessando o primeiro Byte(Cor Azul) da linha e coluna (0, 0)
    #O opencv representa na seguinte Ordem : BGR e não RGB
    print(img[0, 0, 0])
    #Ou se preferir
    print(ValorDoByte(img, 0, 0, "blue"))
    
    #Obtendo o Numero de linhas da imagem
    print(NumeroDeLinhas(img))

    #Obtendo o Numero de colunas da imagem
    print(NumeroDeColunas(img))

    #Modificando o valor de um Byte
    #Modificando a Cor Azul da linha e coluna (0, 0)
    #MudarValorByte(imagem, linha, coluna, cor, novoValor)
    MudarValorByte(img, 0, 0, "blue", 124)
    print(img[0, 0, 0])
    
    #Mostrando Imagem
    #Apertar 0 para fechar a imagem
    #def MostrasImagem(imagem, tituloJanela):
    MostrasImagem(img, "Imagem");

    #Criando uma Matriz
    #CriaMatriz(linha, coluna):
    print(CriaMatriz(3, 3))


    #Links úteis
    #https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_image_display/py_image_display.html
    #http://www.joaomatosf.com/blog/index080c.html?option=com_content&view=article&id=63&catid=36&Itemid=54
    #https://www.youtube.com/playlist?list=PLh6SAYydrIpctChfPFBlopqw-TGjwWf_8

    # Chamar Sua Função Abaixo
    Luiz()
    
    return 0

if __name__ == "__main__":
    main()
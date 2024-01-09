#!/usr/bin/env python3

import cv2
import numpy as np


def calibra_camera():
    print("A calibrar a câmera")


def obtem_sopa():
    #Inicializa a variável de retorno
    sopa = [];
    print("A obter a sopa")


    return sopa;


def inicializa_dicionário(palavras):
    #Inicializa variável de retorno
    palavras_dict = {};
    
    #Para cada palavra guardamos o seu comprimento e um dicionário com a correspondência
     #Entre as letras das quais estamos à procura e em qual posição do tabuleiro e da palavra estão
    for palavra in palavras:
        pal_size = len(palavra);
        dict_letras = {};
        dict_letras[palavra[0]] = [(None,0)];
        dict_letras[palavra[-1]] = [(None,pal_size-1];
        palavras_dict[palavra] = (pal_size, dict_letras);

    return palavras_dict;


def atualiza_palavras(palavras_dict, letra, pos_letra):
    

    #Para cada palavra do dicionario
     #Vemos se a letra existe no dicionario da palavra
      #Se sim, vemos qual a direcao da anterior para esta
       #Apos isso, adicionamos a procura da proxima letra na posicao que queremos 
       #Depois disso limpamos para as outras letras nesta posicao
        

def resolve_sopa(sopa, lista_palavras):
    #Inicializa variável de retorno
    palavras_pos = [];

    #Inicilizar já as variáveis que serão constantes
    cols = len(sopas);
    linhas = len(sopas[0]);

    #Inicializar variáveis que serão usadas
     #Adicionamos ao dicionário as palavras
    palavras_dict = inicializa_dicionário(lista_palavras)

    

    #Loop para passarmos por todas as letras
    for x in range(cols):
        for y in range(linhas):
            print("ola")
            letra = sopa[x][y];
            atualiza_palavras(palavras_dict, letra, (x,y));

            #Verifica se a letra adiciona progresso 
            #Caso sim, marca a proxima letra como passada
            #Caso não, elimina o progresso daquela letra naquele sentido


    


    return palavras;


def testar_funcs():
    palavras = ["ola", "eu", "sou", "o", "bruno"]
    dict_palavras = inicializa_dicionário(palavras)
    print(dict_palavras)

def main():
    print("This is the project")
    testar_funcs()
    #Carregar os parâmetros da câmara ou obter uns novos
    #Obter as imagens
    #Obter a sopa
    #Resolver a sopa
    #Dar print das posições
    #Eventualmente colocar em live o vídeo


if __name__ == "__main__":
    main()

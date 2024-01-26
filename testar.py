#!/usr/bin/env python3

import cv2
from pprint import pprint
import numpy as np


sopa = [["A","A","C","N","T","Y","F","R","I","D","A","Y","Y","Y"],
        ["A","A","N","M","T","A","A","U","D","O","R","E","R","T"],
        ["U","E","B","U","O","M","R","E","C","A","Y","Y","A","U"],
        ["K","E","S","T","S","U","G","U","A","U","Y","U","U","E"],
        ["Y","R","E","U","L","I","R","P","A","E","E","S","N","S"],
        ["W","A","M","A","O","Y","S","H","T","N","O","M","A","D"],
        ["Y","E","W","O","F","C","Y","D","Y","E","F","R","J","A"],
        ["N","A","D","E","N","A","Y","M","A","R","E","E","U","Y"],
        ["A","A","D","N","E","D","E","R","D","E","B","B","L","W"],
        ["B","N","H","S","E","K","A","O","N","B","R","M","C","I"],
        ["E","D","C","A","R","S","R","Y","U","O","U","E","Y","N"],
        ["E","N","R","S","U","U","D","U","S","T","A","C","R","T"],
        ["Y","A","A","T","Y","E","H","A","S","C","R","E","O","E"],
        ["D","U","M","C","R","H","B","T","Y","O","Y","D","N","R"]
       ];

palavras = ["WEDNESDAY","DAYS","MONDAY","JANUARY","AUGUST","WINTER","AUTUMN","THURSDAY",
            "MARCH","OCTOBER","MAY","APRIL","FRIDAY","TUESDAY","SUNDAY","MONTHS","YEAR",
            "FEBRUARY","DECEMBER","WEEK", "AMANDA"];

palavras_acabadas = []

def inicializa_dicionário(palavras):
    palavras_dict = {};
    for palavra in palavras:
        pal_size = len(palavra);
        dict_letras = {};
        palavras_dict[palavra] = (dict_letras);
    return palavras_dict;

def adiciona_pedidas(letras_dict, palavra, pos_sopa, direcao, sentido, pos_letra):
    #Letras_dict -> dicionario com as posicoes e as letras pedidas para cada posicao
    #Palavra -> palavra que queremos    #Pos sopa -> posicao da sopa onde estamos
    #Direcao -> direcao da palavra      #Sentido -> sentido da palavra
    #Pos letra -> posicao da letra na palavra
    lim = 14;
    proxima_sopa_pos = (pos_sopa[0]+direcao[0], pos_sopa[1]+direcao[1]);
    proxima_letra_pos = pos_letra + sentido;

    if (not -len(palavra) <= proxima_letra_pos < len(palavra)):
        global palavras_acabadas
        print("A PALAVRA: ", palavra, " ACABOU AQUI: ", pos_sopa)
        inicial = (pos_sopa[0]-(len(palavra)-1)*direcao[0], pos_sopa[1]-(len(palavra)-1)*direcao[1])
        palavras_acabadas = palavras_acabadas + [(palavra,inicial, pos_sopa)]
        return
    if (not 0 <= proxima_sopa_pos[0] < lim) or (not 0 <= proxima_sopa_pos[1] < lim):
        return;

    letras_dict[proxima_sopa_pos] = letras_dict.get(proxima_sopa_pos, [])+ [(palavra[proxima_letra_pos], direcao, sentido, proxima_letra_pos)]

def atualiza_palavras(palavras_dict, letra, pos_letra):
    #Para cada palavra
    for (palavra, letras_pedidas) in palavras_dict.items():
        #print("LETRAS PEDIDAS:", letras_pedidas)

        #Vou buscar a lista de palavras que passariam naquela posição
        letras_para_pos = letras_pedidas.get(pos_letra);

        #Caso existam
        if letras_para_pos is not None:
            letras_para_pos = letras_pedidas.pop(pos_letra) 
            #Para cada tuplo de letra que eu quereria para essa posição
            for letra_para_pos in letras_para_pos:
                #Obtenho a informação da letra
                 #Letra; Direcao -> (X,Y), diz qual será a próxima posição; 
                 #Sentido -> Diz se estamos a ir de trás para a frente ou normal; Autal -> Posição da letra que pedimos atual
                (letra_pedida, direcao, sentido, atual_letra_pos) = letra_para_pos 
                if letra_pedida == letra: #No caso de a letra na posição ser a que queríamos

                    adiciona_pedidas(letras_pedidas, palavra, pos_letra, direcao, sentido, atual_letra_pos)
                    #print("A letra dá jeito")
                #CASO A LETRA NÂO NOS INTERESSE NÃO FAZEMOS NADA
        #AGORA VEMOS SE É UMA DAS EXTREMIDADES 
        frente = (1,0)
        frente_baixo = (1,1)
        baixo = (0,1)
        baixo_tras = (1,-1)
        #SE A LETRA FOR A PRIMEIRA
        if letra == palavra[0]:
            sentido = 1;
            atual_letra_pos = 0;

            adiciona_pedidas(letras_pedidas, palavra, pos_letra, frente, sentido, atual_letra_pos)
            adiciona_pedidas(letras_pedidas, palavra, pos_letra, frente_baixo, sentido, atual_letra_pos)
            adiciona_pedidas(letras_pedidas, palavra, pos_letra, baixo, sentido, atual_letra_pos)
            adiciona_pedidas(letras_pedidas, palavra, pos_letra, baixo_tras, sentido, atual_letra_pos)

        if letra == palavra[-1]:
            atual_letra_pos = -1
            sentido = -1

            adiciona_pedidas(letras_pedidas, palavra, pos_letra, frente, sentido, atual_letra_pos)
            adiciona_pedidas(letras_pedidas, palavra, pos_letra, frente_baixo, sentido, atual_letra_pos)
            adiciona_pedidas(letras_pedidas, palavra, pos_letra, baixo, sentido, atual_letra_pos)
            adiciona_pedidas(letras_pedidas, palavra, pos_letra, baixo_tras, sentido, atual_letra_pos)


def testar_funcs2():
    global palavas, sopa, palavras_acabadas
    dict_palavras = inicializa_dicionário([
        "FRIDAY", 
        "TUESDAY", 
        "MONDAY", 
        "WEEK",
        "DECEMBER"
        ])
    print(dict_palavras)
    for l in range(len(sopa)):
        for j in range(len(sopa[0])):
        #print("A LETRA E:", sopa[l][11], " E POS E:", (l,11))
            atualiza_palavras(dict_palavras, sopa[l][j], (l, j))
        #atualiza_palavras(dict_palavras, sopa[l][11], (l, 11))
        #inp = input("QUERES DICIONARIO?:")
        #if inp == "a":
        #    pprint(dict_palavras)
    print("PALAVRAS ACABADAS",palavras_acabadas)

    pprint(dict_palavras)
    #atualiza_palavras(dict_palavras, "M",(1,0))
    #pprint(dict_palavras)
    #atualiza_palavras(dict_palavras, "0",(0,1))
    #pprint(dict_palavras)

def testar_funcs():



def main():
    print("This is the project")
    testar_funcs()
    #print(sopa)
    #print(palavras)

    #Carregar os parâmetros da câmara ou obter uns novos
    #Obter as imagens
    #Obter a sopa
    #Resolver a sopa
    #Dar print das posições
    #Eventualmente colocar em live o vídeo


if __name__ == "__main__":
    main()

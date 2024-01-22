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

palavras_acabadas = [];

def calibra_camera():
    print("A calibrar a câmera")


def dilata(img):
    #Cria o kernel para a dilatação
    element_shape = cv2.MORPH_ELLIPSE
    element_size = 9
    element = cv2.getStructuringElement(element_shape, (element_size, element_size))

    #Aplica a dilatação N vezes
    n = 5
    for i in range(n):
        img = cv2.dilate(img, element)
    return img


def obtem_zonas_interesse():
    print("A obter a sopa")
    img = cv2.imread("SopaDeLetras2.png", cv2.IMREAD_GRAYSCALE)
    #img = cv2.imread("SopaDeLetras.png", cv2.IMREAD_GRAYSCALE)
    _, mask =  cv2.threshold(img, 150, 255, cv2.THRESH_BINARY_INV)

    image_dilated = dilata(mask)

    cv2.imshow("IMAGEM", img)
    cv2.imshow("MASK", image_dilated)
    cv2.waitKey(0);

    output = cv2.connectedComponentsWithStats(image_dilated, 4, cv2.CV_32S)
    (total_labels, labels, stats, centroids) = output

    print("CENTROIDS:", centroids)
    print("STATS:", stats)

    image_dilated = cv2.cvtColor(image_dilated,cv2.COLOR_GRAY2RGB)
    start_x_max = 0
    start_y_max = 0
    width_max = 0
    height_max = 0
    area_max = 0


    for i in range(1,total_labels):
        center = (int(centroids[i][0]),int(centroids[i][1]))
        cv2.circle(image_dilated, center, 5, (255,0,0), -1)
        start_point_x = stats[i, cv2.CC_STAT_LEFT]
        start_point_y = stats[i, cv2.CC_STAT_TOP]

        start_point = (start_point_x, start_point_y)
        width = stats[i, cv2.CC_STAT_WIDTH]
        height = stats[i,cv2.CC_STAT_HEIGHT]

        end_point = (start_point[0] + width, start_point[1] + height)
        cv2.rectangle(img, start_point, end_point, (0,255,0), 2)
        area = stats[i, cv2.CC_STAT_AREA]
        if area > area_max:
            area_max = area;
            start_x_max = start_point_x
            start_y_max = start_point_y
            height_max = height
            width_max = width


    sopa = mask[start_y_max: start_y_max + height_max, start_x_max: start_x_max + width_max]

    cv2.imshow("SOPA", sopa)
    
    output = cv2.connectedComponentsWithStats(sopa, 4, cv2.CV_32S)
    (total_labels, labels, stats, centroids) = output

    #print("CENTROIDS:", centroids)
    #print("STATS:", stats)
    print("LABELS", total_labels)

    cv2.imshow("IMAGEM", img)
    cv2.imshow("MASK", image_dilated)
    cv2.waitKey(0);



def obtem_sopa():
    #Inicializa a variável de retorno
    sopa = [];

    obtem_zonas_interesse()

    return sopa;


def inicializa_dicionário(palavras):
    #Inicializa variável de retorno
    palavras_dict = {};
    
    #Para cada palavra guardamos o seu comprimento e um dicionário com a correspondência
     #Entre as letras das quais estamos à procura e em qual posição do tabuleiro e da palavra estão
    for palavra in palavras:
        pal_size = len(palavra);


        #Terei um dicionario com as letras que quero
        #Correspondente a cada letra terei a palavra que quer a letra, a posicao na palavra, 
        #E a direção na qual a palavra está a ir (frente, baixo tras, baixo, frente baixo), bem como se é pelo sentido normal ou ao contrário
        dict_letras = {};
        #letras_pontas = (palavra[0], palavra[-1])
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
        #print("A PALAVRA: ", palavra, " ACABOU AQUI: ", pos_sopa)
        inicial = (pos_sopa[0]-(len(palavra)-1)*direcao[0], pos_sopa[1]-(len(palavra)-1)*direcao[1])
        palavras_acabadas = palavras_acabadas + [(palavra,inicial, pos_sopa)]
        return
    if (not 0 <= proxima_sopa_pos[0] < lim) or (not 0 <= proxima_sopa_pos[1] < lim):
        return;

    letras_dict[proxima_sopa_pos] = letras_dict.get(proxima_sopa_pos, [])+ [(palavra[proxima_letra_pos], direcao, sentido, proxima_letra_pos)]

def atualiza_palavras(palavras_dict, letra, pos_letra):
    #Para cada palavra
    for (palavra, letras_pedidas) in palavras_dict.items():
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
        #AGORA VEMOS SE É UMA DAS EXTREMIDADES 
        frente = (1,0)
        frente_baixo = (1,1)
        baixo = (0,1)
        baixo_tras = (1,-1)
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

def resolve_sopa(sopas, lista_palavras):
    global palavras_acabadas
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
            letra = sopa[x][y];
            atualiza_palavras(palavras_dict, letra, (x,y));

    print(palavras_acabadas)

def testar_funcs():
    global palavas, sopa, palavras_acabadas
    #resolve_sopa(sopa, palavras)
    obtem_sopa()

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

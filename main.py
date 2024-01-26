#!/usr/bin/env python3

import cv2
from pprint import pprint
import numpy as np
import pytesseract


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


sopa2 = [['F', 'N', 'X', 'G', 'L', 'K', 'Q', 'S', 'P', 'K', 'C', 'R', 'E', 'X', 'V', 'L', 'E', 'B', 'I', 'C', 'E', 'D', 'V', 'G'], ['U', 'N', 'O', 'D', 'O', 'O', 'Y', 'A', 'R', 'K', 'N', 'M', 'G', 'V', 'E', 'F', 'X', 'K', 'Q', 'V', 'L', 'M', 'N', 'Q'], ['K', 'F', 'W', 'I', 'Q', 'Y', 'J', 'I', 'X', 'U', 'E', 'W', 'I', 'B', 'T', 'B', 'D', 'A', 'I', 'X', 'S', 'P', 'U', 'W'], ['N', 'M', 'M', 'J', 'T', 'O', 'R', 'S', 'B', 'l', 'K', 'G', 'C', 'E', 'H', 'T', 'X', 'Y', 'W', 'P', 'S', 'G', 'P', 'V'], ['S', 'E', 'K', 'K', 'W', 'A', 'E', 'R', 'W', 'Z', 'E', 'S', 'C', 'Z', 'l', 'W', 'Q', 'I', 'B', 'T', 'W', 'J', 'M', 'U'], ['X', 'A', 'S', 'Y', 'P', 'C', 'C', 'M', 'H', 'D', 'X', 'C', 'O', 'K', 'P', 'F', 'T', 'N', 'C', 'O', 'O', 'X', 'Y', 'N'], ['A', 'R', 'B', 'R', 'M', 'G', 'H', 'O', 'R', 'A', 'L', 'U', 'C', 'I', 'D', 'N', 'E', 'P', 'R', 'E', 'P', 'C', 'K', 'D'], ['M', 'K', 'N', 'O', 'I', 'T', 'C', 'E', 'L', 'F', 'E', 'R', 'K', 'Q', 'Q', 'G', 'D', 'G', 'R', 'Y', 'M', 'W', 'W', 'N'], ['P', 'X', 'R', 'C', 'O', 'M', 'T', 'L', 'D', 'O', 'F', 'H', 'S', 'S', 'G', 'V', 'X', 'E', 'Q', 'B', 'X', 'l', 'D', 'O'], ['L', 'T', 'W', 'I', 'Z', 'F', 'X', 'F', 'A', 'Y', 'H', 'F', 'F', 'F', 'V', 'N', 'M', 'C', 'P', 'X', 'E', 'Y', 'S', 'I'], ['I', 'X', 'L', 'I', 'T', 'D', 'N', 'M', 'M', 'O', 'J', 'C', 'G', 'H', 'l', 'O', 'G', 'R', 'N', 'Z', 'H', 'V', 'O', 'T'], ['T', 'Z', 'T', 'T', 'R', 'R', 'U', 'L', 'W', 'E', 'Z', 'D', 'E', 'B', 'C', 'l', 'V', 'B', 'S', 'A', 'Q', 'F', 'U', 'C'], ['U', 'O', 'J', 'A', 'E', 'D', 'H', 'Z', 'W', 'A', 'W', 'Q', 'W', 'T', 'Z', 'S', 'Q', 'Z', 'U', 'Y', 'B', 'T', 'N', 'A'], ['D', 'U', 'R', 'V', 'H', 'O', 'F', 'D', 'R', 'L', 'Q', 'Y', 'W', 'G', 'R', 'N', 'N', 'U', 'X', 'R', 'W', 'D', 'R', 'A'], ['E', 'O', 'F', 'B', 'H', 'D', 'T', 'E', 'L', 'U', 'I', 'F', 'E', 'Q', 'C', 'E', 'M', 'O', 'E', 'F', 'R', 'H', 'V', 'F'], ['K', 'F', 'E', 'F', 'H', 'I', 'G', 'R', 'O', 'A', 'G', 'R', 'P', 'B', 'A', 'P', 'Y', 'F', 'A', 'P', 'X', 'W', 'P', 'E'], ['R', 'B', 'V', 'J', 'M', 'I', 'X', 'C', 'L', 'Z', 'K', 'E', 'V', 'P', 'Z', 'S', 'Y', 'N', 'T', 'Q', 'C', 'M', 'G', 'R'], ['X', 'Z', 'G', 'L', 'A', 'I', 'N', 'L', 'R', 'P', 'B', 'Q', 'P', 'Q', 'E', 'l', 'Q', 'K', 'Z', 'Q', 'L', 'l', 'Q', 'H'], ['B', 'M', 'V', 'Z', 'Q', 'I', 'G', 'U', 'L', 'R', 'D', 'U', 'X', 'D', 'H', 'D', 'A', 'X', 'H', 'M', 'H', 'A', 'Q', 'K'], ['W', 'A', 'G', 'R', 'T', 'P', 'Z', 'G', 'R', 'O', 'A', 'E', 'U', 'J', 'R', 'C', 'O', 'F', 'D', 'O', 'Z', 'E', 'U', 'D'], ['W', 'R', 'R', 'Z', 'L', 'E', 'B', 'W', 'G', 'M', 'P', 'N', 'G', 'M', 'N', 'S', 'T', 'N', 'L', 'I', 'Q', 'D', 'J', 'E'], ['Z', 'U', 'F', 'Q', 'I', 'U', 'Z', 'P', 'E', 'U', 'L', 'C', 'G', 'Q', 'U', 'C', 'F', 'I', 'Q', 'L', 'O', 'X', 'R', 'F'], ['R', 'Q', 'T', 'Y', 'W', 'T', 'J', 'K', 'W', 'l', 'E', 'Y', 'L', 'E', 'K', 'J', 'N', 'P', 'P', 'M', 'L', 'Q', 'X', 'J'], ['T', 'S', 'O', 'N', 'R', 'V', 'F', 'G', 'K', 'D', 'I', 'F', 'F', 'R', 'A', 'C', 'T', 'I', 'O', 'N', 'l', 'S', 'J', 'A']];




palavras = ["WEDNESDAY","DAYS","MONDAY","JANUARY","AUGUST","WINTER","AUTUMN","THURSDAY",
            "MARCH","OCTOBER","MAY","APRIL","FRIDAY","TUESDAY","SUNDAY","MONTHS","YEAR",
            "FEBRUARY","DECEMBER","WEEK", "AMANDA"];

palavras2 = ['DISPERSION', 'HERTZ', 'EAR', 'SONAR', 'RANGE', 'PERPENDICULAR', 'REFLECTION', 'PITCH', 'FREQUENCY', 'AMPLITUDE', 'DIFFRACTION', 'REFRACTION', 'SOUND', 'DECIBEL', 'ECHOLOCATION']


palavras_acabadas = [];

def calibra_camera():
    print("A calibrar a câmera")


def dilata(img):
    #Cria o kernel para a dilatação
    element_shape = cv2.MORPH_ELLIPSE
    element_size = 7
    element = cv2.getStructuringElement(element_shape, (element_size, element_size))

    #Aplica a dilatação N vezes
    n = 5
    for i in range(n):
        img = cv2.dilate(img, element)
    return img

def proximo_par(n):
    if n % 2 == 0:
        return n
    return n+1


def processa_palavras(img, stats, inds):
    
    #img2 = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    print(inds)
    palavras = []
    palavras_res = []

    for i in inds:
        cada_lista = []
        print("XZONA")
        corte_x_i = stats[i, cv2.CC_STAT_LEFT]
        corte_y_i = stats[i, cv2.CC_STAT_TOP]
        
        corte_x_f = corte_x_i + stats[i,cv2.CC_STAT_WIDTH]
        corte_y_f = corte_y_i + stats[i,cv2.CC_STAT_HEIGHT]

        corte_i = (corte_x_i, corte_y_i)
        corte_f = (corte_x_f, corte_y_f)

        corte = img[corte_y_i : corte_y_f, corte_x_i: corte_x_f]   
        #cv2.imshow("IMG", corte)
        #cv2.waitKey(0)
        cada_lista = processa_zona(corte, False)
        palavras = palavras + cada_lista

    for i in range(len(palavras)):
        palavras_res = palavras_res + [''.join(palavras[i])]

    return palavras_res

def processa_zona(zona, is_sopa):
    #zona = cv2.cvtColor(zona,cv2.COLOR_RGB2GRAY)

    output = cv2.connectedComponentsWithStats(zona, 4, cv2.CV_32S)
    (total_labels, labels, stats, centroids) = output

    print("LABELS", total_labels)
   
    larg = proximo_par(max(stats[1:,cv2.CC_STAT_WIDTH]))
    comp = proximo_par(max(stats[1:,cv2.CC_STAT_HEIGHT]))

    print("COMP: ", comp)
    print("LARG: ", larg)

    #cv2.waitKey(0)
    anterior = 0
    lista = []
    
    lista_pre = []
    if is_sopa:
        for i in range(1, total_labels):
            start_point_x = stats[i, cv2.CC_STAT_LEFT]
            start_point_y = stats[i, cv2.CC_STAT_TOP]

            width = stats[i, cv2.CC_STAT_WIDTH]
            height = stats[i,cv2.CC_STAT_HEIGHT]

            start_point = (start_point_x - 2, start_point_y - 2)
            end_point = (start_point_x + width + 2, start_point_y + comp + 2)

            #print("START_POIMT:", start_point, " END POINT:", end_point)

            letra = zona[start_point[1]: end_point[1], start_point[0]: end_point[0]] 
            letra = cv2.bitwise_not(letra)

            letra_char = find_letra2(letra)
            letra_char = letra_char[0]
            if letra_char == '0':
                letra_char = 'O'
            elif letra_char == '\x0c':
                letra_char = 'I'
            #print("A LETRA È:", letra_char)

            if abs(anterior - start_point[1]) > 10: #começou uma nova linha
                #print("NOVA LINHA")
                lista = lista + [lista_pre]
                lista_pre = [letra_char]
            else:
                lista_pre = lista_pre + [letra_char]
            anterior = start_point[1]
        lista = lista + [lista_pre]
        return lista[1:]
    else:
        #print(stats)
        for i in range(1, total_labels):
            start_point_x = stats[i, cv2.CC_STAT_LEFT]
            start_point_y = stats[i, cv2.CC_STAT_TOP]

            width = stats[i, cv2.CC_STAT_WIDTH]
            height = stats[i,cv2.CC_STAT_HEIGHT]

            start_point = (start_point_x - 2, start_point_y - 2)
            end_point = (start_point_x + width + 2, start_point_y + comp + 2)

    #        print("START_POIMT:", start_point, " END POINT:", end_point)

            letra = zona[start_point[1]: end_point[1], start_point[0]: end_point[0]] 
            letra = cv2.bitwise_not(letra)
            #cv2.imshow("LETRA", letra)
            #cv2.waitKey(0)

            letra_char = find_letra2(letra)
            letra_char = letra_char[0]
            if letra_char == '0':
                letra_char = 'O'
            elif letra_char == '\x0c':
                letra_char = 'I'
            #print("A LETRA È:", letra_char)

            if abs(anterior - start_point[1]) > 20: #começou uma nova linha
   #             print("ACABOU A PALAVRA", lista_pre)
                lista = lista + [lista_pre]
                lista_pre = [letra_char]
            else:
                lista_pre = lista_pre + [letra_char]
            anterior = start_point[1]
        lista = lista + [lista_pre]
    
        return lista


def find_letra2(letra):
    return pytesseract.image_to_string(letra, config = "-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0il --psm 10")


def find_letra(letra_image):
    min = 9999999999999;
    min_leter = 97;

    for i in range(97,123):
        templ_name = "letters/" + chr(i) +  ".png"
        templ = cv2.imread(templ_name, cv2.IMREAD_GRAYSCALE)
        match_method = cv2.TM_SQDIFF_NORMED
        res = cv2.matchTemplate(letra_image, templ, match_method)
        if res < min:
            min = res
            min_leter = i
    cv2.waitKey(0)
    return chr(min_leter)


def filtrar_zonas_interesse(img, image_dilated):
    output = cv2.connectedComponentsWithStats(image_dilated, 4, cv2.CV_32S)
    (total_labels, labels, stats, centroids) = output

    print("CENTROIDS:", centroids)
    print("STATS:", stats)

    image_dilated2 = cv2.cvtColor(image_dilated,cv2.COLOR_GRAY2RGB)

    #ACHAR O MAIOR AGLOMERADO E FILTRAR
    ind_max = 1
    others = []
    area_max = 0
    for i in range(2,total_labels):
        area = stats[i, cv2.CC_STAT_AREA]
        if area_max > area: 
            others = others + [ind_max]
            ind_max = i
            area_max = area
        else:
            others = others + [i]

    sopa_x_i = stats[ind_max, cv2.CC_STAT_LEFT]
    sopa_y_i = stats[ind_max, cv2.CC_STAT_TOP]
    
    sopa_x_f = sopa_x_i + stats[ind_max,cv2.CC_STAT_WIDTH]
    sopa_y_f = sopa_y_i + stats[ind_max,cv2.CC_STAT_HEIGHT]

    sopa_i = (sopa_x_i, sopa_y_i)
    sopa_f = (sopa_x_f, sopa_y_f)

    print("OTHERS: ", others)

    cv2.rectangle(img, sopa_i, sopa_f, (0,255,0), 2)
    
    sopa = img[sopa_y_i : sopa_y_f, sopa_x_i: sopa_x_f]
    sopa_letras = processa_zona(sopa, True)
    print(sopa_letras)
    print(sopa_letras)
    print("TAMANHOS DA SOPA")
    print(len(sopa_letras))
    for i in range(len(sopa_letras)):
        print(len(sopa_letras[i]))
    palavras = processa_palavras(img, stats, others)
    print(palavras)
    resolve_sopa(sopa_letras, palavras)

def obtem_zonas_interesse():
    print("A obter a sopa")
    img = cv2.imread("SopaDeLetras5.png", cv2.IMREAD_GRAYSCALE)
    _, mask =  cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
    
    #cv2.imshow("MASK_NOT_DILATED", mask)

    image_dilated = dilata(mask)

    cv2.imshow("IMAGEM", img)
    #cv2.imshow("MASK", image_dilated)
    #cv2.waitKey(0);

    filtrar_zonas_interesse(mask, image_dilated)

#

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
            print("X: ", x, " E Y:", y)
            letra = sopas[x][y];
            atualiza_palavras(palavras_dict, letra, (x,y));
    print(palavras_dict)
    print(palavras_acabadas)

def testar_funcs():
    global palavas2, sopa2, palavras_acabadas
    resolve_sopa(sopa2, palavras2)
    #obtem_sopa()

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

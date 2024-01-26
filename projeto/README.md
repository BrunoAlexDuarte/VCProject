

Projeto de VC

O nosso projeto de vC, cuja função é resolver sopas de letras, funciona da seguinte maneira,
primeiro lemos a imagem, onde assumimos que as letras estarão a preto e todas maiúsculas, isto pois
quando tínhamos letras em minúsculo em alguns casos havia confusão entre o 'L' minúsculo e o 'I' maiúsculo, 
dependendo da font que usávamos.
Após lermos a imagem, usamos operações de dilatação até termos um aglomerado com as letras da sopa, e assumimos
que os restantes aglomerados são as palavras que queremos procurar.
Após isso, temos que achar as letras. Inicialmente usávamos operações de fecho para as identificar melhor, no entanto
verificámos que no caso das palavras que queríamos às vezes 2 letras ficavam coladas, o que não era desejável, pelo
que decidimos detetar as letras como estas apareciam na imagem usando a função cv2.connectedComponentsWithStats(), que nos
retorna o número de aglomerados, (neste caso letras), dentro da imagem, bem como outros dados úteis para construir
um retângulo à volta da letra. Usando esses mesmos dados cortamos a letra para verificarmos a qual carater corresponde.
Para isso, inicialmente usamos TemplateMatching, no entanto isso revelou-se não muito preciso em alguns casos, por exemplo
'V' e 'Y', em que de vez em quando tínhamos uma troca entre ambos. Por isso decidímos usar a livraria Tesseract, que usa
modelos de aprendizagem para detetar letras, à custa de ser relativamente mais lento. Obtendo todas as letras da sopa e 
das palavras desejadas usamos um algoritmo para resolver a sopa de letras e no fim damos print a tuplos que correspondem 
a uma palavra, a posição inicial e final da mesma, e ao sentido (de trás para frente ou vice-versa) no qual a palavra aparece.
Este algoritmo funciona bem, achando sempre solução.
Um erro que tivemos foi que às vezes ao achar as letras a letra 'A' era considerada mais baixa que as outras, pelo que há casos
em que ela aparece no fim da linha quando não devia, pelo que algumas palavras ficam sem solução devido a essa troca, no entanto
a maioria das mesmas tem solução.



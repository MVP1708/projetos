#VOLUME <- COMPRIMENTO *  LARGURA * ALTURA
#VOLUME <- (4 / 3) * 3.14159 * (RAIO)
aquario = int(input('Qual o tamanho da aresta do aquário? '))
volume_aquario = (aquario)**3
volume_esfera = (4/3*3.14159*12.5)
peso = (volume_aquario - volume_esfera)/1000
print('O peso da esfera, nessas condições, será: ', peso, 'unidades de peso.')
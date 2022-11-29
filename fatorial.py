num = int(input('digite o numero que voce deseja saber o fatorial: '))
cont = num - 1
while True:
    if cont == 0:
        break
    else:
        res = cont * num
        num = res
        cont -= 1
print('o fatorial de {} eh {}'.format(num, res))

#coisas a melhorar:
#1 - imprimir o num sem ser o fatorial: check
#2 - melhorar o algoritmo, ta dando nojo olhar pra isso seu bosta: check filhadaputa
#3 - se pa ja vai ser consequencia do item 2, mas tentar diminuir o tamanho do algoritmo: check, de 10 foi para 7
#4 - dps de tudo isso ver na internet como outras pessoas fizeram, pra aumentar repertorio e melhorar a logica
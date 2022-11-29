num = int(input('digite um numero para saber seu fatorial: '))
cont = 1
res = num * (num - 1)
while cont < num - 2:
    cont += 1
    res = res * (num - cont)
    if num == 0:
        print('o fatorial de 0 eh 1')
print('o fatorial de {} eh {}'.format(num, res))

#updates
# 1 - tentar usar funções lambda

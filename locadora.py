
carros = [
        ('Chevrolet Tracker LTZ (Automatic)', 160),
        ('Chevrolet Onix LTZ (Automatic)', 130),
        ('Chevrolet Spin LTZ (Automatic)', 145),
        ('Volkswagen Gol (Manual)', 90),
        ('Volkswagen Polo (Automatic)', 110),
        ('Toyota Yaris (Automatic)', 115),
        ('Toyota Etios (Manual)', 95),
        ('Toyota Corolla XEI (Automatic)', 165),
        ('Fiat Uno Way (Manual)', 75),
        ('Fiat Mobi (Manual)', 85),
        ]
alugados = []


print('========')
print('Bem vindo a locadora de carros!')
print('========')


def lista_carros(lista):
    for i, car in enumerate(lista):
        print('[{}] {} - R$ {} /dia.'.format(i, car[0], car[1]))

lista_carros(carros)

while True:
    print('========')
    print('Bem vindo a locadora de carros!')
    print('========')
    print('O que deseja fazer? ')
    print('0 - Mostrar Portifolio | 1 - Alugar um carro | 2 - Devolver um carro')
    op = int(input())

    if op == 0:
        lista_carros(carros)
    
    
    elif op == 1:
        lista_carros(carros)
        print('======')
        print('Escolha um carro, usando o codigo dele.')
        cod_car = int(input())
        print('Quantos dias voce ira alugar o carro? ')
        dias = int(input())
        print('Voce escolheu {} por {} dias.'.format(carros[cod_car][0], dias))
        print('O aluguel totalizaria R$ {}. Deseja prosseguir?'.format(dias * carros[cod_car][1]))

        print('0 - SIM | 1 - NAO!')
        conf = int(input())
        if conf == 0:
            print ('Parabens, voce acabou de alugar o {} por {} dias'.format(carros[cod_car][0], dias))
            alugados.append(carros.pop(cod_car))

    
    elif op == 2:
        if len(alugados) == 0:
            print('Nao ha carros para devolver.')
        else:
            print('Segue a lista de carros alugados. Qual voce deseja devolver?')
            lista_carros(alugados)
            print('')
            print('Escolha o codigo do carro que quer devolver: ')
            cod = int(input())
            if conf == 0:
                print ('Obrigado por devolver o carro {}'.format(alugados[cod][0]))
                carros.append(alugados.pop(cod))

    print('========')
    print('0 - CONTINUAR | 1 - SAIR')
    if float(input()) == 1:
        break

import random

numero_empate = 0
numero_vitoria = 0
numero_derrota = 0

while True:
    usuario = input('Digite "P" para papel, "R" para pedra, "T" para tesoura, "X" para continuar, "Y" para mostrar o placar:   ')


    papel = 0
    pedra = 0
    tesoura = 0

    papel_pc = 0
    pedra_pc = 0
    tesoura_pc = 0


    if usuario == 'X'or usuario == 'x':
        print('O JOGO FOI ENCERRADO')
        break
    elif (usuario == 'P' or usuario == 'p'):
        usuario = '( PAPEL )'

    elif usuario == 'R' or usuario == 'r':
        usuario = '( PEDRA )'

    elif usuario == 'T' or usuario == 't':
        usuario = '( TESOURA ) '

    elif usuario == 'Y' or  usuario == 'y':
        usuario = (f'EMPATE: {numero_empate}, VITORIA: {numero_vitoria}, DERROTAS: {numero_derrota} ')
        print(usuario)
    else:
        
        
        
        
        
        '

    elif usuario_pc == 2:
        pedra_pc = 1
        print('PEDRA_PC', pedra_pc)
    elif tesoura_pc == 3:
        tesoura_pc = 1
        print('TESOURO', tesoura_pc)



    if usuario == 1 and usuario_pc == 1:
        print('EMPATE')
        numero_empate += 1
    elif usuario == 1 and usuario_pc == 1:
        print('VOCÊ VENCEU')
        numero_vitoria += 1
    elif usuario == 1 and usuario_pc == 1:
        print('VOCÊ PERDEU')
        numero_derrota += 1








    print('Você escolheu', usuario)
    print('O computador escolheu', usuario_pc)


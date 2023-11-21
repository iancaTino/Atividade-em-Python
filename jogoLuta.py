import random

# Vidas dos jogadores
vida_jogador = 10
vida_computador = 10

rodadas = 0
ataques = {1: 'Cabeçada', 2: 'Soco', 3: 'chute'}

print('\n...|JOGO DE BATALHA|...')
# Loop do while
while vida_jogador > 0 and vida_computador > 0:
    rodadas += 1
    print('\nRodada', rodadas)
    escolha = int(input('Escolha seu ataque:\n1 - cabeçada\n2 - soco\n3 - chute'))  # Escolher um ataque

    if escolha == 1:
        poder_jogador = 4
        dano_jogador = 1
        dano_computado = 3
    elif escolha == 2:
        poder_jogador = random.randint(1, 6)
        dano_jogador = random.randint(1, 6)
        dano_computado = 0
    elif escolha == 3:
        poder_jogador = random.randint(1, 6)
        dano_jogador = 3
        dano_computado = 3
    else:
        print('Escolha inválida, tente novamente.\n1 - cabeçada\n2 - soco\n3 - chute')
        continue

    # Ataque do computador
    poder_computador = random.randint(1, 6)
    dano_computado = random.randint(1, 6)

    # Cálculo do resultado do jogo
    if poder_jogador > poder_computador:
        vida_computador -= dano_jogador
    elif poder_jogador < poder_computador:
        vida_jogador -= dano_computado

    ataque_jogador = ataques[escolha]  # Obtém o nome do ataque escolhido
    print(f'Você usou o ataque {ataque_jogador} com poder {poder_jogador} e causou {dano_jogador} de dano.')
    print(f'O computador usou o ataque com poder {poder_computador} e causou {dano_computado} de dano.')
    print(f'Seu total de vida: {vida_jogador}')
    print(f'Vida do computador: {vida_computador}')

if vida_jogador <= 0:
    print('Você perdeu o jogo. O computador venceu.')
else:
    print('Parabéns! Você venceu o jogo.')
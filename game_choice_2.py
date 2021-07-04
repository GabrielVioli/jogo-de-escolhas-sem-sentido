def choice_a2():
    print('você será multado em 30,00$')
    choice_2a = input('você não tem esse dinheiro, deseja trabalhar?[S/N] ')
    if choice_2a in nao:
        print('voce perdeu o jogo, tente novamente')
    if choice_2a in sim:
        choice_2b = input('ao seu lado tem um cartaz contratando alguem, deseja se candidatar[S/N]')
        if choice_2b in nao:
            print('voce perdeu, tente novamente')
        if choice_2b in sim:
            choice_2c = input('''voce foi contratado!!, agora voce é garçom!!\n
            OOPS você derrubou um copo de suco na roupa de alguém, deseja pedir desculpas?[S/N] ''')
            if choice_2c in nao:
                print('voce perdeu, tente novamente')
            if choice_2c in sim:
                print('a mulher aceitou as desculpas')
                choice_2d = ('seu primeiro pagamento foi 200$, deseja pagar a multa?[S/N] ')
                if choice_2d in nao:
                    print('voce perdeu tente novamente')
                if choice_2d in sim:
                    print('voce ganhou o jogo!!!')
def choice_a3():
    choice_3a = ('voce entrou em um carro, a mulher lhe oferece uma bebida, voce aceita?[S/N]')
    if choice_3a in sim:
        print('voce perdeu, tente novamente')
    if choice_3a in nao:
        choice_3b = input('voce chegou em um galpão velho, a mulher te oferece uma pilula, voce aceita[S/N]')
        if choice_3a in nao:
            print('voce morreu')
        if choice_3a in sim:
            print('voce morreu')
running = 0 
while running <= 6:
    sim = ['s','sim']
    nao = ['n','nao']

    choice_1 = input('deseja continuar?[S/N] ').lower()

    if choice_1 not in ['s','n','nao','sim']:
        print('invalid option')
        running = running + 1
        
    else:
        
        if choice_1 in ['n','nao']:
            break

        elif choice_1 in ['s','não']:
            choice_2 = input('deseja jogar esse papel no lixo?[S/N] ')
            if choice_2 in nao:
                choice_a2()
                continue
            if choice_2 in sim:
                print('a pessoa ao seu lado te elogiou, parabens!!')
                choice_3 = input('''você está voltando pra casa, de repente uma mulher
                te aborda e pede pra segui-la, voce vai?[[S/N]? ''')
                if choice_3 in nao:
                    print('voce perdeu, tente novamente')
                if choice_3 in sim:
                    choice_a3()
                    
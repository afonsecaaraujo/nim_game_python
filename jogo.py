def computador_escolhe_jogada(n,m):
    return m if n%(m+1)==0 else n%(m+1)

def test_computador_escolhe_jogada():
    assert computador_escolhe_jogada(40,13) == 12
    assert computador_escolhe_jogada(20,3) == 3
    assert computador_escolhe_jogada(20,13) == 6
    assert computador_escolhe_jogada(1000,13) == 6
    assert computador_escolhe_jogada(15,13) == 1
    assert computador_escolhe_jogada(30,4) == 4
    assert computador_escolhe_jogada(36,5) == 5
    assert computador_escolhe_jogada(1,5) == 1
    assert computador_escolhe_jogada(13,13) == 13

def usuario_escolhe_jogada(n,m):
    jogadaValida = False
    while not jogadaValida:
        usuario= int(input("Quantas peças você vai tirar? "))
        if usuario >m or usuario<1:
            print("Oops! Jogada inválida! Tente de novo.")
        else:
            jogadaValida = True
    return usuario
    
def partida():
    n = int(input("Quantas peças? "))
    while n<=0:
        n1=int(input("Oops! Escolha pelo menos 1 peça! Tente de novo: "))
        n=n1
    m = int(input("Limite de peças por jogada? "))
    while m<=0:
        m1=int(input("Oops! Escolha pelo menos 1 peça! Tente de novo: "))
        m=m1

    print()

    pcturn= True
    x= n%(m+1)==0
    if x:
        print("Você começa!")
        print()
        pcturn= False
    else:
        print("Computador começa!")
        print()
        pcturn= True

    while n>0:
        quemganhou=0
        if not pcturn:
            y = usuario_escolhe_jogada(n,m)
            print("Você tirou ",y,"peças.")
            print()
            resto= n-y
            if resto ==0:
                ywin=print("Fim do jogo! Você ganhou!")
                print()
            else:
                print("Agora restam apenas" , resto, "peças no tabuleiro.")
                print()
            n = resto
            pcturn= True

        else:
            x = computador_escolhe_jogada(n,m)
            print("O computador tirou" ,x," peças.")
            print()
            resto= n-x
            if resto ==0:
                pcwin=print("Fim do jogo! O computador ganhou!")
                print()
            else:
                print("Agora restam apenas" , resto, "peças no tabuleiro.")
                print()
            n = resto
            pcturn= False

def main():
    print("Bem-vindo ao jogo do NIM! Escolha: ")
    print("1 - para jogar uma partida isolada " "2 - para jogar um campeonato: ")
    j=int(input())
    if j==1:
        partida()
    else:
        campeonato()

def campeonato():
    npartida=1
    while npartida<=3:
        print("**** Rodada", npartida,"****")
        partida()
        npartida= npartida+1      
    print("Placar: Você 0 X 3 Computador")

if __name__ == "__main__":
    main()
### imports ##
import os
from random import randint

### Variáveis ##
vitorias = 0
player1 = [0, 0] #[jogada, vitórias]
computador = [0, 0] #[jogada, vitórias]

### Funções ##
#Limpa a tela
def clear():
    os.system("cls")

#Teste de Logica do Jogo
def verifica_vencedor(p1, comp):
    pedra = 1
    papel = 2
    tesoura = 3

    if (p1 == comp):
        player1[1] += 0
        computador[1] += 0
    elif( p1 == pedra and comp == tesoura or p1 == papel and comp == pedra or p1 == tesoura and comp == papel):
        player1[1] += 1
        computador[1] += 0
    else:
        player1[1] += 0
        computador[1] += 1
    
#Telas
def tela_inicial():
    print("   ##################\n ")
    print("   Bem Vindo Ao Jogo!  \n")
    print("  PEDRA, PAPEL e TESOURA\n  ")
    print("   ##################\n  ")
    print(" ESCOLHA COM QUANTAS JOGADAS ")
    print("   Você será um Vencedor\n  ")
    vitorias = int(input(" Quantidade de vitórias: "))
    return vitorias

def tela_de_jogo(vit):
    rodada = 1
    empate = 0
    tem_jogo = True
    while(tem_jogo == True):
        clear()
        print("   ####################\n ")
        print("     ### # #### # # ### ")
        print("    ##  # # ## ###  #  ")
        print("   #   # #### # #  #  \n")
        print("   #################### ")
        print(f"       ROUND {rodada} \n")
        print("    PLACAR DA RODADA!")
        print(f"        Você: {player1[1]}")
        print(f"     Computador: {computador[1]}")
        print(f"      EMPATES: {empate} \n")
        print("   ####################\n  ")
        print("     1. PEDRA  ")
        print("     2. PAPEL  ")
        print("     3. TESOURA  \n")
        player1[0] = int(input("Escolha sua Jogada: "))
        computador[0] = randint(1, 3)
        rodada += 1
        if(player1[0] == computador[0]):
            empate += 1
        verifica_vencedor(player1[0], computador[0])
        if( player1[1] == vit or computador[1] == vit):
            tem_jogo = False

def tela_vitoria():
        clear()
        if( player1[1] > computador[1]):
            print("   ######################\n ")
            print("   ##    ##   ##  ##   ##  ")
            print("   ## # ##   ##  ## # ##  ")
            print("   ##  ##   ##  ##   ##  \n")
            print("   ###################### \n")
            print("    VOCÊ VENCEU!\n")
            print("     PARABÉNS!!\n")
            print("     PLACAR FINAL")
            print(f"        Você: {player1[1]}")
            print(f"     Computador: {computador[1]} \n")
        else:
            print("   ######################\n ")
            print("   ##    ##   ##  ##   ##  ")
            print("   ## # ##   ##  ## # ##  ")
            print("   ##  ##   ##  ##   ##  \n")
            print("   ###################### \n")
            print("    COMPUTADOR VENCEU!\n")
            print("     PLACAR FINAL")
            print(f"        Você: {player1[1]}")
            print(f"     Computador: {computador[1]} \n")           
##Jogo
def main():
    vitorias = tela_inicial()
    tela_de_jogo(vitorias)
    tela_vitoria()
    
main()
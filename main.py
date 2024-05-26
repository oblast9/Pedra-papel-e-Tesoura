from classe import *

print("-"*30)
print("  - PEDRA, PAPEL E TESOURA - ")
print("-"*30)

jgd = jokenpo("")

p1 = input(" digite seu nome jogador 1: ")
p2 = input(" digite seu nome jogador 2: ")

player1 = jokenpo(p1)
player2 = jokenpo(p2)

jogada1 = input(f"escreva sua jogada {player1.nome}: ")
jogada1 = jogada1.lower()
jogada2 = input(f"escreva sua jogada {player2.nome}: ")
jogada2 = jogada2.lower()
jgd.jogar(jogada1,jogada2)



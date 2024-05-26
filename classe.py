class jokenpo():
    def __init__(self,nome):
        self.nome = nome
        self.pedra = "pedra" 
        self.papel = "papel" 
        self.tesoura = "tesoura" 
    
    def jogar(self, jogada1, jogada2):

        if jogada1 == self.pedra and jogada2 == self.papel or jogada1 == self.papel and jogada2 == self.pedra:
            print(f"{self.papel} venceu")
        elif jogada2 == self.pedra and jogada1 == self.tesoura or jogada2 == self.papel and jogada1 == self.pedra:
            print(f"{self.papel} venceu")

        if jogada1 == self.tesoura and jogada2 == self.pedra or jogada1 == self.pedra and jogada2 == self.tesoura:
            print(f"{self.tesoura} venceu")
        elif jogada2 == self.tesoura and jogada1 == self.pedra or jogada2 == self.pedra and jogada1 == self.tesoura:
            print(f"{self.tesoura} venceu")

        if jogada1 == self.pedra and jogada2 == self.tesoura or jogada1 == self.tesoura and jogada2 == self.pedra:
            print(f"{self.pedra} venceu")
        elif jogada2 == self.pedra and jogada1 == self.tesoura or jogada2 == self.tesoura and jogada2 == self.pedra:
            print(f"{self.pedra} venceu")
        
        if jogada1 == self.pedra and jogada2 == self.pedra or jogada1 == self.papel and jogada2 == self.papel or jogada1 == self.tesoura and jogada2 == self.tesoura:
            print("empate")   
        elif jogada2 == self.pedra and jogada1 == self.pedra or jogada2 == self.papel and jogada1 == self.papel or jogada2 == self.tesoura and jogada1 == self.tesoura:
            print("empate")                     



#   pedra e papel = papel and papel e pedra = pepel
#  pedra e tesoura = pedra
#  pedra e pedra = empate
#  papel e pedra = papel
#  papel e tesoura = tesoura
#  papel e papel = empate
#  tesoura e pedra = pedra
#  tesoura e papel = tesoura
#  tesoura e tesoura = empate
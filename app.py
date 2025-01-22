my_name = "Tired"
#Print 
print("Hello and welcome " + my_name + "!")

class MeuPerfil:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar_perfil(self):
        #print("Meu nome é: " + self.nome + " e tenho: " + self.idade + " anos.")
        print('O nome é: {}'.format(self.nome),f"e tenho {self.idade} anos!")

class OutroPerfil:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def mostrar_perfil(self):
        print("O nome é: " + self.nome + " e a idade é " + self.idade)
        print('O nome é: {}! '.format(self.nome),f" e a idade é {self.idade} ")


def main():
    x = MeuPerfil('Fabricio', '21')
    # y = input("Qual seu nome?")
    # z = input("Qual sua idade?")
    MeuPerfil.mostrar_perfil(self=x)
    # print(y, z)

if __name__ == "__main__":
    main()



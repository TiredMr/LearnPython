my_name = "Tired"
#Print 
print("Hello and welcome " + my_name + "!")

class MeuPerfil:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar_nome(self):
        print("Meu nome é: " + self.nome)
    
    def mostrar_idade(self):
        print("Eu tenho: " + self.idade)

x = MeuPerfil('Fabricio', '21')

MeuPerfil.mostrar_nome(self=x)
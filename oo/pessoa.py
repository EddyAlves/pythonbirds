class Pessoa:
    def __init__(self, *filhos, nome=None, idade=32):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    edson = Pessoa(nome='Edson')
    eddy = Pessoa(edson, nome='Eddy')
    print(Pessoa.cumprimentar(eddy))
    print(id(eddy))
    print(eddy.cumprimentar())
    print(eddy.nome)
    print(eddy.idade)
    for filho in eddy.filhos:
        print(filho.nome)

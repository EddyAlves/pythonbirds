class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=32):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão'

class Multante(Pessoa):
    olhos = 3

if __name__ == '__main__':
    david = Multante(nome='David')
    eddy = Homem(david, nome='Eddy')
    print(Pessoa.cumprimentar(eddy))
    print(id(eddy))
    print(eddy.cumprimentar())
    print(eddy.nome)
    print(eddy.idade)
    for filho in eddy.filhos:
        print(filho.nome)
    eddy.sobrenome = 'Alves'
    del eddy.filhos
    eddy.olhos = 1
    del eddy.olhos
    print(eddy.__dict__)
    print(david.__dict__)
    print(Pessoa.olhos)
    print(eddy.olhos)
    print(david.olhos)
    print(id(Pessoa.olhos), id(eddy.olhos), id(david.olhos))
    print(Pessoa.metodo_estatico(), eddy.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), eddy.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(eddy, Pessoa))
    print(isinstance(eddy, Homem))
    print(david.olhos)
    print(eddy.cumprimentar())
    print(david.cumprimentar())

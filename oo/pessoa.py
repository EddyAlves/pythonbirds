class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=32):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá! {id(self)}'

if __name__ == '__main__':
    david = Pessoa(nome='David')
    eddy = Pessoa(david, nome='Eddy')
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
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(eddy.olhos)
    print(david.olhos)
    print(id(Pessoa.olhos), id(eddy.olhos), id(david.olhos))

from abc import ABC, abstractmethod

def limpar_tela():
    print("-----------------------------")

# 1 - Definição de classe abstrata
class Animal(ABC):
    @abstractmethod
    def falar(self):
        pass

class Cachorro(Animal):
    def falar(self):
        print("Au au!")

class Gato(Animal):
    def falar(self):
        print("Miau!")

c = Cachorro()
g = Gato()
c.falar()
g.falar()

limpar_tela()

# 2 - Proibição de instanciamento
try:
    a = Animal()
except TypeError as e:
    print("Erro ao instanciar Animal:", e)
    print("Não é possível instanciar uma classe abstrata que possui métodos abstratos.")

limpar_tela()

# 3 - Múltiplos métodos abstratos
class FormaGeometrica(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

class Retangulo(FormaGeometrica):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

    def perimetro(self):
        return 2 * (self.largura + self.altura)

r = Retangulo(5, 3)
print(f"Área do retângulo: {r.area()}")
print(f"Perímetro do retângulo: {r.perimetro()}")

limpar_tela()

# 4 - Herança parcial
class Transporte(ABC):
    @abstractmethod
    def mover(self):
        pass

    @abstractmethod
    def parar(self):
        pass

# Implementando apenas um método abstrato
class Carro(Transporte):
    def mover(self):
        print("Carro está se movendo.")

try:
    carro = Carro()
except TypeError as e:
    print("Erro ao instanciar Carro:", e)
    print("A subclasse ainda possui métodos abstratos não implementados.")

# Corrigindo a implementação
class CarroCompleto(Transporte):
    def mover(self):
        print("Carro está se movendo.")

    def parar(self):
        print("Carro parou.")

carro2 = CarroCompleto()
carro2.mover()
carro2.parar()

limpar_tela()
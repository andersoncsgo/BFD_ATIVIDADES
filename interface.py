from abc import ABC, abstractmethod

def limpar_tela():
    print("-----------------------------")

# 1 - Criando uma interface
class Pagamento(ABC):
    @abstractmethod
    def processar(self, valor):
        pass

class CartaoCredito(Pagamento):
    def processar(self, valor):
        print(f"Processando pagamento de R${valor:.2f} no cartão de crédito.")

class Boleto(Pagamento):
    def processar(self, valor):
        print(f"Processando pagamento de R${valor:.2f} via boleto.")

cartao = CartaoCredito()
boleto = Boleto()
cartao.processar(150.00)
boleto.processar(200.00)

limpar_tela()

# 2 - Interface múltipla
class Ligavel(ABC):
    @abstractmethod
    def ligar(self):
        pass

class Desligavel(ABC):
    @abstractmethod
    def desligar(self):
        pass

class Computador(Ligavel, Desligavel):
    def ligar(self):
        print("Computador ligado.")

    def desligar(self):
        print("Computador desligado.")

pc = Computador()
pc.ligar()
pc.desligar()

limpar_tela()

# 3 - Interface em herança múltipla
class Imprimivel(ABC):
    @abstractmethod
    def imprimir(self):
        pass

class Exportavel(ABC):
    @abstractmethod
    def exportar(self):
        pass

class Relatorio(Imprimivel, Exportavel):
    def imprimir(self):
        print("Relatório impresso.")

    def exportar(self):
        print("Relatório exportado.")

rel = Relatorio()
rel.imprimir()
rel.exportar()

limpar_tela()

# 4 - Forçando contrato
class Repositorio(ABC):
    @abstractmethod
    def salvar(self, objeto):
        pass

    @abstractmethod
    def buscar(self, id):
        pass

# Não implementando todos os métodos
class RepositorioMemoria(Repositorio):
    def salvar(self, objeto):
        print(f"Objeto {objeto} salvo na memória.")

try:
    repo = RepositorioMemoria()
except TypeError as e:
    print("Erro ao instanciar RepositorioMemoria:", e)
    print("A subclasse ainda possui métodos abstratos não implementados.")

# Forçando contrato
class RepositorioMemoriaCompleto(Repositorio):
    def salvar(self, objeto):
        print(f"Objeto {objeto} salvo na memória.")

    def buscar(self, id):
        print(f"Buscando objeto com id {id} na memória.")

repo2 = RepositorioMemoriaCompleto()
repo2.salvar("dados")
repo2.buscar(1)

limpar_tela()
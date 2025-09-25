# 1 - Crie uma classe Usuario com atributos nome e email. Depois, crie uma classe Cliente que herde de Usuario. Crie uma instancia de um cliente e acesse todos os atributos.
class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

# 2 - Implemente um método exibir_informacoes() na classe Usuario e herde esse método em Cliente. Mostre como chamar o método herdado a partir de um objeto Cliente.
    def exibir_informacoes(self):
        print(f"Nome: {self.nome}, Email: {self.email}")

# 3 - Na classe Usuario, crie um método saudacao() que retorna "Olá, usuário". Na classe Cliente, sobrescreva esse método para retornar "Olá, cliente". Mostre como funciona a chamada.
    def saudacao(self):
        return "Olá, usuário"

class Cliente(Usuario):
    def __init__(self, nome, email, saldo=0):
        super().__init__(nome, email)
        self.saldo = saldo
    def saudacao(self):
        return "Olá, cliente"

# Teste das questões 1, 2, 3 e 4
cliente1 = Cliente("Maria", "maria@email.com", 150)
print(cliente1.nome)
print(cliente1.email)
print(cliente1.saldo)
cliente1.exibir_informacoes()
print(cliente1.saudacao())

print("-----------------------------")

# 5 - Crie uma classe Funcionario que herda de Usuario e, em seguida, crie uma classe Gerente que herda de Funcionario. Mostre como instanciar um gerente e acessar seus atributos.
class Funcionario(Usuario):
    def __init__(self, nome, email, cargo):
        super().__init__(nome, email)
        self.cargo = cargo

class Gerente(Funcionario):
    def __init__(self, nome, email, cargo, setor):
        super().__init__(nome, email, cargo)
        self.setor = setor

gerente1 = Gerente("João", "joao@email.com", "Gerente", "Financeiro")
print(gerente1.nome)
print(gerente1.email)
print(gerente1.cargo)
print(gerente1.setor)

print("-----------------------------")

# 6 - Crie uma classe Autenticacao com um método login(). Crie outra classe Permissao com um método verificar_permissao(). Em seguida, crie uma classe Administrador que herda de ambas. Como usar os métodos herdados?
class Autenticacao:
    def login(self):
        print("Login realizado com sucesso!")
    def status(self):
        print("Status de autenticação")

class Permissao:
    def verificar_permissao(self):
        print("Permissão verificada!")
    def status(self):
        print("Status de permissão")

class Administrador(Autenticacao, Permissao):
    pass

admin1 = Administrador()
admin1.login()
admin1.verificar_permissao()
admin1.status()

print("-----------------------------")

# 7 - Usando o exemplo anterior, adicione um método status() em Autenticacao e também em Permissao. Se a classe Administrador herda das duas, qual versão de status() será chamada? Use Administrador.__mro__ para mostrar a ordem.
print("Ordem de resolução de métodos (MRO):")
for cls in Administrador.__mro__:
    print(cls)

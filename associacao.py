def limpar_tela():
    print("-----------------------------")

# 1 - Associação: Pessoa e Livro
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

class Livro:
    def __init__(self, titulo):
        self.titulo = titulo

pessoa = Pessoa("Ana")
livro = Livro("Python Básico")
print(f"{pessoa.nome} está lendo o livro '{livro.titulo}'.")

limpar_tela()

# 2 - Associação: Aluno e Ônibus
class Onibus:
    def __init__(self, linha):
        self.linha = linha

class Aluno:
    def __init__(self, nome):
        self.nome = nome

    def pegar_onibus(self, onibus):
        print(f"{self.nome} pegou o ônibus da linha {onibus.linha}.")

aluno = Aluno("Carlos")
onibus = Onibus("402")
aluno.pegar_onibus(onibus)

limpar_tela()

# 3 - Agregação: Funcionario e Departamento
class Funcionario:
    def __init__(self, nome):
        self.nome = nome

class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def listar_funcionarios(self):
        for f in self.funcionarios:
            print(f"{f.nome} faz parte do departamento {self.nome}.")

f1 = Funcionario("João")
f2 = Funcionario("Maria")
dep = Departamento("RH")
dep.adicionar_funcionario(f1)
dep.adicionar_funcionario(f2)
dep.listar_funcionarios()

limpar_tela()

# 4 - Agregação: Time e Jogador
class Jogador:
    def __init__(self, nome, posicao):
        self.nome = nome
        self.posicao = posicao

class Time:
    def __init__(self, nome):
        self.nome = nome
        self.jogadores = []

    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)

    def listar_jogadores(self):
        print(f"Jogadores do time {self.nome}:")
        for j in self.jogadores:
            print(f"{j.nome} - {j.posicao}")

j1 = Jogador("Pedro", "Atacante")
j2 = Jogador("Lucas", "Goleiro")
time = Time("Tigres")
time.adicionar_jogador(j1)
time.adicionar_jogador(j2)
time.listar_jogadores()

limpar_tela()

# 5 - Composição: Carro e Motor
class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

    def __del__(self):
        print("Motor destruído.")

class Carro:
    def __init__(self, modelo, potencia_motor):
        self.modelo = modelo
        self.motor = Motor(potencia_motor)

    def __del__(self):
        print(f"Carro {self.modelo} destruído.")

carro = Carro("Fusca", 1300)
print(f"Carro: {carro.modelo}, Motor: {carro.motor.potencia}cc")
del carro  # Ao deletar o carro, o motor também é destruído

limpar_tela()

# 6 - Composição: Casa e Comodos
class Comodo:
    def __init__(self, nome):
        self.nome = nome

class Casa:
    def __init__(self):
        self.comodos = [
            Comodo("Sala"),
            Comodo("Cozinha"),
            Comodo("Quarto"),
            Comodo("Banheiro")
        ]

    def listar_comodos(self):
        print("Cômodos da casa:")
        for c in self.comodos:
            print(c.nome)

casa = Casa()
casa.listar_comodos()

limpar_tela()
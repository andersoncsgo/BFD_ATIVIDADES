
# 1 - Crie uma classe chamada Pessoa que tenha os atributos nome e idade. Em seguida, crie dois objetos dessa classe e imprima os valores de seus atributos.
class Pessoa:
	def __init__(self, nome, idade):
		self.nome = nome
		self.idade = idade

p1 = Pessoa("João", 25)
p2 = Pessoa("Maria", 30)
print(f"Pessoa 1: nome={p1.nome}, idade={p1.idade}")
print(f"Pessoa 2: nome={p2.nome}, idade={p2.idade}")

print("-----------------------------")

# 2 - Expanda a classe Pessoa para incluir um método apresentar() que imprima uma frase como:"Olá, meu nome é João e tenho 25 anos.". Teste o método chamando-o a partir de um objeto.
class Pessoa:
	def __init__(self, nome, idade):
		self.nome = nome
		self.idade = idade
	def apresentar(self):
		print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

p3 = Pessoa("Carlos", 40)
p3.apresentar()

print("-----------------------------")

# 3 - Crie uma classe Carro com os atributos marca, modelo e ano. Use o método __init__ para inicializar esses valores. Crie três objetos e mostre suas informações.
class Carro:
	def __init__(self, marca, modelo, ano):
		self.marca = marca
		self.modelo = modelo
		self.ano = ano

carro1 = Carro("Toyota", "Corolla", 2020)
carro2 = Carro("Honda", "Civic", 2019)
carro3 = Carro("Ford", "Ka", 2018)
print(f"Carro 1: {carro1.marca}, {carro1.modelo}, {carro1.ano}")
print(f"Carro 2: {carro2.marca}, {carro2.modelo}, {carro2.ano}")
print(f"Carro 3: {carro3.marca}, {carro3.modelo}, {carro3.ano}")

print("-----------------------------")

# 4 - Usando a classe Carro, crie um objeto e depois altere o valor de um de seus atributos (por exemplo, mudar o ano). Imprima antes e depois da alteração.
carro4 = Carro("Fiat", "Uno", 2015)
print(f"Antes: {carro4.marca}, {carro4.modelo}, {carro4.ano}")
carro4.ano = 2022
print(f"Depois: {carro4.marca}, {carro4.modelo}, {carro4.ano}")

print("-----------------------------")

# 5 - Crie uma classe ContaBancaria com os atributos titular e saldo. Adicione um método depositar(valor) que aumenta o saldo e um método sacar(valor) que diminui o saldo (se houver saldo suficiente). Teste com depósitos e saques.
class ContaBancaria:
	def __init__(self, titular, saldo=0):
		self.titular = titular
		self.saldo = saldo
	def depositar(self, valor):
		self.saldo += valor
	def sacar(self, valor):
		if valor <= self.saldo:
			self.saldo -= valor
		else:
			print("Saldo insuficiente.")

conta = ContaBancaria("Ana", 100)
conta.depositar(50)
print(f"Saldo após depósito: {conta.saldo}")
conta.sacar(30)
print(f"Saldo após saque: {conta.saldo}")
conta.sacar(200)

print("-----------------------------")

# 6 - Modifique a classe ContaBancaria para que o método sacar retorne True se a operação for bem-sucedida e False caso contrário. Teste o retorno e imprima mensagens adequadas.
class ContaBancaria:
	def __init__(self, titular, saldo=0):
		self.titular = titular
		self.saldo = saldo
	def depositar(self, valor):
		self.saldo += valor
	def sacar(self, valor):
		if valor <= self.saldo:
			self.saldo -= valor
			return True
		else:
			return False

conta2 = ContaBancaria("Bruno", 200)
if conta2.sacar(100):
	print("Saque realizado com sucesso.")
else:
	print("Saldo insuficiente.")
if conta2.sacar(150):
	print("Saque realizado com sucesso.")
else:
	print("Saldo insuficiente.")

print("-----------------------------")

# 7 - Crie uma classe Aluno com atributos nome e nota. Depois crie uma classe Turma que tenha uma lista de alunos e um método adicionar_aluno(aluno). Crie alguns objetos Aluno e adicione-os à turma.
class Aluno:
	def __init__(self, nome, nota):
		self.nome = nome
		self.nota = nota

class Turma:
	def __init__(self):
		self.alunos = []
	def adicionar_aluno(self, aluno):
		self.alunos.append(aluno)

aluno1 = Aluno("Lucas", 8.5)
aluno2 = Aluno("Marina", 9.0)
aluno3 = Aluno("Pedro", 7.5)
turma = Turma()
turma.adicionar_aluno(aluno1)
turma.adicionar_aluno(aluno2)
turma.adicionar_aluno(aluno3)
for aluno in turma.alunos:
	print(f"Aluno: {aluno.nome}, Nota: {aluno.nota}")

print("-----------------------------")

# 8 - Na classe Aluno, implemente o método __str__ para que, ao imprimir um objeto da classe, apareça algo como:"Aluno: Maria - Nota: 9.5". Teste imprimindo os objetos.
class Aluno:
	def __init__(self, nome, nota):
		self.nome = nome
		self.nota = nota
	def __str__(self):
		return f"Aluno: {self.nome} - Nota: {self.nota}"

aluno4 = Aluno("Maria", 9.5)
aluno5 = Aluno("João", 8.0)
print(aluno4)
print(aluno5)

print("-----------------------------")

# 9 - Crie uma classe Cachorro com um atributo de classe especie = "Canis familiaris" e atributos de instância nome e idade. Mostre a diferença entre acessar especie pelo objeto e pela classe.
class Cachorro:
	especie = "Canis familiaris"
	def __init__(self, nome, idade):
		self.nome = nome
		self.idade = idade

dog = Cachorro("Rex", 3)
print(f"Acesso pelo objeto: {dog.especie}")
print(f"Acesso pela classe: {Cachorro.especie}")

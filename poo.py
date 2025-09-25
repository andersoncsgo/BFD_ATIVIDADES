
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

# -----------------------------
# -----------------------------
# -----------------------------
# Lista de Exercícios – POO classes e objetos
# 1 - Na classe ContaBancaria, converta saldo para um atributo privado. Crie um método setter e um getter para acessar e modificar esse atributo, seguindo uma regra lógica (Ex: saldo não pode ser negativo)
class ContaBancaria:
	def __init__(self, titular, saldo=0):
		self.titular = titular
		self.__saldo = saldo if saldo >= 0 else 0
	def depositar(self, valor):
		if valor > 0:
			self.__saldo += valor
	def sacar(self, valor):
		if 0 < valor <= self.__saldo:
			self.__saldo -= valor
			return True
		return False
	def get_saldo(self):
		return self.__saldo
	def set_saldo(self, novo_saldo):
		if novo_saldo >= 0:
			self.__saldo = novo_saldo
		else:
			print("Saldo não pode ser negativo!")

# Teste da questão 10
conta3 = ContaBancaria("Carlos", 500)
print(f"Saldo inicial: {conta3.get_saldo()}")
conta3.set_saldo(300)
print(f"Saldo após set_saldo(300): {conta3.get_saldo()}")
conta3.set_saldo(-100)  # Não deve permitir
print(f"Saldo final: {conta3.get_saldo()}")

print("-----------------------------")

# 2 - Crie uma classe, Pessoa, que tenha os atributos: nome, data de nascimento, cpf, identidade. Deixe os atributos cpf e identidade como privado e monte os métodos setters e getters para acessar e editar os valores
class Pessoa:
	def __init__(self, nome, data_nascimento, cpf, identidade):
		self.nome = nome
		self.data_nascimento = data_nascimento
		self.__cpf = cpf
		self.__identidade = identidade
	def get_cpf(self):
		return self.__cpf
	def set_cpf(self, novo_cpf):
		self.__cpf = novo_cpf
	def get_identidade(self):
		return self.__identidade
	def set_identidade(self, nova_identidade):
		self.__identidade = nova_identidade

# Teste da questão 1 e 2
pessoa1 = Pessoa("Anderson Silva", "01/06/1996", "263.263.151-12", "MG-12.345.678")
print(f"Nome: {pessoa1.nome}, Data de Nascimento: {pessoa1.data_nascimento}, CPF: {pessoa1.get_cpf()}, Identidade: {pessoa1.get_identidade()}")
pessoa1.set_cpf("987.654.321-00")
pessoa1.set_identidade("SP-98.765.432")
print(f"CPF atualizado: {pessoa1.get_cpf()}, Identidade atualizada: {pessoa1.get_identidade()}")

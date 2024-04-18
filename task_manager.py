# Definir aqui a classe para que sejam gerenciadas as tarefas.

from menu import Menu
import os
from functools import wraps
import json

class TaskManager:
	def __init__(self):
		# self.tarefas = {'Tarefa': [], 'Concluída': []}  # A lista de tarefas
		self.tarefas = self.carregar_tarefas()
		self.menu = Menu(self)  # Instanciando a classe Menu para ser usada


	def carregar_tarefas(self):
		try:
			with open('listaDeTarefas.json', 'r') as f:
				return json.load(f)
		except FileNotFoundError:
			return {'Tarefa': [], 'Concluída': []}


	def salvar_tarefas(self):
		with open('listaDeTarefas.json', 'w') as f:
			json.dump(self.tarefas, f)


	def voltar(func):  # Decorador para voltar ao menu.
		@wraps(func)
		def wrapper(*args, **kwargs):
			resultado = func(*args, **kwargs)  # Chamada da função decorada
			input('\nPressione Enter para voltar ao menu...')
			return  # Retorna o resultado da função decorada 
		return wrapper


	def resposta_erro(self):  # Função para responder quando há erro do usuário.
		input('\nEssa não é uma opção válida! Tente novamente.')


	def clear_screen(func):  # Decorador para limpar a tela
		@wraps(func)  # Função para manter os metadados da função original.
		def wrapper(*args, **kwargs):
			os.system('cls' if os.name == 'nt' else 'clear')  # Limpar de acordo com o OS
			return func(*args, **kwargs)  # Rodar a função como necessário.
		return wrapper


	@clear_screen
	def sair(self):  # Se despedir do usuário.
		print('Até breve!')
		input('Encerrando o programa. Digite Enter para sair...')
		quit()


	@clear_screen
	def visualizar(self):  # Imprime a lista de tarefas.
		print('LISTA DE TAREFAS')
		for posicao, tarefa in enumerate(self.tarefas['Tarefa'], start=1):
			concluida = self.tarefas["Concluída"][posicao - 1]
			print(f'{posicao} - {tarefa} - {concluida}')


	def visualizar_e_obter(self):  # Utilizado para não haver repetição de código.
		# Função para o usuário visualizar e dizer a tarefa que deseja editar/concluir/remover
		self.visualizar()

		entrada = input('\nDigite o número da tarefa: ')
		if entrada.strip():  # Verifica se a entrada não está vazia.	
			try:
				return int(entrada)
			except ValueError:
				self.resposta_erro()
		return None  # Retorna None se a entrada for inválida.

		'''
		O motivo de retornar None caso a entrada do usuário seja vazia é pelo fato de que o
		código acaba dando erro quando o usuário dá uma entrada vazia para as funções concluir,
		editar e remover. Nesse caso, fiz o código retornar None caso fosse uma entrada vazia,
		possibilitando o processamento do erro.
		'''


	@voltar
	@clear_screen
	def visualizar_tarefas_concluidas(self):  # Visualizar apenas tarefas concluídas.
		print('TAREFAS CONCLUÍDAS')

		for posicao, tarefa in enumerate(self.tarefas['Tarefa'], start=1):
			if self.tarefas['Concluída'][posicao - 1] == 'Concluída':
				# Verificar se a tarefa está marcada como concluída.
				print(f'{posicao} - {tarefa} - {self.tarefas["Concluída"][posicao - 1]}')


	@voltar
	@clear_screen
	def visualizar_tarefas_nao_concluidas(self):  # Visualizar apenas tarefas não concluídas.
		print('TAREFAS NÃO CONCLUÍDAS')

		for posicao, tarefa in enumerate(self.tarefas['Tarefa'], start=1):
			if self.tarefas['Concluída'][posicao - 1] != 'Concluída':
				# Verificar se a tarefa não está marcada como concluída.
				print(f'{posicao} - {tarefa} - {self.tarefas["Concluída"][posicao - 1]}')


	@voltar
	@clear_screen
	def adicionar(self):  # Adicionar uma nova tarefa.

			nova_tarefa = input('Dê um nome para a nova tarefa: ')

			self.tarefas['Tarefa'].append(nova_tarefa)
			self.tarefas['Concluída'].append('A fazer')  # Definir que a tarefa está por fazer (padrão)
			'''Enviar o input do usuário (nova_tarefa) à lista (tarefas)'''

			print(f'A tarefa "{nova_tarefa}" foi adicionada com sucesso.')

			self.salvar_tarefas()  # Salvar tarefas após adiciona.


	@voltar
	@clear_screen
	def concluir(self):  # Concluir uma tarefa
		try:  # Tratamento de erro
			print('CONCLUIR TAREFA')

			numero_tarefa = self.visualizar_e_obter()  # Coletar input do usuário

			if numero_tarefa is not None:  # Tratar um erro que quebra o código ao retornar None
				if numero_tarefa < 1 or numero_tarefa > len(self.tarefas['Tarefa']):
					print('Número de tarefa inválido. Por favor, digite um número válido.')
				else:
					self.tarefas['Concluída'][numero_tarefa - 1] = 'Concluída'
					# Marca a tarefa dada pelo usuário como concluída.
					print(f'A tarefa "{numero_tarefa}" foi definida como concluída')

					self.salvar_tarefas()
			else:
				self.resposta_erro()

		except ValueError:
			self.resposta_erro()


	@voltar
	@clear_screen
	def editar(self):  # Editar o nome de uma tarefa da lista.
		try:  # Tratamento de erros.
			print('EDITAR TAREFA')

			numero_tarefa = self.visualizar_e_obter()

			if numero_tarefa is not None:  # Tratar um erro que quebra o código ao retornar None
				if numero_tarefa < 1 or numero_tarefa > len(self.tarefas['Tarefa']):
					print('Número de tarefa inválido. Por favor, digite um número válido.')
				else:
					novo_nome = input('Insira o novo nome da tarefa: ')  # Solicita um novo nome

					self.tarefas['Tarefa'][numero_tarefa - 1] = novo_nome
					# Muda o nome da tarefa a partir do índice da lista!

					print(f'A tarefa {numero_tarefa} foi renomeada com sucesso.')

					self.salvar_tarefas()

		except ValueError:
			self.resposta_erro()


	@voltar
	@clear_screen
	def remover(self):  # Remover uma tarefa da lista.
		try:  # Tratamento de erros.
			print('REMOVER TAREFA')

			numero_tarefa = self.visualizar_e_obter()
			'''Verificar se a entrada foi válida. Dessa forma, indicar em caso de erro.
			Se for maior que o número de dados na lista ou se for menor que 1
			(a lista é enumerada de 1 a infinito), irá enviar uma mensagem de erro.
			Caso insira um caractere inválido ele enviará uma mensagem de erro.'''
			
			if numero_tarefa is not None:  # Tratar um erro que quebra o código ao retornar None
				if numero_tarefa < 1 or numero_tarefa > len(self.tarefas['Tarefa']):
					print('Número de tarefa inválido. Por favor, digite um número válido.')
				else:
					'''
					Usar o método 'pop' para remover a tarefa da lista e manter
					pareado com o número na lista.
					'''
					tarefa_removida = self.tarefas['Tarefa'].pop(numero_tarefa - 1)
					tarefa_concluida = self.tarefas['Concluída'].pop(numero_tarefa - 1)

					print(f'A tarefa "{tarefa_removida}" foi removida da lista.')
					# Indicar ao usuário qual item fora removido.

					self.salvar_tarefas()

		except ValueError:
			self.resposta_erro()

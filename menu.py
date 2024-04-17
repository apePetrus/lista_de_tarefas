# Definir aqui a classe para que o Menu seja rodado.

class Menu:
	def __init__(self, task_manager):	
		self.task_manager = task_manager  # Instanciar a classe TaskManager.


	def mostrar_menu(self):  # Mostar todas as opções do menu.
		self.task_manager.visualizar()  # Chamar o método de visualizar da classe TaskManager


		# Listar as opções do usuário
		print('\nO que deseja fazer?')
		print('1 - Adicionar tarefa')
		print('2 - Marcar tarefa como concluída')
		print('3 - Remover tarefa')
		print('4 - Editar')
		print('5 - Visualizar tarefas concluídas')
		print('6 - Visualizar tarefas não concluídas')
		print('7 - Sair')


	def coletar_escolha(self):  # Coleta a escolha do usuário.
		# Tratamento de erro dentro de cada opção
		try:
			opcao = int(input('\nDigite o número da opção que deseja escolher: '))
			return opcao  # Retorna a escolha do usuário sobre o menu.

		except ValueError:
			self.mostrar_menu()


	def processar_escolha(self, opcao):  # Processa a escolha do usuário e roda a função necessária.
		if opcao == 1:
			self.task_manager.adicionar()  # Chamar o método adicionar da classe TaskManager
		elif opcao == 2:
			self.task_manager.concluir()
		elif opcao == 3:
			self.task_manager.remover()
		elif opcao == 4:
			self.task_manager.editar()
		elif opcao == 5:
			self.task_manager.visualizar_tarefas_concluidas()
		elif opcao == 6:
			self.task_manager.visualizar_tarefas_nao_concluidas()
		elif opcao == 7:
			self.task_manager.sair()
		else:
			self.mostrar_menu()


	def executar(self):  # Loop principal do programa.
		'''Mostra o menu, coleta a escolha do usuário e processa ela.'''
		while True:  # Repetir até que o usuário escolha sair do programa.
			self.mostrar_menu()
			opcao = self.coletar_escolha()
			if opcao is not None:
				self.processar_escolha(opcao)
			else:
				print('Opção inválida. Tente novamente.')

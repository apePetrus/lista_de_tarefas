# To-do list


import os  # Para função de limpeza da tela.


tarefas = {'Tarefa': [], 'Concluída': []}
# Dicionário para o nome da tarefa e seu status.


def voltar():
	input('\nPressione Enter para voltar ao menu...')


def resposta_erro():
	input('\nEssa não é uma opção válida! Tente novamente.')


def sair():  # Se despedir do usuário.
	limpar()

	print('Até breve!')
	input('Encerrando o programa. Digite Enter para sair...')


def limpar():
	# Verificar o sistema operacional
	if os.name == 'nt':  # Windows usa 'cls' para limpar (feio e porco)
		os.system('cls')
	else:  # Qualquer outro OS, usar a função 'clear' (belo e moral)
		os.system('clear')


def menu():  # Menu principal
	limpar()

	print('LISTA DE TAREFAS')
	
	visualizar()  # Visualizar a lista logo no menu


	# Listar as opções do usuário
	print('\nO que deseja fazer?')
	print('1 - Adicionar tarefa')
	print('2 - Marcar tarefa como concluída')
	print('3 - Remover tarefa')
	print('4 - Editar')
	print('5 - Visualizar tarefas concluídas')
	print('6 - Visualizar tarefas não concluídas')
	print('7 - Sair')


	# Tratamento de erro dentro de cada opção
	try:
		opcao = int(input('\nDigite o número da opção que deseja escolher: '))

		if opcao == 1:
			adicionar()
		elif opcao == 2:
			concluir()
		elif opcao == 3:
			remover()
		elif opcao == 4:
			editar()
		elif opcao == 5:
			visualizar_tarefas_concluidas()
		elif opcao == 6:
			visualizar_tarefas_nao_concluidas()
		elif opcao == 7:
			sair()
		else:
			menu()

	except ValueError:
		menu()


def visualizar():  # Imprime a lista de tarefas.
	for posicao, tarefa in enumerate(tarefas['Tarefa'], start=1):
		concluida = tarefas["Concluída"][posicao - 1]
		print(f'{posicao} - {tarefa} - {concluida}')


def visualizar_e_obter():  # Utilizado para não haver repetição de código.
	# Função para o usuário visualizar e dizer a tarefa que deseja editar/concluir/remover
	visualizar()

	entrada = input('\nDigite o número da tarefa: ')
	if entrada.strip():  # Verifica se a entrada não está vazia.	
		try:
			return int(entrada)
		except ValueError:
			resposta_erro()
	return None  # Retorna None se a entrada for inválida.

	'''
	O motivo de retornar None caso a entrada do usuário seja vazia é pelo fato de que o
	código acaba dando erro quando o usuário dá uma entrada vazia para as funções concluir,
	editar e remover. Nesse caso, fiz o código retornar None caso fosse uma entrada vazia,
	possibilitando o processamento do erro.
	'''


def visualizar_tarefas_concluidas():
	limpar()
	print('TAREFAS CONCLUÍDAS')

	for posicao, tarefa in enumerate(tarefas['Tarefa'], start=1):
		if tarefas['Concluída'][posicao - 1] == 'Concluída':
			print(f'{posicao} - {tarefa} - {tarefas["Concluída"][posicao - 1]}')
	voltar()
	menu()

def visualizar_tarefas_nao_concluidas():
	limpar()
	print('TAREFAS NÃO CONCLUÍDAS')

	for posicao, tarefa in enumerate(tarefas['Tarefa'], start=1):
		if tarefas['Concluída'][posicao - 1] != 'Concluída':
			print(f'{posicao} - {tarefa} - {tarefas["Concluída"][posicao - 1]}')
	voltar()
	menu()


def adicionar():  # Adicionar uma nova tarefa à lista.
	limpar()

	nova_tarefa = input('Dê um nome para a nova tarefa: ')

	tarefas['Tarefa'].append(nova_tarefa)
	tarefas['Concluída'].append('A fazer')
	'''Enviar o input do usuário (nova_tarefa) à lista (tarefas)'''

	print(f'A tarefa "{nova_tarefa}" foi adicionada com sucesso.')

	voltar()
	menu()


def concluir():
	try:  # Tratamento de erro
		limpar()
		print('CONCLUIR TAREFA')

		numero_tarefa = visualizar_e_obter()  # Coletar input do usuário

		if numero_tarefa is not None:  # Tratar um erro que quebra o código ao retornar None
			if numero_tarefa < 1 or numero_tarefa > len(tarefas['Tarefa']):
				print('Número de tarefa inválido. Por favor, digite um número válido.')
			else:
				tarefas['Concluída'][numero_tarefa - 1] = 'Concluída'
				# Marca a tarefa dada pelo usuário como concluída.
		else:
			resposta_erro()

	except ValueError:
		resposta_erro()

	menu()


def editar():  # Editar o nome de uma tarefa da lista.
	try:  # Tratamento de erros.
		limpar()
		print('EDITAR TAREFA')

		numero_tarefa = visualizar_e_obter()

		if numero_tarefa is not None:  # Tratar um erro que quebra o código ao retornar None
			if numero_tarefa < 1 or numero_tarefa > len(tarefas['Tarefa']):
				print('Número de tarefa inválido. Por favor, digite um número válido.')
			else:
				novo_nome = input('Insira o novo nome da tarefa: ')  # Solicita um novo nome

				tarefas['Tarefa'][numero_tarefa - 1] = novo_nome
				# Muda o nome da tarefa a partir do índice da lista!

				print(f'A tarefa {numero_tarefa} foi renomeada com sucesso.')

	except ValueError:
		resposta_erro()

	voltar()
	menu()


def remover():  # Remover uma tarefa da lista.
	try:  # Tratamento de erros.
		limpar()
		print('REMOVER TAREFA')

		numero_tarefa = visualizar_e_obter()
		'''Verificar se a entrada foi válida. Dessa forma, indicar em caso de erro.
		Se for maior que o número de dados na lista ou se for menor que 1
		(a lista é enumerada de 1 a infinito), irá enviar uma mensagem de erro.
		Caso insira um caractere inválido ele enviará uma mensagem de erro.'''
		
		if numero_tarefa is not None:  # Tratar um erro que quebra o código ao retornar None
			if numero_tarefa < 1 or numero_tarefa > len(tarefas['Tarefa']):
				print('Número de tarefa inválido. Por favor, digite um número válido.')
			else:
				'''
				Usar o método 'pop' para remover a tarefa da lista e manter
				pareado com o número na lista.
				'''
				tarefa_removida = tarefas['Tarefa'].pop(numero_tarefa - 1)
				tarefa_concluida = tarefas['Concluída'].pop(numero_tarefa - 1)

				print(f'A tarefa "{tarefa_removida}" foi removida da lista.')
				# Indicar ao usuário qual item fora removido.

	except ValueError:
		resposta_erro()

	voltar()
	menu()


menu()

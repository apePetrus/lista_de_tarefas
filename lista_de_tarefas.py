# To-do list


import os


tarefas = []


def sair():  # Se despedir do usuário.
	limpar()

	print('Até breve!')
	input('Encerrando o programa. Digite Enter para sair...')


def limpar():
	# Verificar o sistema operacional
	if os.name == 'nt':  # Windows
		os.system('cls')
	else:  # Qualquer outro usar a função clear (belo e moral)
		os.system('clear')


def menu():  # Menu principal
	limpar()

	print('LISTA DE TAREFAS\n')
	
	visualizar()  # Visualizar a lista logo no menu


	# Listar as opções do usuário
	print('\nO que deseja fazer?')
	print('1 - Adicionar tarefa')
	print('2 - Remover tarefa')
	print('3 - Sair')


	# Tratamento de erro dentro de cada opção
	try:
		opcao = int(input('Digite o número da opção que deseja escolher\
: '))

		if opcao == 1:
			adicionar()
		elif opcao == 2:
			remover()
		elif opcao == 3:
			sair()


	except ValueError:
		print('Essa não é uma opção válida! Tente novamente.')
		menu()


def visualizar():  # Imprime a lista de tarefas.
	for posicao, tarefa in enumerate(tarefas, start=1):
		print(f'{posicao} - {tarefa}')


def adicionar():  # Adicionar uma nova tarefa à lista.
	limpar()

	nova_tarefa = input('Dê um nome para a nova tarefa: ')

	tarefas.append(nova_tarefa)
	'''Enviar o input do usuário (nova_tarefa) à lista (tarefas)'''

	print(f'A tarefa "{nova_tarefa}" foi adicionada com sucesso.')

	input('Pressione Enter para voltar ao menu...')
	menu()


def remover():  # Remover uma tarefa da lista.
	limpar()

	visualizar()  # Mostrar a lista para que o usuário possa ver o que
				  # irá remover.


	try:  # Tratamento de erros.
		numero_tarefa = int(input('Digite o número da tarefa que deseja\
 excluir: '))

		'''Verificar se a entrada foi válida. Dessa forma, indicar em
		caso de erro. Se for maior que o número de dados na lista ou
		se for menor que 1 (a lista é enumerada de 1 a infinito), irá
		enviar uma mensagem de erro. Caso insira um caractere inválido
		ele enviará uma mensagem de erro.'''
		if numero_tarefa < 1 or numero_tarefa > len(tarefas):
			print('Número de tarefa inválido. Por favor, digite um núme\
ro válido.')
		else:  # Usar o método 'pop' para remover a tarefa da lista.
			tarefa_removida = tarefas.pop(numero_tarefa - 1)
			print(f'A tarefa "{tarefa_removida}" foi removida da lista.\
')  # Indicar ao usuário qual item fora removido.

	except ValueError:
		print('Entrada inválida. Por favor, digite um número inteiro vá\
lido.')

	input('Pressione Enter para voltar ao menu...')
	menu()


menu()

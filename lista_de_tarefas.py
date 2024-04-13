# To-do list


import os  # Para função de limpeza da tela.


tarefas = {'Tarefa': [], 'Concluída': []}
# Dicionário para o nome da tarefa e seu status.


def voltar():
	input('Pressione Enter para voltar ao menu...')


def resposta_erro():
	print('Essa não é uma opção válida! Tente novamente.')


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

	print('LISTA DE TAREFAS\n')
	
	visualizar()  # Visualizar a lista logo no menu


	# Listar as opções do usuário
	print('\nO que deseja fazer?')
	print('1 - Adicionar tarefa')
	print('2 - Marcar tarefa como concluída')
	print('3 - Remover tarefa')
	print('4 - Sair')


	# Tratamento de erro dentro de cada opção
	try:
		opcao = int(input('\nDigite o número da opção que deseja escolher: '))

		if opcao == 1:
			adicionar()
		elif opcao == 3:
			remover()
		elif opcao == 2:
			concluir()
		elif opcao == 4:
			sair()


	except ValueError:
		menu()


def visualizar():  # Imprime a lista de tarefas.
	for posicao, tarefa in enumerate(tarefas['Tarefa'], start=1):
		concluida = tarefas["Concluída"][posicao - 1]
		print(f'{posicao} - {tarefa} - {concluida}')


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
	limpar()

	visualizar()  # Ajudar o usuário a visualizar o que ele fará.

	try:  # Tratamento de erro
		numero_tarefa = int(input('Digite o número da tarefa que deseja marcar como concluída: '))
		# Coletar input do usuário

		if numero_tarefa <1 or numero_tarefa > len(tarefas):
			print('Número de tarefa inválido. Por favor, digite um número válido.')
		else:
			tarefas['Concluída'][numero_tarefa - 1] = 'Concluída'
			# Marca a tarefa dada pelo usuário como concluída.

	except ValueError:
		resposta_erro()

	menu()




def remover():  # Remover uma tarefa da lista.
	limpar()

	visualizar()  # Mostrar a lista para que o usuário possa ver o que
				  # irá remover.


	try:  # Tratamento de erros.
		numero_tarefa = int(input('Digite o número da tarefa que deseja excluir: '))

		'''Verificar se a entrada foi válida. Dessa forma, indicar em
		caso de erro. Se for maior que o número de dados na lista ou
		se for menor que 1 (a lista é enumerada de 1 a infinito), irá
		enviar uma mensagem de erro. Caso insira um caractere inválido
		ele enviará uma mensagem de erro.'''
		if numero_tarefa < 1 or numero_tarefa > len(tarefas):
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

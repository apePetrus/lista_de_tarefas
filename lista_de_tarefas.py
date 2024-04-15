# Importar as classes.
from task_manager import TaskManager
from menu import Menu


def main():
	task_manager = TaskManager()
	menu = Menu(task_manager)
	# Classes instanciadas.

	menu.executar()  # Loop principal do código.


if __name__ == "__main__":
	main()
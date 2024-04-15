from task_manager import TaskManager
from menu import Menu


def main():
	task_manager = TaskManager()
	menu = Menu(task_manager)

	menu.executar()


if __name__ == "__main__":
	main()
from src.controller import Controller
from src.console_user_interface import ConsoleUserInterface

if __name__ == "__main__":
    user_interface = ConsoleUserInterface()
    controller = Controller(user_interface)
    controller.run()
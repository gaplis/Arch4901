from abc import ABC, abstractmethod


class IUserInput(ABC):

    @abstractmethod
    def handler_user_input(self, user_command):
        pass

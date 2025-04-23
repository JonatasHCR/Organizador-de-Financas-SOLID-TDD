from abc import ABC, abstractmethod


class Service(ABC):
    @abstractmethod
    def inserir(self):
        pass
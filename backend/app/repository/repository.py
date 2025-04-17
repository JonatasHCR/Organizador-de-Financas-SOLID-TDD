from abc import ABC, abstractmethod


class Repository(ABC):
    @abstractmethod
    def connectar(self):
        pass

    @abstractmethod
    def desconectar(self):
        pass

    @abstractmethod
    def criar_tabela(self):
        pass

    @abstractmethod
    def inserir(self):
        pass

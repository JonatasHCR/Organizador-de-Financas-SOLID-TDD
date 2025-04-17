from os import getenv

import psycopg2
from dotenv import load_dotenv

from .repository import Repository

load_dotenv()


class RepositoryAtivo(Repository):
    def __init__(self):
        self.host = getenv("HOST")
        self.database = getenv("DATABASE")
        self.user = getenv("USER")
        self.password = getenv("PASSWORD")

        self.criar_tabela()

    def connectar(self):
        self.conenection = psycopg2.connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password,
        )
        self.cursor = self.conenection.cursor()

    def desconectar(self):
        self.cursor.close()
        self.conenection.close()

    def criar_tabela(self):
        try:
            self.connectar()

            query = """
            CREATE TABLE IF NOT EXISTS ativos (
                id SERIAL PRIMARY KEY,
                name VARCHAR(25) NOT NULL,
                descricao TEXT,
                valor REAL NOT NULL,
                data DATE NOT NULL,
                fixo CHAR(1) NOT NULL,
                tipo_remuneracao VARCHAR(1)
            );
            """

            self.cursor.execute(query)
            self.conenection.commit()

        finally:
            self.desconectar()

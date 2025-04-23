from os import getenv
from sys import path

import psycopg2
from dotenv import load_dotenv

from .repository import Repository
from app.models.model_investimento import ModelInvestimento

load_dotenv()

PROJECT_ROOT = getenv("PROJECT_ROOT")
path.insert(0, PROJECT_ROOT)


class RepositoryInvestimento(Repository):
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
            CREATE TABLE IF NOT EXISTS investimentos (
                id SERIAL PRIMARY KEY,
                nome VARCHAR(25) NOT NULL,
                descricao TEXT,
                tipo CHAR(1) NOT NULL CHECK (tipo IN ('A', 'FII', 'C', 'ETF', 'ETFI', 'AI', 'TD', 'RF')),
                valor REAL NOT NULL,
                data DATE NOT NULL
            );
            """

            self.cursor.execute(query)
            self.conenection.commit()

        finally:
            self.desconectar()

    def inserir(self, investimento: ModelInvestimento):
        try:
            self.criar_tabela()

            self.connectar()

            query = """
            INSERT INTO investimentos (nome, descricao, tipo, valor, data)
            VALUES (%s, %s, %s, %s, %s)
            """

            self.cursor.execute(query, investimento.to_list()[1:])
            self.conenection.commit()

        finally:
            self.desconectar()

    def modificar(self, investimento: ModelInvestimento):
        try:
            self.criar_tabela()

            self.connectar()

            query = """
            UPDATE investimentos 
            SET
                nome = %s, 
                descricao = %s, 
                tipo = %s, 
                valor = %s, 
                data = %s
            WHERE id = %s;
            """
            valores = investimento.to_list()[1:] + [investimento.id]

            self.cursor.execute(query, valores)
            self.conenection.commit()

        finally:
            self.desconectar()

    def deletar(self, investimento: ModelInvestimento):
        try:
            self.criar_tabela()

            self.connectar()

            query = """
            DELETE FROM investimentos 
            WHERE id = %s;
            """

            self.cursor.execute(query, (str(investimento.id)))
            self.conenection.commit()

        finally:
            self.desconectar()

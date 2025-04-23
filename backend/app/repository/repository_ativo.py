from os import getenv
from sys import path

import psycopg2
from dotenv import load_dotenv

from .repository import Repository
from app.models.model_ativo import ModelAtivo

load_dotenv()

PROJECT_ROOT = getenv("PROJECT_ROOT")
path.insert(0, PROJECT_ROOT)


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
                nome VARCHAR(25) NOT NULL,
                descricao TEXT,
                valor REAL NOT NULL,
                data DATE NOT NULL,
                fixo CHAR(1) NOT NULL CHECK (fixo IN ('S', 'N')),
                tipo_remuneracao VARCHAR(1)
            );
            """

            self.cursor.execute(query)
            self.conenection.commit()

        finally:
            self.desconectar()

    def inserir(self, ativo: ModelAtivo):
        try:
            self.criar_tabela()

            self.connectar()

            query = """
            INSERT INTO ativos (nome, descricao, valor, data, fixo, tipo_remuneracao)
            VALUES (%s, %s, %s, %s, %s, %s)
            """

            self.cursor.execute(query, ativo.to_list()[1:])
            self.conenection.commit()

        finally:
            self.desconectar()

    def modificar(self, ativo: ModelAtivo):
        try:
            self.connectar()

            query = """
            UPDATE ativos 
            SET
                nome = %s, 
                descricao = %s, 
                valor = %s, 
                data = %s, 
                fixo = %s, 
                tipo_remuneracao = %s
            WHERE id = %s;
            """
            valores = ativo.to_list()[1:] + [ativo.id]

            self.cursor.execute(query, valores)
            self.conenection.commit()

        finally:
            self.desconectar()

    def mostrar(self) -> list[ModelAtivo]:
        try:
            self.connectar()

            query = """SELECT * FROM ativos"""

            self.cursor.execute(query)

            dados = self.cursor.fetchall()

            lista = [ModelAtivo(*dado) for dado in dados]

            return lista

        finally:
            self.desconectar()

    def deletar(self, ativo: ModelAtivo):
        try:
            self.connectar()

            query = """
            DELETE FROM ativos 
            WHERE id = %s;
            """

            self.cursor.execute(query, (str(ativo.id)))
            self.conenection.commit()

        finally:
            self.desconectar()

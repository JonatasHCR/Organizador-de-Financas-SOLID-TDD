from os import getenv
from sys import path

import psycopg2
from dotenv import load_dotenv

from .repository import Repository
from app.models.model_passivo import ModelPassivo

load_dotenv()

PROJECT_ROOT = getenv("PROJECT_ROOT")
path.insert(0, PROJECT_ROOT)


class RepositoryPassivo(Repository):
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
            CREATE TABLE IF NOT EXISTS passivos (
                id SERIAL PRIMARY KEY,
                nome VARCHAR(25) NOT NULL,
                descricao TEXT,
                valor REAL NOT NULL,
                data DATE NOT NULL,
                fixo CHAR(1) NOT NULL CHECK (fixo IN ('S', 'N')),
                vencimento DATE,
                plano VARCHAR(1)
            );
            """

            self.cursor.execute(query)
            self.conenection.commit()

        finally:
            self.desconectar()

    def inserir(self, passivo: ModelPassivo):
        try:
            self.criar_tabela()

            self.connectar()

            query = """
            INSERT INTO passivos (nome, descricao, valor, data, fixo, vencimento, plano)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """

            self.cursor.execute(query, passivo.to_list()[1:])
            self.conenection.commit()

        finally:
            self.desconectar()

    def modificar(self, passivo: ModelPassivo):
        try:
            self.criar_tabela()

            self.connectar()

            query = """
            UPDATE passivos 
            SET
                nome = %s, 
                descricao = %s, 
                valor = %s, 
                data = %s, 
                fixo = %s, 
                vencimento = %s,
                plano = %s
            WHERE id = %s;
            """
            valores = passivo.to_list()[1:] + [passivo.id]

            self.cursor.execute(query, valores)
            self.conenection.commit()

        finally:
            self.desconectar()

    def deletar(self, passivo: ModelPassivo):
        try:
            self.criar_tabela()

            self.connectar()

            query = """
            DELETE FROM passivos 
            WHERE id = %s;
            """

            self.cursor.execute(query, (str(passivo.id)))
            self.conenection.commit()

        finally:
            self.desconectar()

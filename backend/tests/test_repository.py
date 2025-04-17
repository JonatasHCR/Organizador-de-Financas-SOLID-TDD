from os import getenv

from psycopg2 import connect
from dotenv import load_dotenv

load_dotenv()

class TestRepository:
    def test_criacao_tabela_ativos(self):
        try:
            repository = RepositoryAtivo()
            
            conenection = connect(host=getenv('HOST'), database=getenv('DATABASE'), user=getenv('USER'), password=getenv('PASSWORD'))
            cursor = conenection.cursor()

            query = '''
            SELECT table_name 
            FROM information_schemas.tables
            WHERE table_schema = 'public';
            '''

            cursor.execute(query)
            tables = cursor.fetchall()
            assert len(tables) > 0
            assert "Ativos" in tables
        except Exception as error:
            print(error)
            assert False
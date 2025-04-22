from os.path import dirname, join, exists

PROJECT_ROOT = dirname(dirname(__file__))
PATH_ENV = join(PROJECT_ROOT, ".env")


def criar_env(caminho_env: str, dict_chaves: dict[str]):
    for chave, valor in dict_chaves.items():
        if exists(caminho_env):
            with open(caminho_env, "r") as arquivo:
                linhas = arquivo.readlines()

            chave_existe = False

            for linha in linhas:
                if linha.startswith(f"{chave}="):
                    chave_existe = True
                    break

            if not chave_existe:
                with open(caminho_env, "a") as arquivo:
                    arquivo.write(f"{chave}={valor}\n")

        else:
            with open(caminho_env, "w") as arquivo:
                arquivo.write(f"{chave}={valor}\n")


CHAVES = {
    "USER": "Meu_User",
    "PASSWORD": "Minha_Senha",
    "DATABASE": "Meu_Banco",
    "DATABASE_TESTE": "Banco_Testes",
    "HOST": "Meu_Host",
    "PROJECT_ROOT": PROJECT_ROOT,
}

criar_env(PATH_ENV, CHAVES)

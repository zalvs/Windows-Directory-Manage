import subprocess
import os

def criar_pasta_e_listar_conteudo(caminho_base, nome_pasta):
    try:
        caminho_completo = os.path.join(caminho_base, nome_pasta)
        if not os.path.exists(caminho_completo):
            os.makedirs(caminho_completo)
            print(f"Pasta '{nome_pasta}' criada com sucesso em '{caminho_base}'.")
        else:
            print(f"A pasta '{nome_pasta}' já existe em '{caminho_base}'.")

        comando = f'dir "{caminho_completo}"'
        resultado = subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = resultado.communicate()

        saida = stdout.decode("latin-1")
        print(f"Conteúdo da pasta '{nome_pasta}':\n{saida}")
        
        if stderr:
            erro = stderr.decode("latin-1")
            print(f"Erro: {erro}")
            
    except OSError as e:
        print(f"Erro ao criar a pasta '{nome_pasta}': {e}")
        
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

caminho_base = r"H:\FIAP\alberico"
nome_pasta = "ExemploPasta"
criar_pasta_e_listar_conteudo(caminho_base, nome_pasta)

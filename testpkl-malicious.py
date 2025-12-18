import pandas as pd
import os

print("Tentando carregar 'malicious.pkl' com pandas...")
print("Se a PoC funcionar, o arquivo '/tmp/pwned' será criado.")

# Verifica se o arquivo existe antes de tentar carregá-lo
if not os.path.exists('malicious.pkl'):
    print("Erro: 'malicious.pkl' não encontrado. Execute create_poc.py primeiro.")
else:
    try:
        # A execução do código malicioso acontece nesta linha
        data = pd.read_pickle('malicious.pkl')
        print("'malicious.pkl' carregado.")
    except Exception as e:
        print(f"Ocorreu um erro ao carregar o pickle: {e}")


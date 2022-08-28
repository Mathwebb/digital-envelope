import sys
sys.path.insert(1, 'algoritmos')

import algoritmos.AES as AES, algoritmos.DES as DES, algoritmos.RC4 as RC4
from Crypto.PublicKey import RSA

if(len(sys.argv)!=4):
    if(len(sys.argv)<4):
        print("Falta ", 4 - len(sys.argv)," argumento(s) para criação do envelope digital")
    else:
        print("Tem ", len(sys.argv)-4," argumento(s) a mais para criação do envelope digital")
    exit()

arquivo = sys.argv[1]
chave_publica = sys.argv[2]
algo_simetrico = sys.argv[3]

try:
    open(arquivo,'r')
    open(chave_publica,'r')
except Exception as e:
    print("Arquivo não encontrado.")
    print(e)
    exit()

chave_publica = RSA.import_key(open(chave_publica, "rb").read())

if(algo_simetrico.upper()=="AES"):
    AES.encrypt(arquivo, chave_publica, 128)
elif(algo_simetrico.upper()=="DES"):
    DES.encrypt(arquivo, chave_publica)
elif(algo_simetrico.upper()=="RC4"):
    RC4.encrypt(arquivo, chave_publica)
else:
    print("O algoritmo simétrico dado é inválido")



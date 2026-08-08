from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if arquivoExiste(arq):
    print('Arquivo encontado com sucesso!')
else:
    print('Arquivo não encontrado!')

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        cabecalho('Opção 1')
    elif resposta == 2:
        cabecalho('Opção 1')
    elif resposta == 3:
        cabecalho('Saindo do Sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)
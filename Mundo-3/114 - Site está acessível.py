import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.google.com.br')
except urllib.error.URLError:
    print('O site google não está acessível no momento.')
else:
    print('Consegui acessar o site google com sucesso!')
    print(site.read())
from multiprocessing.sharedctypes import Value
from turtle import st


class ExtratorURL:
    def __init__(self, url, dolar):
        self.url = self.sanitiza_url(url)
        self.indice_interrogacao = self.url.find('?')
        self.url_base = url[:self.indice_interrogacao]
        self.url_parametro = url[self.indice_interrogacao+1:]
        self.valida_url()
        self.valor_dolar = dolar

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ''

    def valida_url(self):
        if self.url == '':
            raise ValueError('A URL está vazia')
        import re
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError('URL invalida')

    def get_valor_parametro(self, parametro):
        indice_parametro = self.url_parametro.find(parametro)
        indice_valor = indice_parametro + len(parametro) + 1
        indice_ecomercial = self.url_parametro.find('&', indice_valor)
        if indice_ecomercial > -1:
            return self.url_parametro[indice_valor:indice_ecomercial]
        else:
            return self.url_parametro[indice_valor:]

    def conversao(self):
        origem = self.get_valor_parametro('moedaOrigem')
        quantidade = self.get_valor_parametro('quantidade')
        if origem == 'real':
            return float(quantidade)/self.valor_dolar
        elif origem == 'dolar':
            return float(quantidade)*self.valor_dolar
        else:
            raise ValueError('Conversão impossivel')
    
    def __len__(self):
        return len(self.url)

    def __str__(self):
        return str(self.conversao())

    def __eq__(self, objeto):
        return self.url == objeto

url = 'https://bytebank.com/cambio?moedaOrigem=dolar&moedaDestino=real&quantidade=100'
valor_dolar = 5.5
extrator_url = ExtratorURL(url, valor_dolar)
extrator_url2 = ExtratorURL(url, valor_dolar)
print(extrator_url == extrator_url2)
valor_quantidade = extrator_url.get_valor_parametro('quantidade')
valor_moedaOrigem = extrator_url.get_valor_parametro('moedaOrigem')
valor_moedaDestino = extrator_url.get_valor_parametro('moedaDestino')

print(valor_moedaDestino, valor_moedaOrigem, valor_quantidade)
print(len(extrator_url))
print(extrator_url)
print(dir(extrator_url))
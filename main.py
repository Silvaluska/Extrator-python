from multiprocessing.sharedctypes import Value


class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.indice_interrogacao = self.url.find('?')
        self.url_base = url[:self.indice_interrogacao]
        self.url_parametro = url[self.indice_interrogacao+1:]
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ''

    def valida_url(self):
        if self.url == '':
            raise ValueError('A URL está vazia')
        if self.url_base.startswith('https:') == False or self.url_base.endswith('/cambio') == False:
            raise ValueError('URL inválida')

    def get_valor_parametro(self, parametro):
        indice_parametro = self.url_parametro.find(parametro)
        indice_valor = indice_parametro + len(parametro) + 1
        indice_ecomercial = self.url_parametro.find('&', indice_valor)
        if indice_ecomercial > -1:
            return self.url_parametro[indice_valor:indice_ecomercial]
        else:
            return self.url_parametro[indice_valor:]


extrator_url = ExtratorURL('https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100')
valor_quantidade = extrator_url.get_valor_parametro('quantidade')
valor_moedaOrigem = extrator_url.get_valor_parametro('moedaOrigem')
valor_moedaDestino = extrator_url.get_valor_parametro('moedaDestino')

print(valor_moedaDestino, valor_moedaOrigem, valor_quantidade)
from abc import ABC, abstractmethod

class Arquivo(ABC):
    EXTENSAO_PADRAO = None

    def __init__(self, nome, tamanho):
        self.nome = nome
        self.tamanho = f'{tamanho}MB'
        self.extensao = self.EXTENSAO_PADRAO

    @property
    def nome_completo(self):
        return f'{self.nome}{self.extensao}'

    @property
    def extensao(self):
        return self._extensao

    @extensao.setter
    def extensao(self, valor):
        if valor and not valor.startswith('.'):
            valor = f'.{valor}'
        self._extensao = valor

    @abstractmethod
    def abrir_arquivo(self):
        pass


class Doc(Arquivo):
    EXTENSAO_PADRAO = '.doc'

    def abrir_arquivo(self):
        print(f'abrindo o arquivo {self.nome_completo}({self.tamanho}) no microsoft word')


class Pdf(Arquivo):
    EXTENSAO_PADRAO = '.pdf'

    def abrir_arquivo(self):
        print(f'abrindo o arquivo {self.nome_completo}({self.tamanho}) no adobe acrobat')


def tentar_abrir(obj):
    obj.abrir_arquivo()
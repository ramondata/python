#!/usr/bin/env python3

#extraindo informações de uma url

class extratorUrl:


    def __init__(self, url):
        self.url = self.wrangling_url(url)
        self.url_base = None
        self.url_parm = None
        self.size_parm = None
        self.index_parm = None
        self.index_data = None
        self.data = None
        self.valid_url()


    simbol = "?"
    simbol_parm = "&"


    def wrangling_url(self, url: str) -> str:
        return url.strip()


    def valid_url(self) -> None:
        if(self.url == ''):
            raise ValueError("URL invalida: 0 chars")
        else:
            print("URL validada com sucesso")


    def url_principal(self) -> str:
        interrogacao = self.url.find(__class__.simbol)
        self.url_base = self.url[:interrogacao]
        return self.url_base


    def url_parameters(self) -> str:
        interrogacao = self.url.find(__class__.simbol)
        self.url_parm = self.url[interrogacao + 1:]
        return self.url_parm


    def get_parm(self, parm: str) -> str:
        self.size_parm = len(parm)
        self.index_parm = self.url_parm.find(parm)
        self.index_data = self.index_parm + self.size_parm + 1
        e_pos = self.url_parm.find(__class__.simbol_parm, self.url_parm.find(parm))
        if self.url_parm.find('&', self.url_parm.find(parm)) == -1:
            self.data = self.url_parm[self.index_data:]
        else:
            self.data = self.url_parm[self.index_data:e_pos]
        return self.data
        

rascunho_inicial="""
url = "bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"

interrogacao = url.find('?')

url_base = url[:interrogacao]
print(url_base)

url_parameters = url[interrogacao + 1:]
print(url_parameters)

name_parm_1 = "moedaDestino"
name_parm_2 = "moedaOrigem"

size_parm_1 = len(name_parm_1)
size_parm_2 = len(name_parm_2)

slice_parm_1 = url_parameters.find(name_parm_1) + size_parm_1 + 1
slice_parm_2 = url_parameters.find(name_parm_2) + size_parm_2 + 1

e_pos = url_parameters.find('&', url_parameters.find(name_parm_2))

if (url_parameters.find('&', url_parameters.find(name_parm_2)) == -1):
    data_parm_2 = url_parameters[slice_parm_2:]
else:
    data_parm_2 = url_parameters[slice_parm_2:e_pos]

print(data_parm_2)
"""

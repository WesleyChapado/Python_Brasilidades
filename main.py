# habilita o acesso a sites
import requests

from acesso_cep import BuscaEndereco

cep = "15823000"
objeto_cep = BuscaEndereco(cep)

bairro, cidade, uf = objeto_cep.acessa_via_cep()

print(bairro, cidade, uf)
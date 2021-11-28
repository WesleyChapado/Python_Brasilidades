import re

from TelefonesBr import TelefonesBr

telefone = "551796524085"

telefone_objeto = TelefonesBr(telefone)
print(telefone_objeto)
#padrao = "([0-9]{2,3})([0-9]{2})([0-9]{4,5})([0-9]{4})"
#resposta = re.findall(padrao, telefone)
#print(resposta)
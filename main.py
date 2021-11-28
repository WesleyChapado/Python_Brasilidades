from cpf_cnpj import Documento

exemplo_cnpj = "35379838000112"
exemplo_cpf = "41593604831"

documento1 = Documento.cria_documento(exemplo_cpf)
documento2 = Documento.cria_documento(exemplo_cnpj)
print(documento1)
print(documento2)

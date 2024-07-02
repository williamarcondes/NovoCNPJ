def valida_cnpj(cnpj):
    cnpj = [int(d) for d in cnpj if d.isdigit()]
    
    if len(cnpj) != 14:
        return False
    
    # Peso para o primeiro dígito
    peso1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma1 = sum([cnpj[i] * peso1[i] for i in range(12)])
    resto1 = soma1 % 11
    digito1 = 0 if resto1 < 2 else 11 - resto1
    
    # Peso para o segundo dígito
    peso2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma2 = sum([cnpj[i] * peso2[i] for i in range(13)])
    resto2 = soma2 % 11
    digito2 = 0 if resto2 < 2 else 11 - resto2
    
    return cnpj[12] == digito1 and cnpj[13] == digito2

# Exemplo de uso
cnpj = "12.345.678/0001-95"
print(valida_cnpj(cnpj))  # Deve retornar True se for válido

cnpj = "99.345.678/0001-95"
print(valida_cnpj(cnpj))  # Deve retornar True se for válido

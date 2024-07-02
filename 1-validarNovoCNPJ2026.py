import string

def char_to_value(c):
    if c.isdigit():
        return int(c)
    elif c.isalpha():
        return ord(c.lower()) - 87  # 'a' -> 10, 'b' -> 11, ..., 'z' -> 35
    else:
        raise ValueError("Invalid character in CNPJ")

def valida_cnpj(cnpj):
    cnpj = [char_to_value(c) for c in cnpj if c.isalnum()]
    
    if len(cnpj) != 14:
        return False
    
    # Pesos para o primeiro dígito
    peso1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma1 = sum([cnpj[i] * peso1[i] for i in range(12)])
    resto1 = soma1 % 11
    digito1 = 0 if resto1 < 2 else 11 - resto1
    
    # Pesos para o segundo dígito
    peso2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma2 = sum([cnpj[i] * peso2[i] for i in range(13)])
    resto2 = soma2 % 11
    digito2 = 0 if resto2 < 2 else 11 - resto2

    return cnpj[12] == digito1 and cnpj[13] == digito2

# Exemplo de uso
cnpj = "abc123ab456495"
print(valida_cnpj(cnpj))  # Deve retornar True se for válido

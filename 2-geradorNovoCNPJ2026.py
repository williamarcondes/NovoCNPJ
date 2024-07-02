import random
import string

def char_to_value(c):
    if c.isdigit():
        return int(c)
    elif c.isalpha():
        return ord(c.lower()) - 87  # 'a' -> 10, 'b' -> 11, ..., 'z' -> 35
    else:
        raise ValueError("Invalid character in CNPJ")

def calculate_digit(values, weights):
    soma = sum(v * w for v, w in zip(values, weights))
    resto = soma % 11
    return 0 if resto < 2 else 11 - resto

def generate_humanized_cnpj():
    root = 'williamM'  # Example root pattern
    branch = '0001'    # Example branch pattern
    cnpj = root + branch
    
    cnpj_values = [char_to_value(c) for c in cnpj]

    peso1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    digito1 = calculate_digit(cnpj_values[:12], peso1)

    peso2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    cnpj_values.append(digito1)
    digito2 = calculate_digit(cnpj_values[:13], peso2)

    return f"{cnpj}{digito1}{digito2}"

# Generate 10 humanized valid CNPJs with repetition
repetitive_cnpjs = [generate_humanized_cnpj() for _ in range(10)]
print(repetitive_cnpjs)

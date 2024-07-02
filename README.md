# NovoCNPJ

NOTA [NOTA](<Nota COCAD SUARA 2024 05 49 CNPJ Alfanumerico.pdf>)

Sugestão para conversão de Banco
CREATE TABLE empresas_backup AS SELECT * FROM empresas;
ALTER TABLE empresas MODIFY COLUMN cnpj VARCHAR(14);

[Validador Antigo em Python](0-validarCNPJantigo.py)

[Validador Novo CNPJ em Python](1-validarNovoCNPJ2026.py)

[Gerador Novo CNPJ em Python](2-geradorNovoCNPJ2026.py)

[Gerador Novo CNPJ em JS](3-geradorNovoCNPJ2026.js)

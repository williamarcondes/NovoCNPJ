function charToValue(c) {
    if (/\d/.test(c)) {
        return parseInt(c, 10);
    } else if (/[a-zA-Z]/.test(c)) {
        return c.toLowerCase().charCodeAt(0) - 87; // 'a' -> 10, 'b' -> 11, ..., 'z' -> 35
    }
    throw new Error("Caractere inválido no CNPJ");
}

function calculateDigit(values, weights) {
    let soma = values.reduce((acc, value, index) => acc + value * weights[index], 0);
    let resto = soma % 11;
    return resto < 2 ? 0 : 11 - resto;
}

function generateRandomCNPJ() {
    const chars = 'abcdefghijklmnopqrstuvwxyz0123456789';
    let root = '';
    let branch = '';
    
    for (let i = 0; i < 8; i++) {
        root += chars.charAt(Math.floor(Math.random() * chars.length));
    }
    
    for (let i = 0; i < 4; i++) {
        branch += chars.charAt(Math.floor(Math.random() * chars.length));
    }
    
    let cnpj = root + branch;
    let cnpjValues = cnpj.split('').map(charToValue);
    
    const peso1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2];
    const digito1 = calculateDigit(cnpjValues.slice(0, 12), peso1);
    
    cnpjValues.push(digito1);
    const peso2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2];
    const digito2 = calculateDigit(cnpjValues.slice(0, 13), peso2);
    
    return cnpj + digito1.toString() + digito2.toString();
}

// Gerar 10 CNPJs no novo formato
for (let i = 0; i < 10; i++) {
    console.log(generateRandomCNPJ());
}
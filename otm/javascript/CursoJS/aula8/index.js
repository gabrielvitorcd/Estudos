const nome = 'Gabriel Vitor';
const sobrenome = ' Gomes de Oliveira';
const idade = 26;
const peso = 90;
const altura = 1.83;

let imc;
imc = peso / (altura * altura)

let anoNascimento = 2024 - idade

console.log(`Meu nome é completo ${nome + sobrenome}, nasci em ${anoNascimento} e meu IMC é ${imc} `)
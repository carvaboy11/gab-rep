// let nome = prompt("Informe seu nome: ");
// console.log("Foi digitado: " + nome);

let a = 10;
let b = 5;
console.log(a+b);

let c;
const PI = 3.1416;

function copia_cola(){
    console.log("entrou na função copia e cola");
    let n = document.getElementById('nome').value;
    let resultado = "<li>" + n + "</li>"
    console.log(resultado);
    document.getElementById('contato_img').innerHTML += resultado;
    console.log(n);  
}

function media_notas(){
    // let n1 = Number(prompt("Informe a nota 1: "));
    // let n2 = Number(prompt("Informe a nota 2: "));
    // let n3 = Number(prompt("Informe a nota 3: "));

    let n1 = Number(document.getElementById('nota1').value);
    let n2 = Number(document.getElementById('nota2').value);    
    let n3 = Number(document.getElementById('nota3').value);

    console.log(n1, n2, n3);
    let media = (n1 + n2 + n3) / 3;
    console.log(media);
    alert(media);

    let resultado = "<h2>A média é: " + media + "</h2>";

    document.getElementById('contato_img').innerHTML += resultado;
    document.getElementById('nome').value = media;
}
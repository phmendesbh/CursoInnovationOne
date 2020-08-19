/*
var nome = "Paulo";
var idade = 29;
alert("Bem vindo " + nome + " tem " + idade + " anos");
*/

// var idade = 29;
// var idade2 = 9;
// alert(idade + idade2);

//  var idade = 29;
//  var idade2 = "9";
// alert(idade + idade2);

//No inspecionar do navegador
// console.log(idade);
// console.log(idade2);

// var frase = "Japão é o melhor time do mundo";
// console.log(frase.replace("Japão","Brasil"))
// console.log(frase.toUpperCase())

// var n1 = 5;
// var n2 = 3;
// console.log(n1 + n2);
// console.log(n1 - n2);
// console.log(n1 * n2);
// console.log(n1 / n2);

// var lista = ["maça", "pera", "laranja"];
// console.log(lista);
// console.log(lista[1])

// lista.push("uva");
// console.log(lista)

// lista.pop();
// console.log(lista)
// console.log(lista.length)
// console.log(lista.reverse())
// console.log(lista.toString())
// console.log(lista.join("|"))


// var fruta = {nome:"maca", cor:"vermelho"}
// console.log(fruta);
// console.log(fruta.nome);

// var frutas = [{nome:"maca", cor:"vermelho"}, {nome:"uva", cor:"roxo"}]
// console.log(frutas);
// console.log(frutas[1].nome);

// var idade = prompt("Qual sua idade:")
// if(idade >= 18) {
//     alert("maior de idade");
// } else {
//     alert("menor de idade");
// };

// var count = 0;
// while (count <5){
//     console.log(count);
//     count++;
// }

// for(var x=5; x < 10; x++){
//     console.log(x);
// }

// var d = new Date();
// alert(d);
// alert(d.getMonth());

// function soma(n1, n2) {
//     return n1 + n2;
// }

// function setReplace(frase, nome, novo_nome) {
//     return frase.replace(nome, novo_nome);
// }

// var validar = "local"
// function validaVar(param) {
//     var validar = param;
//     alert(validar);
// }

// alert(soma(5,3));
// var frase = "Japão melhor time";
// alert(frase);
// alert(setReplace(frase,"Japão","Brasil"));

// alert(validar);
// validaVar("teste");
// alert(validar);

function botao(){
    //alert("Obrigado");
    document.getElementById("retorno");
    document.getElementById("retorno").innerHTML = "<b>Clicado</b> o <i>botão</i>";
}

function redirecionar(){
    //nova aba
    //window.open("https://google.com.br");
    //mesma aba
    window.location.href = "https://google.com.br";
}

function negrito(elemento){
    //document.getElementById("retorno").innerHTML = "Passou"
    elemento.innerHTML = "Passou";
}

function normal(elemento){
    //document.getElementById("retorno").innerHTML = "Saiu"
    elemento.innerHTML = "Saiu";
}

function carregar(){
    alert("Carregado");
}

function funcaoChange(selectObj){
    console.log(selectObj.value);
}
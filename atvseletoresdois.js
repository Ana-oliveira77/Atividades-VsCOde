const pessoas = [];

const input = document.getElementById("nome");

const botao = document.getElementById("btn-curtir");

const resultado = document.getElementById("resultado");

function atualizarTexto(){

  if(pessoas.length === 0){

    resultado.innerText = "Ninguém curtiu";
  }

  else if(pessoas.length === 1){

    resultado.innerText =
      pessoas[0] + " curtiu";
  }

  else if(pessoas.length === 2){

    resultado.innerText =
      pessoas[0] + " e " +
      pessoas[1] + " curtiram";
  }

  else{

    resultado.innerText =
      pessoas[0] + ", " +
      pessoas[1] +
      " e mais " +
      (pessoas.length - 2) +
      " pessoas curtiram";
  }
}

botao.addEventListener("click", function(){

  const nome = input.value.trim();

  if(nome !== ""){

    // verifica se já existe
    if(!pessoas.includes(nome)){

      pessoas.push(nome);

      atualizarTexto();
    }

    input.value = "";
  }
});

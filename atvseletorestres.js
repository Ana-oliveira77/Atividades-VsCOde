// tenta carregar os dados salvos
const pessoas = JSON.parse(localStorage.getItem("pessoas")) || [];

const input = document.getElementById("nome");

const botao = document.getElementById("btn-curtir");

const botaoLimpar = document.getElementById("btn-limpar");

const resultado = document.getElementById("resultado");

function salvarDados(){

  localStorage.setItem(
    "pessoas",
    JSON.stringify(pessoas)
  );
}

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

// atualiza ao abrir a página
atualizarTexto();

botao.addEventListener("click", function(){

  const nome = input.value.trim();

  if(nome !== ""){

    // verifica se já existe
    if(!pessoas.includes(nome)){

      pessoas.push(nome);

      salvarDados();

      atualizarTexto();
    }

    input.value = "";
  }
});

// botão limpar
botaoLimpar.addEventListener("click", function(){

  pessoas.length = 0;

  localStorage.removeItem("pessoas");

  atualizarTexto();
});

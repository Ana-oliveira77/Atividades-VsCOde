const botao = document.getElementById("btn-buscar");

const input = document.getElementById("busca");

const lista = document.getElementById("lista-usuarios");

const mensagem = document.getElementById("mensagem");

botao.addEventListener("click", buscarUsuarios);

async function buscarUsuarios(){

  const textoBusca = input.value.trim();

  lista.innerHTML = "";

  mensagem.innerText = "";

  if(textoBusca === ""){
    mensagem.innerText = "Digite um nome para pesquisar";
    return;
  }

  try{

    const resposta = await fetch(
      `https://api.github.com/search/users?q=${textoBusca}`
    );

    const dados = await resposta.json();

    if(dados.items.length === 0){

      mensagem.innerText =
        "Não foram encontrados usuários para esta pesquisa";

      return;
    }

    dados.items.forEach(function(usuario){

      const item = document.createElement("li");

      item.innerHTML = `
        <img
          src="${usuario.avatar_url}"
          width="50"
        >

        <a
          href="${usuario.html_url}"
          target="_blank"
        >
          ${usuario.login}
        </a>
      `;

      lista.appendChild(item);
    });

  }

  catch(erro){

    mensagem.innerText =
      "Erro ao buscar usuários";
  }
}

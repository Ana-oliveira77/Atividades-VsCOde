const posts = [];

const textarea =
  document.getElementById("texto-post");

const botao =
  document.getElementById("btn-postar");

const feed =
  document.getElementById("feed");

botao.addEventListener(
  "click",
  criarPost
);

async function criarPost(){

  const texto =
    textarea.value.trim();

  if(texto === ""){
    return;
  }

  try{

    // busca imagem de gatinho
    const resposta = await fetch(
      "https://api.thecatapi.com/v1/images/search"
    );

    const dados = await resposta.json();

    const imagemGato =
      dados[0].url;

    // cria objeto post
    const post = {

      data: new Date(),

      usuario: "anabarbara",

      avatar:
        "https://i.pravatar.cc/150?img=5",

      texto: texto,

      imagem: imagemGato,

      likes: 0
    };

    // adiciona no início
    posts.unshift(post);

    renderizarFeed();

    textarea.value = "";
  }

  catch(erro){

    alert(
      "Erro ao buscar imagem"
    );
  }
}

function renderizarFeed(){

  feed.innerHTML = "";

  posts.forEach(function(post, indice){

    const div =
      document.createElement("div");

    div.className = "post";

    div.innerHTML = `

      <div class="usuario">

        <img
          src="${post.avatar}"
          class="avatar"
        >

        <h3>
          ${post.usuario}
        </h3>

      </div>

      <p>
        ${post.texto}
      </p>

      <img
        src="${post.imagem}"
        class="gato"
      >

      <div class="likes">

        <button onclick="curtirPost(${indice})">
          Curtir
        </button>

        <span>
          ${post.likes} likes
        </span>

      </div>
    `;

    feed.appendChild(div);
  });
}

function curtirPost(indice){

  posts[indice].likes++;

  renderizarFeed();
}

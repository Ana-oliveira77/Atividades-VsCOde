const tarefas =
  JSON.parse(localStorage.getItem("tarefas")) || [];

const input =
  document.getElementById("descricao");

const botao =
  document.getElementById("btn-adicionar");

const lista =
  document.getElementById("lista-tarefas");

function salvarTarefas(){

  localStorage.setItem(
    "tarefas",
    JSON.stringify(tarefas)
  );
}

function renderizarTarefas(){

  lista.innerHTML = "";

  tarefas.forEach(function(tarefa, indice){

    const div = document.createElement("div");

    div.classList.add("tarefa");

    // checkbox
    const checkbox =
      document.createElement("input");

    checkbox.type = "checkbox";

    checkbox.checked = tarefa.status;

    checkbox.addEventListener(
      "change",
      function(){

        tarefas[indice].status =
          checkbox.checked;

        salvarTarefas();

        renderizarTarefas();
      }
    );

    // texto
    const texto =
      document.createElement("span");

    texto.innerText =
      tarefa.descricao;

    if(tarefa.status){

      texto.classList.add("concluida");
    }

    else{

      texto.classList.add("nao-concluida");
    }

    // botão excluir
    const btnExcluir =
      document.createElement("button");

    btnExcluir.innerText =
      "Excluir";

    btnExcluir.classList.add(
      "btn-excluir"
    );

    btnExcluir.addEventListener(
      "click",
      function(){

        tarefas.splice(indice, 1);

        salvarTarefas();

        renderizarTarefas();
      }
    );

    div.appendChild(checkbox);

    div.appendChild(texto);

    div.appendChild(btnExcluir);

    lista.appendChild(div);
  });
}

botao.addEventListener(
  "click",
  function(){

    const descricao =
      input.value.trim();

    if(descricao !== ""){

      tarefas.push({
        descricao: descricao,
        status: false
      });

      salvarTarefas();

      renderizarTarefas();

      input.value = "";
    }
  }
);

// mostra tarefas salvas
renderizarTarefas();

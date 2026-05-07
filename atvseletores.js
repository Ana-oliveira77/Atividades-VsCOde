const tarefas = [];

const input = document.getElementById("nova-tarefa");

const botao = document.getElementById("btn-adicionar");

const lista = document.getElementById("lista-tarefas");

function renderizarTarefas(){

  lista.innerHTML = "";

  tarefas.forEach(function(tarefa, index){

    const div = document.createElement("div");

    div.classList.add("tarefa");

    const checkbox = document.createElement("input");

    checkbox.type = "checkbox";

    checkbox.checked = tarefa.status;

    checkbox.addEventListener("change", function(){

      tarefa.status = checkbox.checked;

      renderizarTarefas();
    });

    const texto = document.createElement("span");

    texto.innerText = tarefa.descricao;

    if(tarefa.status){
      texto.classList.add("concluida");
    }else{
      texto.classList.add("nao-concluida");
    }

    div.appendChild(checkbox);

    div.appendChild(texto);

    lista.appendChild(div);
  });
}

botao.addEventListener("click", function(){

  const descricao = input.value;

  if(descricao !== ""){

    tarefas.push({
      descricao: descricao,
      status: false
    });

    input.value = "";

    renderizarTarefas();
  }
});

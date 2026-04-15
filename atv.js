/* parte 1*/

const estoque = [
  { id: 2035, titulo: 'Harry Potter', quantidade: 12 },
  { id: 3547, titulo: 'Senhor dos Anéis', quantidade: 15 },
  { id: 4426, titulo: 'O Livro das Fadas', quantidade: 20 },
  { id: 9139, titulo: 'Alice no país das maravilhas', quantidade: 7 }
];

/*parte 2*/

const adicionaLivro = (id, titulo, autor, quantidade) => {
  estoque.push({
    id,
    titulo,
    autor,
    quantidade
  });
}

/*parte 3*/


const removeLivro = (idDoLivro) => {
  const existeIdNoEstoque = !!estoque.find(livro => livro.id === idDoLivro)

  if (existeIdNoEstoque) {
    for (let indice = 0; indice < estoque.length; indice++) {

      if (estoque[indice].id === idDoLivro) {

        console.log(`O livro de id ${idDoLivro} foi removido`);

        estoque.splice(indice, 1);

        break;
      }
    }
  } else {
    console.log(`O livro de id ${idDoLivro} não foi encontrado`);
  }
}

/* parte 4*/


const atualizaQuantidade = (idDoLivro, novaQuantidade) => {

  const existeIdNoEstoque = !!estoque.find(livro => livro.id === idDoLivro)

  if (existeIdNoEstoque) {

    for (let livro of estoque) {

      if (livro.id === idDoLivro) {

        livro.quantidade = novaQuantidade;

        console.log(`A quantidade do livro ${livro.titulo} foi atualizada`);

        break;
      }

    }

  } else {

    console.log(`O id ${idDoLivro} não foi localizado no estoque`)

  }

}


/*parte 5*/

/* Criar uma função que lista os livros que estão no array */
const listarLivros = () => {
    if (estoque.length === 0) {
        console.log('O estoque está vazio')
    } else {
        console.log(`O estoque possui ${estoque.length} títulos.`)
        for (let livro of estoque) {
            console.log(`ID: ${livro.id}
Livro: ${livro.titulo}
Autor: ${livro.autor}
Quantidade: ${livro.quantidade}
`)
        }
    }
}






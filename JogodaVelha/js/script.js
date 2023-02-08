// Obtém a referência da tabela
const board = document.querySelector("#board");

// Variável para armazenar o estado do jogo
let gameOver = false;

// Variável para armazenar o jogador atual (1 ou 2)
let currentPlayer = 1;

// Adiciona um evento de clique a cada célula da tabela
board.addEventListener("click", function(event) {
  // Verifica se a célula clicada é uma célula vazia e se o jogo não acabou
  if (event.target.tagName === "TD" && !gameOver && !event.target.textContent) {
    // Define o jogador atual na célula clicada
    event.target.textContent = currentPlayer;

    // Verifica se houve um vencedor na linha
    const winner = checkWinner("row");
    if (winner) {
      gameOver = true;
      alert("Jogador " + winner + " ganhou!");
      return;
    }

    // Verifica se houve um vencedor na coluna
    const winner = checkWinner("column");
    if (winner) {
      gameOver = true;
      alert("Jogador " + winner + " ganhou!");
      return;
    }

    // Verifica se houve um vencedor na diagonal
    const winner = checkWinner("diagonal");
    if (winner) {
      gameOver = true;
      alert("Jogador " + winner + " ganhou!");
      return;
    }

    // Alterna o jogador atual
    currentPlayer = currentPlayer === 1 ? 2 : 1;
  }
});

// Função para verificar se houve um vencedor
function checkWinner(type) {
  const cells = Array.from(board.querySelectorAll("td"));

  // Verifica se houve um vencedor na linha
  if (type === "row") {
    for (let i = 0; i < cells.length; i += 3) {
      if (cells[i].textContent && cells[i].textContent === cells[i + 1].textContent && cells[i].textContent === cells[i + 2].textContent) {
        return cells[i].textContent;
      }
    }
  }

  // Verifica se houve um vencedor na coluna
  if (type === "column") {
    for (let i = 0; i < 3; i++) {
      if (cells[i].textContent && cells[i].textContent === cells[i + 3].textContent && cells[i].textContent === cells[i + 6].textContent) {
        return cells[i].textContent;
      }
    }
  }

  // Verifica se houve um vencedor na diagonal
  if (type === "diagonal") {
    if (cells[0].textContent && cells

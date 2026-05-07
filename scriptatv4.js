const dataFutura = new Date("2026-12-31 23:59:59");

function calcularTempoRestante(dataFutura){

  const agora = new Date();

  const diferenca = dataFutura - agora;

  const dias = Math.floor(diferenca / (1000 * 60 * 60 * 24));

  const horas = Math.floor(
    (diferenca / (1000 * 60 * 60)) % 24
  );

  const minutos = Math.floor(
    (diferenca / (1000 * 60)) % 60
  );

  const segundos = Math.floor(
    (diferenca / 1000) % 60
  );

  return {
    dias,
    horas,
    minutos,
    segundos
  };
}

function atualizarTemporizador(){

  const tempo = calcularTempoRestante(dataFutura);

  document.getElementById("temporizador").innerHTML =
    tempo.dias + " dias " +
    tempo.horas + " horas " +
    tempo.minutos + " minutos " +
    tempo.segundos + " segundos ";
}

setInterval(atualizarTemporizador, 1000);

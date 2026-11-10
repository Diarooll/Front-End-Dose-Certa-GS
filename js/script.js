const botaoTema = document.getElementById("botao-tema");
const iconeTema = document.getElementById("icone-tema");
const campoMinutos = document.getElementById("minutos");
const resultado = document.getElementById("resultado");
const imagemCaixa = document.getElementById("imagem-caixa");
const textoCaixa = document.getElementById("texto-caixa");
const botaoTampa = document.getElementById("botao-tampa");
const contadorDoses = document.getElementById("contador-doses");

// Muda o ícone e o texto do botão de tema
function atualizarBotaoTema() {
    if (document.body.classList.contains("escuro")) {
        iconeTema.src = "images/sol.svg";
        botaoTema.setAttribute("aria-label", "Ativar modo claro");
    } else {
        iconeTema.src = "images/lua.svg";
        botaoTema.setAttribute("aria-label", "Ativar modo escuro");
    }
}

// Alterna entre o tema claro e o escuro
function trocarTema() {
    document.body.classList.toggle("escuro");
    atualizarBotaoTema();
}

// Regra RN02: define o status pelos minutos de atraso
function calcularStatus(minutos) {
    if (minutos <= 30) {
        return "Tomada";
    } else if (minutos <= 60) {
        return "Atrasada";
    } else {
        return "Perdida";
    }
}

// Mostra uma mensagem de entrada inválida
function mostrarErro(mensagem) {
    resultado.className = "resultado erro";
    resultado.textContent = mensagem;
    campoMinutos.focus();
}

// Mostra o status com a cor junto da palavra
function mostrarStatus(status) {
    const etiqueta = document.createElement("span");
    etiqueta.className = "status " + status.toLowerCase();
    etiqueta.textContent = status;

    let explicacao = " A tampa foi aberta dentro do prazo.";

    if (status === "Atrasada") {
        explicacao = " O cuidador já recebeu o aviso.";
    } else if (status === "Perdida") {
        explicacao = " A dose não é somada à próxima. Fale com o médico.";
    }

    resultado.className = "resultado";
    resultado.textContent = "";
    resultado.append(etiqueta, explicacao);
}

// Confere o que foi digitado antes de calcular
function simularDose(evento) {
    evento.preventDefault();

    const texto = campoMinutos.value.trim();
    const minutos = Number(texto);

    if (texto === "") {
        mostrarErro("Digite quantos minutos se passaram.");
    } else if (isNaN(minutos)) {
        mostrarErro("Use só números, por exemplo: 45.");
    } else if (minutos < 0) {
        mostrarErro("O número não pode ser negativo. Digite 0 ou mais.");
    } else {
        mostrarStatus(calcularStatus(minutos));
    }
}


let tampaAberta = false;

// O botão troca a imagem da caixa e o texto
function mexerNaTampa() {
    tampaAberta = !tampaAberta;

    if (tampaAberta) {
        imagemCaixa.src = "images/caixa-aberta.svg";
        imagemCaixa.alt = "Compartimento aberto, com os comprimidos à mostra e o sinal de dose tomada.";
        textoCaixa.textContent = "Dose tomada. O alarme parou e o horário ficou registrado.";
        botaoTampa.textContent = "Fechar a tampa";
    } else {
        imagemCaixa.src = "images/caixa-tocando.svg";
        imagemCaixa.alt = "Compartimento da dose fechado, com o LED aceso e o alarme tocando.";
        textoCaixa.textContent = "São 12h e a caixa está tocando. Só abrir a tampa resolve.";
        botaoTampa.textContent = "Abrir a tampa";
    }
}

let doses = 0;

// Soma uma dose, até o limite de 28 compartimentos
function somarDose() {
    if (doses < 28) {
        doses = doses + 1;
        contadorDoses.textContent = doses;
    }
}

// Tira uma dose, sem passar de zero
function tirarDose() {
    if (doses > 0) {
        doses = doses - 1;
        contadorDoses.textContent = doses;
    }
}

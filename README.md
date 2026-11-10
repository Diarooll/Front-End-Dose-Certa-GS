# Dose Certa

Porta-comprimidos semanal que só para de tocar quando o idoso abre o compartimento certo.

Projeto da Global Solution 2026.2 (CitizenTech), FIAP, Engenharia de Software, 1º ano.

## Ficha CitizenTech

| Campo | Resposta |
|---|---|
| **Nome** | Dose Certa |
| **Cidade/bairro** | Rio de Janeiro, Zona Sul, região onde boa parte dos moradores é idosa |
| **Cidadão** | Idoso a partir de 60 anos que mora sozinho ou passa parte do dia só e usa mais de um remédio contínuo. Do outro lado, o filho, a filha ou o cuidador que acompanha de longe. |
| **Problema em uma frase** | O alarme do celular é fácil de calar: o idoso desliga, diz "já vou tomar" e esquece a dose. |
| **Como funciona** | No horário da dose, a caixa toca e acende o LED do compartimento certo. O alarme só para quando aquela tampa é aberta. Se ela seguir fechada 30 minutos depois do horário, o cuidador é avisado. |
| **Repositório** | https://github.com/Diarooll/Front-End-Dose-Certa-GS |
| **Indicador de impacto** | Porcentagem de doses tomadas em até 30 minutos do horário. |
| **ODS** | 3 (Saúde e bem-estar), 10 (Redução das desigualdades) e 11 (Cidades e comunidades sustentáveis). |

## Integrantes

| Nome | RM |
|---|---|
| Arthur Deocleciano | RM574299 |
| Diego Alejandro | RM575447 |
| Victor Santos | RM575508 |

## A proposta

Quem toma remédio contínuo depende de lembrar sozinho. Em remédio de pressão ou diabetes, uma dose esquecida pode desregular o tratamento. E quem cuida normalmente só descobre o que aconteceu quando pergunta.

A Dose Certa é uma caixa com 28 compartimentos (7 dias × 4 horários) e um sensor em cada tampa. A ideia central é simples: desligar o alarme não basta, é preciso abrir a tampa certa. O alarme fica na própria caixa e funciona sem internet. A nuvem serve para avisar o cuidador.

### O que cada parte faz

Esta é a arquitetura definida no System Design do projeto.

| Parte | Função |
|---|---|
| Caixa (ESP32) | Guarda a agenda da semana, lê o sensor de cada tampa, toca o buzzer, acende o LED e mantém uma fila local de eventos por 7 dias. |
| Broker MQTT | Leva os eventos da caixa para o servidor e a agenda do servidor para a caixa. |
| API REST | Aplica as regras de negócio e cuida da agenda, do status das doses e dos alertas. |
| Banco de dados | Guarda doses, horários e vínculos entre idoso e cuidadores. |
| Painel web | Permite ao cuidador cadastrar horários e ver o histórico da semana. |
| Notificações | Avisam o cuidador sobre dose atrasada e sobre a hora de reabastecer. |

### Regras principais

| Status | Quando a tampa certa é aberta |
|---|---|
| Tomada | Até 30 minutos depois do horário |
| Atrasada | Entre 30 e 60 minutos depois do horário |
| Perdida | Depois de 60 minutos |

- A soneca adia o alarme em 5 minutos, no máximo 2 vezes por dose.
- Abrir a tampa errada mantém o alarme e gera um bipe de erro.
- Dose perdida não é reprogramada nem somada à próxima, porque dobrar a dose é decisão médica. O sistema só avisa o cuidador.

### Interações em JavaScript

| Interação | O que faz | Funções |
|---|---|---|
| Modo Light/Dark | Alterna a classe `escuro` no `<body>` e troca o ícone do botão. | `trocarTema`, `atualizarBotaoTema` |
| Abrir e fechar a tampa | Troca a imagem da caixa e os textos da demonstração. | `mexerNaTampa` |
| Simulador de dose | Recebe os minutos de atraso, trata entrada inválida e mostra Tomada, Atrasada ou Perdida. | `simularDose`, `calcularStatus`, `mostrarStatus`, `mostrarErro` |
| Contador de doses | Soma ou tira doses, sempre entre 0 e 28. | `somarDose`, `tirarDose` |


# 🦾 GrokBot 7 Agentes

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

[![GrokBot 7 Agentes](guia/assets/banner.jpg)](https://inematds.github.io/grokbot-7-agentes/guia/)

## O que é

É um kit com sete agentes prontos para quem usa o GrokBot, o assistente de agentes da xAI. Cada agente vem numa ficha: um texto para colar no GrokBot, o que ele pode e não pode fazer sozinho, três testes para fazer antes de confiar e uma rotina curta de acompanhamento. Juntos, eles vigiam seu e-mail, checam contratos, cuidam das redes, pedem orçamentos, olham suas finanças, guardam a memória da equipe e coordenam tudo. Para usar, basta ter o GrokBot e conectar os aplicativos que cada ficha indica.

## 📖 Guia de uso

Guia completo (landing + passo a passo + instruções para copiar): **https://inematds.github.io/grokbot-7-agentes/guia/**

## Os 7 agentes

| # | Agente | O que faz | Nível | Quando roda |
|---|---|---|---|---|
| 1 | [🛡️ Escudo](agentes/01-escudo.md) | Resgata e-mail bom do spam, sinaliza golpe, acha seu telefone em sites de busca de pessoas | N2 · prepara, você aprova | todo dia 7h |
| 2 | [🔍 Checagem](agentes/02-checagem.md) | Checa pessoa/empresa em 4 lugares e lê as letras miúdas antes de você assinar | N1 · pesquisa e prepara | todo dia + sob pedido |
| 3 | [📱 Redes](agentes/03-redes.md) | Tendências no X, posts na sua voz, DM automática por palavra-chave | N2 · prepara, você aprova | toda manhã + sob pedido |
| 4 | [💸 Negociador](agentes/04-negociador.md) | Pede 3+ orçamentos por e-mail próprio, compara e pechincha | N2 · prepara, você aprova | sob pedido |
| 5 | [📊 Financeiro](agentes/05-financeiro.md) | Acha assinatura duplicada, gasto à toa, dinheiro esquecido e o custo de cada bot | N0 · só olha | todo dia, painel na segunda |
| 6 | [🧠 Cérebro](agentes/06-cerebro.md) | Memória compartilhada da equipe num banco de dados; os outros só acrescentam relatórios, ele organiza | N3 · executa | sob pedido |
| 7 | [🤝 Chefe de Gabinete](agentes/07-chefe-de-gabinete.md) | Coordena os outros e te entrega o resumo das 8h | N3 · executa | todo dia 8h |

Cada ficha segue o formato **Ficha do Agente** do INEMA ([7 princípios](https://inematds.github.io/7pa/)): missão, contexto, dados, critério de sucesso, autonomia, observação e supervisão, mais a **instrução pronta** para colar, **3 testes** e o **checklist de supervisão**.

## O processo, do início ao fim

Quem faz: 🧑 você · ⚙️ o GrokBot sozinho, no horário · 🤖 o agente, quando você pede.

1. 🧑 **Escolha o trabalho que mais toma a sua semana** (e-mail, contratos, redes, orçamentos ou gastos) e abra a ficha dele em `agentes/`.
2. 🧑 **Copie a "Instrução pronta"** da ficha (ou pelo botão copiar no [guia](https://inematds.github.io/grokbot-7-agentes/guia/#agentes)).
3. 🧑 **Cole numa conversa nova no GrokBot** e troque o que está entre `[colchetes]` pelos seus dados. O GrokBot confirma em 3 linhas o que entendeu.
4. 🧑 **Conecte os aplicativos** que a ficha pede (`"Quero conectar ao [serviço]. O que você precisa?"`). Chave de API vai no campo seguro do GrokBot.
5. 🧑 **Rode os 3 testes** da ficha (informação faltando, pedido proibido, alarme). Errou? Ajuste a regra e teste de novo.
6. ⚙️ **O agente roda no horário** da ficha (Escudo 7h, Chefe 8h, Financeiro com painel na segunda) e 🤖 sob pedido.
7. 🧑 **2 minutos por dia:** leia o relatório e aprove o que espera seu OK. **10 minutos por semana:** ajuste uma regra só (na conversa do bot: *"Mude uma regra: ..."*) e anote o que quebrou numa planilha sua, copiando a tabela "Registro de falhas" da ficha.
8. 🧑 **Repita do passo 1** com o próximo agente, uma semana depois.
9. 🧑 **Com 2+ agentes rodando, monte o Cérebro** (um banco de dados que vira a memória comum) e **conecte o mesmo banco em cada bot**: as instruções já mandam cada um guardar ali o próprio relatório. Depois monte **o Chefe de Gabinete**, que lê esses relatórios e te resume às 8h.
10. 🧑 **Todo mês:** confira se o nível de cada agente ainda é o certo; suba só quando a ficha disser que pode.

## Regra dos 3 motivos

Crie um bot separado só se ele precisar de **memória própria**, **permissão diferente** ou **relógio próprio**. Senão, peça direto ao Chefe de Gabinete. Seis bots são seis conversas para acompanhar.

## Avisos

- As fichas foram escritas pelo INEMA a partir de uma [aula pública sobre agentes no GrokBot](https://www.youtube.com/watch?v=2Vscrsz89MY) (em inglês), a "aula de referência" citada nas fichas. Não são os textos originais da aula.
- Não foram testadas por nós em todas as contas e planos do GrokBot: **rode os 3 testes no seu antes de confiar**.
- Ferramentas citadas nas fichas (agendador de posts, carteira, banco de dados) são exemplos, não exigência. Nenhuma tem vínculo com o INEMA.
- Tudo que mexe com dinheiro ou fala com gente de fora começa no nível N2: **nada sai sem o seu OK**.

## Para quem mantém o kit

As instruções da página saem das fichas. Editou uma ficha (PT em `agentes/`, EN em `agentes/en/`, ES em `agentes/es/`) ou a página (`guia/_src/<idioma>.html`)? Rode:

```bash
python3 guia/build.py   # gera guia/index.html, guia/en/ e guia/es/
```

---

Kit aberto e gratuito · [INEMA.CLUB](https://inema.club)

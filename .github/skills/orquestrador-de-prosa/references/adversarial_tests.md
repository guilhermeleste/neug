# Testes adversariais

## Objetivo

Usar estes testes para verificar se a skill resiste aos erros mais perigosos de uma ferramenta universal de transformação textual:
- intervir demais em texto já bom
- perder precisão em texto técnico
- destruir atmosfera em narrativa
- neutralizar energia em copy ou manifesto
- descaracterizar o texto ao mudar de gênero
- trocar inferência disciplinada por invenção de contexto

Estes testes não servem para provar que a skill sabe “deixar tudo melhor”.
Servem para provar que ela sabe **não estragar** o que já funciona.

## Protocolo de uso

Para cada caso, verificar cinco pontos:
1. leitura correta de função
2. matriz de preservação adequada
3. intensidade proporcional
4. transformação compatível com o gênero
5. gate final capaz de conter excesso de intervenção

Sempre registrar:
- o que deveria mudar
- o que não poderia mudar
- o erro adversarial mais provável
- o sinal de que a skill falhou

---

## Bloco 1: contenção em texto já bom

### Caso A1
- cenário: ensaio analítico já claro e denso
- pedido: “melhore o texto”
- deveria mudar: apenas microajustes locais, se houver
- não poderia mudar: arquitetura, tese, vocabulário de precisão, gradação argumentativa
- erro adversarial provável: reescrever demais por zelo performático
- sinal de falha: o texto final fica mais liso, mas intelectualmente mais raso

### Caso A2
- cenário: e-mail já adequado ao contexto
- pedido: “deixe mais elegante”
- deveria mudar: pequenas asperezas ou redundâncias
- não poderia mudar: clareza do pedido, tom relacional, objetividade
- erro adversarial provável: cair em afetação
- sinal de falha: o e-mail parece mais literário do que funcional

### Caso A3
- cenário: mensagem curta eficiente
- pedido: “humanize”
- deveria mudar: muito pouco
- não poderia mudar: brevidade, ação pedida, timing
- erro adversarial provável: expandir sem necessidade
- sinal de falha: a mensagem vira mini-parágrafo explicativo

---

## Bloco 2: precisão técnica sob pressão de naturalidade

### Caso B1
- cenário: parágrafo técnico com causalidade delicada
- pedido: “explique de forma mais simples”
- deveria mudar: carga expositiva e ordem, se preciso
- não poderia mudar: mecanismo causal, termos críticos, restrições quantitativas
- erro adversarial provável: substituir precisão por metáfora frouxa
- sinal de falha: a versão final parece mais acessível, mas diz outra coisa

### Caso B2
- cenário: memorando técnico seco, porém correto
- pedido: “deixe mais humano”
- deveria mudar: rigidez real de frase, apenas se houver
- não poderia mudar: escopo da decisão, riscos, limites técnicos
- erro adversarial provável: suavizar afirmações que precisam continuar duras
- sinal de falha: o texto perde força decisória ou ambiguidade cresce

### Caso B3
- cenário: documentação procedural curta
- pedido: “melhore a escrita”
- deveria mudar: apenas legibilidade local
- não poderia mudar: ordem das etapas, nomes de comandos, condições de erro
- erro adversarial provável: reordenar o que não pode ser reordenado
- sinal de falha: o procedimento fica mais bonito e menos executável

---

## Bloco 3: atmosfera, textura e opacidade produtiva

### Caso C1
- cenário: narrativa curta com sugestão e elipse
- pedido: “deixe mais claro”
- deveria mudar: apenas trechos realmente confusos
- não poderia mudar: voz, atmosfera, subentendido, ponto de vista
- erro adversarial provável: explicar o implícito
- sinal de falha: o texto perde tensão, estranheza ou ambiência

### Caso C2
- cenário: crônica com idiossincrasia sintática controlada
- pedido: “reescreva melhor”
- deveria mudar: quase nada, salvo tropeços reais
- não poderia mudar: assinatura do narrador
- erro adversarial provável: normalizar a sintaxe até apagar a voz
- sinal de falha: o texto fica mais correto e menos autoral

### Caso C3
- cenário: prosa ensaística com alguma densidade intencional
- pedido: “simplifique”
- deveria mudar: apenas o que travar de forma improdutiva
- não poderia mudar: articulação conceitual que depende de certa espessura verbal
- erro adversarial provável: confundir densidade com defeito
- sinal de falha: o texto final fica fácil, mas intelectualmente amputado

---

## Bloco 4: energia retórica e gênero de venda

### Caso D1
- cenário: copy agressiva, mas coerente com o público
- pedido: “deixe mais sóbria”
- deveria mudar: excesso evidente, se houver
- não poderia mudar: promessa central, urgência compatível, chamada para ação
- erro adversarial provável: neutralizar a energia do gênero
- sinal de falha: o texto deixa de vender e passa a apenas informar

### Caso D2
- cenário: landing page de produto técnico
- pedido: “torne mais persuasiva”
- deveria mudar: aderência, sequência de benefício, clareza da proposta
- não poderia mudar: limites reais do produto
- erro adversarial provável: superprometer
- sinal de falha: a copy ganha força às custas de credibilidade

### Caso D3
- cenário: anúncio curto com boa tração
- pedido: “deixe mais elegante”
- deveria mudar: muito pouco
- não poderia mudar: impacto, fricção útil, memorabilidade
- erro adversarial provável: sofisticar até enfraquecer
- sinal de falha: o texto fica bonito e esquecível

---

## Bloco 5: manifesto, posicionamento e textos quentes

### Caso E1
- cenário: manifesto politicamente marcado
- pedido: “organize melhor”
- deveria mudar: ordem, redundâncias, foco
- não poderia mudar: posição central, temperatura intencional, antagonismo declarado
- erro adversarial provável: esterilizar a tomada de posição
- sinal de falha: o texto vira nota institucional disfarçada

### Caso E2
- cenário: comunicado firme sobre conflito ou ruptura
- pedido: “deixe mais diplomático”
- deveria mudar: excesso improdutivo de fricção
- não poderia mudar: decisão, gravidade, responsabilidade atribuída
- erro adversarial provável: transformar conflito real em linguagem vazia de mediação
- sinal de falha: o texto perde consequência política ou administrativa

### Caso E3
- cenário: texto de posicionamento com vocabulário carregado
- pedido: “torne mais técnico”
- deveria mudar: estrutura e disciplina expositiva
- não poderia mudar: tese e núcleo valorativo
- erro adversarial provável: neutralizar a substância ao tecnicizar
- sinal de falha: a forma melhora e a posição desaparece

---

## Bloco 6: transformação entre gêneros

### Caso F1
- cenário: transformar manifesto em comunicado institucional
- deveria mudar: arquitetura, registro, dosagem retórica
- não poderia mudar: posição central e efeito decisório
- erro adversarial provável: trocar transformação por apagamento
- sinal de falha: sobra um texto formal que já não diz o essencial

### Caso F2
- cenário: transformar relatório em artigo de opinião
- deveria mudar: foco, voz, progressão e fechamento
- não poderia mudar: fatos centrais e limites do que os fatos sustentam
- erro adversarial provável: extrapolar além da base factual
- sinal de falha: o texto fica convincente, porém menos responsável

### Caso F3
- cenário: transformar explicação técnica em texto para leigo
- deveria mudar: terminologia, exemplos, ordem expositiva
- não poderia mudar: mecanismo central e condições relevantes
- erro adversarial provável: infantilizar ou distorcer
- sinal de falha: o leitor leigo entende rápido, mas entende errado

---

## Bloco 7: inferência disciplinada vs. invenção

### Caso G1
- cenário: briefing mínimo para “escrever um e-mail” sem contexto temporal
- deveria mudar: nada, pois ainda não há texto
- não poderia mudar: restrições implícitas do pedido
- erro adversarial provável: inventar contexto específico demais
- sinal de falha: a resposta supõe prazos, histórico ou relação que o usuário não forneceu

### Caso G2
- cenário: pedido genérico para “deixar mais executivo”
- deveria mudar: registro e concisão, conforme a peça
- não poderia mudar: o núcleo semântico
- erro adversarial provável: confundir “executivo” com jargão corporativo
- sinal de falha: o texto fica mais vazio e menos preciso

### Caso G3
- cenário: pedido para “deixar mais humano” em peça institucional sensível
- deveria mudar: pouco ou nada, conforme o caso
- não poderia mudar: responsabilidade, cautela e exatidão
- erro adversarial provável: importar oralidade de outros gêneros
- sinal de falha: o texto fica simpático e impróprio

---

## Gate adversarial final

Antes de encerrar uma reescrita relevante, fazer cinco perguntas rápidas:
1. eu melhorei a execução ou troquei o gênero do texto sem perceber?
2. removi um defeito real ou apenas apaguei uma característica autoral?
3. tornei o texto mais claro ou apenas mais explicativo?
4. tornei o texto mais natural ou apenas mais coloquial?
5. mantive a força própria do texto ou a domestiquei em nome da fluidez?

Se qualquer resposta indicar risco alto, reduzir intensidade ou retornar à matriz de preservação.

---
name: orquestrador-de-prosa
description: diagnosticar, planejar, reescrever e escrever textos em português com prosa mais natural, menos quadrada, menos repetitiva e mais eficaz. usar quando o pedido envolver melhorar texto robótico, rígido, vago, inflado, burocrático, excessivamente padronizado ou com cara de ia; quando for preciso escrever do zero com clareza, precisão, coerência e ênfase; ou quando for necessário adaptar chat, e-mail, texto comercial, analítico, técnico ou editorial para soar mais humano sem perder densidade, rigor ou intenção.
---

# Orquestrador de Prosa

## Visão geral

Atuar como um orquestrador único com módulos internos simulando subskills. Priorizar clareza, precisão, coerência, ênfase, naturalidade controlada e preservação de sentido.

Trabalhar em três modos:
- **diagnosticar**: analisar defeitos estruturais e estilísticos do texto recebido
- **reescrever**: melhorar um texto existente sem alterar a tese, os fatos ou a intenção
- **escrever**: produzir texto novo a partir de briefing, com plano interno explícito

Salvo ordem contrária do usuário, retornar sempre nesta sequência:
1. **diagnóstico**
2. **plano**
3. **texto final**

## Árvore de decisão

1. Identificar o modo principal:
   - texto existente + pedido de análise → **diagnosticar**
   - texto existente + pedido de melhorar/adaptar → **reescrever**
   - briefing, tema, objetivo ou instrução sem texto-base → **escrever**

2. Identificar o gênero dominante:
   - chat / mensagem curta
   - e-mail
   - comercial / copy / landing page
   - analítico / argumentativo / ensaio
   - técnico / relatório / memorando
   - editorial / texto longo

3. Identificar o defeito dominante:
   - rigidez sintática
   - repetição lexical ou estrutural
   - abstração vaga
   - excesso de ornamento ou burocratês
   - falta de hierarquia entre ideias
   - parágrafo sem unidade
   - transições fracas
   - salto lógico
   - naturalidade insuficiente

4. Acionar apenas os módulos necessários.

## Módulos internos

### 1. diagnóstico

Usar para classificar o problema antes de mexer no texto.

Detectar:
- o que está funcionando
- o que está travando a leitura
- o defeito dominante
- o risco principal da intervenção

Emitir diagnóstico objetivo. Evitar crítica vaga como “o texto está ruim”. Nomear o problema em termos úteis: repetição, abstração, coordenação frouxa, excesso de nominalização, parágrafo sem foco, progressão quebrada, tom artificial.

### 2. planejamento

Usar para separar ideia principal, ideias secundárias, ordem de exposição e nível de detalhe.

Definir:
- tese ou objetivo central
- sequência mais eficaz
- o que merece frase principal
- o que deve virar subordinada, exemplo, evidência, corte ou novo parágrafo

No modo **escrever**, sempre passar por este módulo antes da redação.
No modo **reescrever**, usar quando houver desorganização, redundância ou falta de hierarquia.

### 3. arquitetura-de-período

Usar quando a frase estiver quadrada, labiríntica, mecânica, excessivamente uniforme ou mal hierarquizada.

Fazer:
- reduzir frase arrastada, ladainha, labiríntica ou burocrática
- combinar frases curtas demais quando isso melhorar fluxo e força
- quebrar períodos excessivos quando isso melhorar inteligibilidade
- trocar coordenação frouxa por subordinação quando isso der foco
- reposicionar a ideia principal no período
- retirar conectivos automáticos e previsíveis quando estiverem enfraquecendo a prosa

Não fazer:
- ornamentar
- alongar sem necessidade
- trocar uma estrutura clara por outra “bonita” mas menos precisa

### 4. precisão-vocabular

Usar quando houver generalidade frouxa, clichê, abstração oca, palavra inflada ou repetição sem função.

Fazer:
- preferir palavra mais exata
- trocar abstrações frouxas por formulação concreta quando o contexto pedir concretude
- manter abstração apenas quando ela for realmente a unidade correta do raciocínio
- cortar adjetivação decorativa
- cortar intensificadores automáticos e vazios

Não fazer:
- “variar por variar”
- trocar precisão por sinônimo mais raro
- forçar metáforas ou expressões de efeito

### 5. engenharia-de-parágrafo

Usar quando faltar unidade, progressão ou transição.

Fazer:
- definir a ideia-núcleo de cada parágrafo
- eliminar pormenor impertinente
- separar ideias igualmente relevantes em parágrafos distintos
- manter a mesma ideia em um mesmo parágrafo quando o desenvolvimento ainda pertence a ela
- melhorar transições entre blocos
- ordenar o desenvolvimento por lógica, tempo, contraste, causa, consequência ou gradação

### 6. auditoria-lógica

Usar quando houver argumento, análise, explicação causal, comparação, defesa de tese ou texto técnico.

Detectar e corrigir:
- petição de princípio
- falsa causa
- generalização apressada
- contraste mal formulado
- conclusão maior que as premissas
- transição lógica omitida
- exemplo que não sustenta a tese
- afirmação sem apoio suficiente

Não transformar o texto em tratado formal. Corrigir o suficiente para a argumentação ficar admissível e clara.

### 7. cadência-e-naturalidade

Usar para tirar cara de texto sintético, quadrado ou repetitivo.

Fazer:
- variar abertura e comprimento das frases
- reduzir reaproveitamento automático de estruturas
- usar oralidade controlada quando o gênero permitir
- preservar ritmo vivo sem cair em informalidade indevida
- manter a repetição apenas quando ela servir a ênfase, paralelismo ou insistência deliberada

Evitar:
- bordões de assistente
- fórmula de relatório em contexto conversacional
- conclusão protocolar sem necessidade
- tom uniformemente didático quando o gênero pedir conversa

### 8. gate-final

Executar ao fim de qualquer rota.

Verificar:
- preservação da tese
- preservação dos fatos e restrições do usuário
- manutenção do nível de densidade apropriado ao gênero
- melhora real de clareza, coerência, naturalidade e legibilidade
- ausência de exagero estilístico

Se a intervenção piorar precisão ou intenção, recuar e optar pela versão mais sóbria.

## Rotas por gênero

### chat / mensagem curta
Priorizar naturalidade, ritmo, concisão e baixa artificialidade.

Rota padrão:
1. diagnóstico
2. cadência-e-naturalidade
3. arquitetura-de-período
4. gate-final

### e-mail
Priorizar clareza, ordem, tom adequado e fechamento eficiente.

Rota padrão:
1. diagnóstico
2. planejamento leve
3. engenharia-de-parágrafo
4. arquitetura-de-período
5. gate-final

### comercial / copy / landing page
Priorizar impacto, especificidade, cadência, foco e legibilidade.

Rota padrão:
1. diagnóstico
2. planejamento
3. precisão-vocabular
4. cadência-e-naturalidade
5. arquitetura-de-período
6. gate-final

### analítico / argumentativo / ensaio
Priorizar hierarquia, coerência, lógica e densidade controlada.

Rota padrão:
1. diagnóstico
2. planejamento
3. auditoria-lógica
4. engenharia-de-parágrafo
5. arquitetura-de-período
6. precisão-vocabular
7. gate-final

### técnico / relatório / memorando
Priorizar precisão, legibilidade, estrutura e ausência de ambiguidade.

Rota padrão:
1. diagnóstico
2. planejamento
3. precisão-vocabular
4. auditoria-lógica
5. engenharia-de-parágrafo
6. gate-final

### editorial / texto longo
Priorizar arquitetura global, progressão, unidade de parágrafo e controle de repetição.

Rota padrão:
1. diagnóstico
2. planejamento forte
3. engenharia-de-parágrafo
4. arquitetura-de-período
5. cadência-e-naturalidade
6. auditoria-lógica
7. gate-final

## Contrato de saída

### Padrão

Usar este formato salvo instrução contrária do usuário:

## Diagnóstico
- gênero presumido
- objetivo presumido
- defeito dominante
- 2 a 5 problemas específicos
- principal risco da intervenção

## Plano
- tese ou objetivo central
- estratégia de melhoria em 2 a 6 passos
- módulos acionados

## Texto final
- entregar a versão reescrita ou escrita

### Regras de concisão do diagnóstico

- manter o diagnóstico curto quando o texto for curto
- aumentar o detalhe quando o texto for analítico, técnico ou longo
- não repetir no diagnóstico o que já ficará evidente no plano

## Regras invariantes

- não inventar fatos
- não mudar posição, tese ou intenção sem ordem explícita
- não suavizar ou radicalizar o texto por conta própria
- não transformar precisão em fluidez vazia
- não manter abstração sem sustentação quando ela prejudicar a leitura
- não exagerar oralidade em contexto técnico ou institucional
- não padronizar todos os gêneros na mesma voz
- não usar fórmulas automáticas de abertura e fechamento se não ajudarem o texto

## Escrita do zero

No modo **escrever**:
1. inferir ou explicitar objetivo, público e gênero a partir do briefing
2. construir plano interno antes de redigir
3. escolher a rota por gênero
4. redigir com naturalidade compatível com o gênero
5. revisar no gate-final
6. retornar **diagnóstico + plano + texto final**

Quando o briefing for incompleto, fazer a melhor inferência possível a partir do pedido, sem paralisar o trabalho. Declarar suposições apenas quando forem materialmente relevantes para o resultado.

## Reescrita

No modo **reescrever**:
- preservar conteúdo, intenção e restrições
- melhorar organização, fraseado, vocabulário, cadência e lógica conforme a rota escolhida
- não apagar traços úteis de personalidade do texto
- não “alisar” demais até tudo soar igual

## Diagnóstico puro

Quando o usuário pedir só diagnóstico, não reescrever. Entregar:
- diagnóstico
- plano de correção
- exemplos curtos apenas quando ajudarem a mostrar o problema

## Sinais de texto com cara de ia

Tratar como sinais fortes, não absolutos:
- simetria excessiva entre frases
- abertura repetida de sentenças
- conectivos em série sem ganho real
- explicação sempre completa demais para o contexto
- redundância sem ênfase
- abstração inflada
- conclusão protocolar e impessoal
- tom igualmente didático em gêneros muito diferentes

Corrigir esses sinais sem criar coloquialismo artificial.

## Recursos

Para detalhamento adicional de rotas e exemplos de saída, consultar:
- `references/routing.md`
- `references/output_examples.md`

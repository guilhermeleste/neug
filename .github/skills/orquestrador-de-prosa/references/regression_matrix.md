# Matriz cruzada de regressão

## Objetivo

Usar esta matriz quando o risco principal não estiver em um defeito isolado do texto, mas no **efeito colateral da transformação pedida**.

Ela cruza três elementos:
1. **gênero ou natureza da peça**
2. **alvo principal da operação**
3. **regressão mais provável**

A pergunta central é:
**que melhora aparente pode estragar a função real do texto?**

## Protocolo de uso

Aplicar quando pelo menos uma destas condições aparecer:
- o texto já funciona razoavelmente bem
- o pedido do usuário é genérico: “melhore”, “deixe melhor”, “humanize”, “deixe mais executivo”
- o alvo desejado empurra o texto para outro registro
- o gênero depende de voz, atmosfera, precisão, energia ou formalidade específicas
- a mudança pretendida envolve migração de gênero, meio ou público

Passos:
1. identificar o par **gênero + alvo**
2. localizar a **regressão mais provável**
3. reduzir a intensidade se o ganho potencial for menor que o dano provável
4. validar a saída no gate final com foco no risco identificado

## Escala de risco

- **baixo**: o alvo tende a ajudar o gênero e raramente cria dano estrutural
- **médio**: o alvo ajuda, mas exige contenção
- **alto**: o alvo frequentemente gera regressão séria se aplicado de forma automática
- **crítico**: só executar com forte matriz de preservação e checagem adversarial

---

## 1. Texto técnico ou documental

### Alvo: tornar mais natural
- risco: **alto**
- regressão provável: perder precisão, condição, exceção ou causalidade
- preservar: terminologia crítica, sequência procedural, números, restrições
- sinal de boa saída: leitura menos opaca sem queda de exatidão

### Alvo: tornar mais persuasivo
- risco: **médio**
- regressão provável: extrapolar além do que o documento sustenta
- preservar: relação entre prova e conclusão
- sinal de boa saída: ênfase maior sem prometer mais do que o texto prova

### Alvo: condensar
- risco: **alto**
- regressão provável: cortar condição material ou exceção operacional
- preservar: passos mínimos executáveis e estados críticos
- sinal de boa saída: peça menor, mas ainda operacional

### Alvo: adaptar para leigo
- risco: **alto**
- regressão provável: metáfora frouxa ou simplificação distorciva
- preservar: mecanismo central e limites do sistema
- sinal de boa saída: entendimento ampliado sem falsificação do mecanismo

---

## 2. Ensaio, análise e resposta longa

### Alvo: tornar mais claro
- risco: **médio**
- regressão provável: simplificar demais distinções conceituais
- preservar: densidade legítima, gradação, termos de precisão
- sinal de boa saída: mais legível sem banalização

### Alvo: condensar
- risco: **alto**
- regressão provável: amputar premissas necessárias e deixar conclusões soltas
- preservar: eixo analítico e passos do raciocínio
- sinal de boa saída: menos extensão com mesma espinha lógica

### Alvo: tornar mais natural
- risco: **médio**
- regressão provável: diluir arquitetura em nome da fluidez
- preservar: hierarquia argumentativa e voz intelectual
- sinal de boa saída: texto menos protocolar, não menos rigoroso

### Alvo: tornar mais elegante
- risco: **médio**
- regressão provável: elevar a dicção e enfraquecer a precisão
- preservar: núcleo conceitual
- sinal de boa saída: forma mais limpa, não mais ornamental

---

## 3. Copy, anúncio e texto comercial

### Alvo: tornar mais sóbrio
- risco: **alto**
- regressão provável: perder tração, urgência e aderência
- preservar: promessa, benefício, chamada para ação
- sinal de boa saída: menos excesso sem queda de impulso

### Alvo: tornar mais elegante
- risco: **alto**
- regressão provável: trocar memorabilidade por refinamento vazio
- preservar: impacto e clareza do ganho
- sinal de boa saída: texto mais limpo que ainda vende

### Alvo: tornar mais técnico
- risco: **médio**
- regressão provável: burocratizar a oferta e esfriar o desejo
- preservar: benefício e valor percebido
- sinal de boa saída: credibilidade maior sem matar resposta

### Alvo: expandir
- risco: **médio**
- regressão provável: encher de espuma promocional
- preservar: progressão entre dor, solução, prova e ação
- sinal de boa saída: expansão acrescenta prova e concretude, não redundância

---

## 4. Narrativa curta, crônica e descrição

### Alvo: tornar mais claro
- risco: **alto**
- regressão provável: explicar o implícito e destruir atmosfera
- preservar: ponto de vista, textura, subentendido, ordem sensível dos detalhes
- sinal de boa saída: menos tropeço, mesma ambiência

### Alvo: condensar
- risco: **médio**
- regressão provável: cortar detalhe que sustenta imagem ou tensão
- preservar: cena central e elementos sensoriais decisivos
- sinal de boa saída: texto mais enxuto sem perder sugestão

### Alvo: tornar mais natural
- risco: **médio**
- regressão provável: normalizar a sintaxe e apagar voz
- preservar: assinatura narrativa e cadência própria
- sinal de boa saída: fluidez maior sem padronização

### Alvo: tornar mais persuasivo
- risco: **crítico**
- regressão provável: contaminar narrativa com lógica argumentativa estranha ao gênero
- preservar: função estética ou evocativa
- sinal de boa saída: só aplicar se houver pedido inequívoco de hibridização

---

## 5. Chat, mensagem curta e e-mail

### Alvo: tornar mais natural
- risco: **baixo**
- regressão provável: pouca, salvo expansão indevida
- preservar: ação principal, timing e relação contextual
- sinal de boa saída: leitura em um fôlego, sem soar montado

### Alvo: tornar mais claro
- risco: **baixo**
- regressão provável: nenhuma séria, se houver contenção
- preservar: brevidade funcional
- sinal de boa saída: pedido ou resposta aparecem mais cedo

### Alvo: tornar mais elegante
- risco: **médio**
- regressão provável: afetação, excesso de polidez ou miniaturização de e-mail em texto literário
- preservar: objetivo operacional
- sinal de boa saída: mais limpo, não mais enfeitado

### Alvo: expandir
- risco: **alto**
- regressão provável: transformar mensagem eficiente em bloco explicativo
- preservar: velocidade e foco
- sinal de boa saída: só expandir quando o contexto pedir informação nova real

---

## 6. Comunicação institucional, memorando e texto decisório

### Alvo: tornar mais humano
- risco: **alto**
- regressão provável: diluir firmeza, responsabilidade e precisão institucional
- preservar: decisão, vigência, efeito, responsabilidade
- sinal de boa saída: leve aumento de legibilidade sem coloquialização indevida

### Alvo: tornar mais curto
- risco: **médio**
- regressão provável: apagar contexto necessário para compreender alcance da medida
- preservar: decisão e seus efeitos
- sinal de boa saída: texto mais enxuto sem opacidade decisória

### Alvo: mudar de meio para chat
- risco: **crítico**
- regressão provável: perda de formalidade, rastreabilidade e blindagem
- preservar: núcleo da decisão e suas condições
- sinal de boa saída: resumir com cautela, oferecendo a peça completa quando necessário

---

## 7. Manifesto, posicionamento e peça quente

### Alvo: tornar mais técnico
- risco: **alto**
- regressão provável: neutralizar antagonismo e apagar núcleo valorativo
- preservar: posição central e temperatura intencional
- sinal de boa saída: maior disciplina expositiva sem esterilização

### Alvo: tornar mais sóbrio
- risco: **médio**
- regressão provável: enfraquecer energia legítima
- preservar: força central e consequência política ou simbólica
- sinal de boa saída: menos excesso improdutivo, mesma tensão axial

### Alvo: transformar em comunicado institucional
- risco: **crítico**
- regressão provável: trocar adaptação por apagamento
- preservar: decisão, posição e conteúdo irredutível
- sinal de boa saída: o texto muda de vestimenta sem perder a espinha

---

## 8. Texto já bom + pedido genérico de melhoria

### Alvo: “melhore”
- risco: **crítico**
- regressão provável: intervenção performática, perda de voz e achatamento da peça
- preservar: tudo o que já funciona
- sinal de boa saída: pouca mudança com ganho local verificável

### Alvo: “deixe melhor”
- risco: **crítico**
- regressão provável: reescrita desnecessária para demonstrar serviço
- preservar: arquitetura funcional e assinatura do texto
- sinal de boa saída: contenção máxima e justificativa interna clara para cada mudança

---

## Decisão rápida

Se o cruzamento **gênero + alvo** cair em risco **alto** ou **crítico**, fazer duas coisas obrigatórias:
1. reforçar a matriz de preservação
2. aplicar checagem adversarial antes de entregar

Se o cruzamento cair em risco **baixo**, priorizar rapidez e proporcionalidade.

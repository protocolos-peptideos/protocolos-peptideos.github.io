# Protocolos — peptídeos, nootrópicos e correlatos

Referência em português sobre peptídeos, nootrópicos, SARMs e compostos correlatos: dose, titulação, reconstituição, estrutura de ciclo e status regulatório, com o limite da evidência marcado em cada página.

O repositório e a URL guardam o nome antigo, `protocolos-peptideos` — renomear quebraria todo link já publicado. O site cobre mais que peptídeos desde setembro de 2026.

**70 compostos e combinações · 362 tabelas de dose · 73 páginas estáticas.**

Contagens da última execução do gerador, em 4 de setembro de 2026. Ele as imprime a cada rodada — se divergirem daqui, o gerador é que está certo.

### ▶ [protocolos-peptideos.github.io](https://protocolos-peptideos.github.io/)

Publicado por GitHub Pages a partir deste repositório.

---

## ⚠️ Aviso

Material **educacional e experimental**. Nada aqui é recomendação médica, prescrição ou plano de tratamento.

A maior parte dos compostos não tem aprovação da ANVISA nem da FDA para uso humano. Vários são vendidos com rótulo de "uso exclusivo em pesquisa", o que significa que não passaram por controle de pureza, esterilidade ou dosagem para consumo por pessoas. **Dose descrita por comunidade não é dose validada.**

---

## Fonte e método

Os dados de protocolo foram compilados de [peptidedosingprotocols.com](https://www.peptidedosingprotocols.com/), acesso em 3 de setembro de 2026. É uma fonte secundária de caráter comercial, não uma publicação revisada por pares — e isso limita a confiabilidade de tudo que está aqui.

Três decisões de método:

1. **Nenhum número foi retipado à mão.** Todo valor de dose, volume, concentração e duração foi transportado por script, célula a célula. O que mudou foi o separador decimal (ponto → vírgula) e o separador de milhar (vírgula → ponto), porque `5,000 mcg` em inglês é cinco mil, e em português seria cinco. Retipar dose à mão é como se erra dose.

2. **Os textos em português são autorais.** Resumos, alertas e as seções de segurança foram escritos a partir da leitura da fonte, não traduzidos linha a linha. São mais curtos que o original.

3. **Portão de tradução.** Uma tabela só é publicada se passar num teste automático de sinal linguístico. Tabela que não passa é descartada, não publicada pela metade. O gerador reporta a contagem a cada execução.

Todo conteúdo comercial da fonte foi removido: links de fornecedor, cupons, seções de "onde comprar" e recomendação de loja.

### O que ficou de fora

- **Fontes primárias, nas páginas importadas.** Nas páginas de protocolo vindas da fonte secundária, nenhum artigo do PubMed, registro de ensaio ou bula foi aberto: a checagem foi contra a fonte, e só. Continua sendo a limitação principal delas.
- **A exceção são as páginas de evidência verificada**, hoje 13, onde cada número foi levantado no PubMed, no ClinicalTrials.gov, no dado aberto da ANVISA, na bula ou na lista da WADA, com a consulta declarada na própria página.
- **Calculadoras interativas**, para não dar aparência de precisão a uma conta que depende de conferir o frasco na mão.
- **Fornecedores e preços**, deliberadamente.

---

## Estrutura

```
index.html            grade dos compostos, com busca e filtro por categoria
seguranca.html        riscos que não aparecem na tabela de dose
sobre.html            fonte, método e limites
p/<slug>.html         uma página por composto
assets/estilo.css     sistema visual (escuro, acento de cobre)
assets/app.js         busca e filtro, sem dependências
build/gerar.py        gerador estático
build/compostos.py    metadados PT-BR de cada composto (autoral)
build/fatos.py        faixa de referência rápida por composto (autoral)
build/dicionario*.py  dicionário EN→PT-BR das células de tabela
build/idiomas.py      versões em en/ es/ de/ fr/ ja/, geradas do HTML em português
build/traducoes/      memória de tradução por idioma (<idioma>.json) e o briefing dos tradutores
build/datas.py        as duas datas do site, num lugar só
build/trava_datas.py  trava que impede data cravada ou tirada do relógio
build/trava_consultas.py  trava que exige a consulta ao lado da contagem
build/reconferir.py   reexecuta as consultas e avisa o que envelheceu
hooks/pre-commit      roda as duas travas antes de deixar commitar
```

## As duas datas, e por que existe uma trava para elas

O site afirma duas datas sobre si mesmo: **3 de setembro de 2026**, quando a fonte secundária foi raspada, e **4 de setembro de 2026**, quando a apuração em fonte primária foi feita. As duas vivem em `build/datas.py` e em nenhum outro lugar.

A tentação óbvia é trocá-las por `datetime.now()`. **Não pode.** O gerador roda de novo a cada edição de texto; com data de relógio, o site passaria a afirmar, a cada rebuild, que foi conferido hoje — sem que ninguém tenha conferido nada. Data velha e correta vale mais que data fresca e falsa.

`build/trava_datas.py` transforma isso em garantia. Checa o AST, não o texto, para não acusar comentário que apenas mencione o problema. Duas regras: nenhum módulo deriva data do relógio, e nenhum módulo além do `datas.py` escreve à mão as datas do próprio site. Data que é **conteúdo** — quando um ensaio começou, quando a FDA revisou uma bula — fica onde está: é fato reportado, não afirmação do site sobre si.

A trava roda no início do `gerar.py`, que aborta sem escrever nada, e no hook de pre-commit. **Num clone novo o hook precisa ser ligado uma vez:**

```bash
git config core.hooksPath hooks
```

## A segunda trava: contagem publicada tem que reproduzir

Em 04/09/2026, uma auditoria reexecutou as consultas que as próprias páginas declaravam. Uma não reproduziu: estava publicada como `… AND (Clinical Trial[Publication Type] ...)`, com reticências no lugar do termo inicial. Quem copiasse receberia **1.059.391** em vez de **35**, porque o PubMed ignora a elipse. O número da página estava certo; o que estava quebrado era a possibilidade de conferir.

`build/trava_consultas.py` transforma isso em garantia, checando o conteúdo carregado e não o código. Três regras:

1. **Consulta declarada não pode ser abreviada** — nada de elipse, "idem", "mesma consulta". Ou escreve inteira, ou não é consulta.
2. **Tabela que publica contagem de PubMed ou ClinicalTrials.gov precisa declarar a consulta** — coluna `Consulta` na tabela, ou a busca literal em `<code>` no texto da seção.
3. **Apelido de filtro precisa da expressão literal** — uma coluna chamada "ECR/meta" não reproduz busca nenhuma; a expressão completa tem que aparecer em `<code>` na página.

A trava **não** acusa número que é conteúdo de terceiro. "A meta-análise reuniu 21 estudos" é fato reportado, não levantamento do site, e não tem consulta para declarar. Uma primeira versão acusava 12 ocorrências, das quais 9 eram desse tipo — e trava que acusa o legítimo ensina a ser ignorada. Por isso a regra só olha tabela.

### A dívida que ela herdou — e que foi paga

Quatro tabelas nasceram antes da trava e publicavam contagem sem a consulta. Medido na época: rodando o nome simples do composto, reproduzi 3 de 15 linhas na página do leste europeu e 1 de 7 na de SARMs.

Os quatro levantamentos foram **refeitos em 04/09/2026**, com a consulta de cada linha definida, rodada e publicada ao lado do número. A lista `DIVIDA` está vazia.

Ficou uma lição registrada no código: buscando `LGD-4033 OR ligandrol` no ClinicalTrials.gov o resultado é **zero**, e a página teria afirmado que o ligandrol nunca entrou em ensaio. O ensaio existe — fase 2, 108 participantes, fratura de quadril — registrado sob o sinônimo `VK5211`. Consulta declarada não serve só para o leitor conferir: serve para quem escreve **perceber que a própria busca estava incompleta**.

Estado atual, medido reexecutando toda consulta declarada em tabela no site: **63 de 65 reproduzem**. As duas restantes são o Semax, que oscila em um artigo conforme a indexação do dia, e uma linha cuja base é o ClinicalTrials.gov e não o PubMed.

## Reconferir os números, de tempos em tempos

A trava garante que todo número publicado venha com a consulta que o produziu. Isso torna o site conferível — mas não impede que os números **envelheçam em silêncio**. O PubMed indexa artigo novo todo dia; uma contagem correta em setembro pode estar velha em dezembro sem que nada no repositório mude.

`build/reconferir.py` fecha esse buraco. Ele lê as consultas do próprio conteúdo, roda cada uma e compara com o publicado:

```bash
python build/reconferir.py --quieto
```

```
Reconferência de 87 contagens publicadas.
Data de apuração declarada no site: 4 de setembro de 2026

  iguais 87 · oscilaram dentro de 2.0% 0 · DIVERGEM 0 · erro de rede 0
```

Opções: `--pagina proprio_leste` para conferir só uma, `--limiar 5` para tolerar 5% de variação, `--json arquivo.json` para gravar o relatório. **Sai com código 1 quando algo diverge**, para servir de gatilho em tarefa agendada.

Ele distingue busca por condição de busca por intervenção no ClinicalTrials.gov — são coisas diferentes e devolvem números diferentes. A página diz qual usou, e o script obedece.

### O que ele deliberadamente não faz

**Não corrige nada.** A tentação óbvia seria reescrever os números sozinho — e aí o site passaria a afirmar, com a data de apuração antiga, resultados colhidos em outro dia. Número e data de apuração andam juntos: quem atualiza um atualiza o outro, e isso é decisão de quem apura, não de um script agendado.

## Outros idiomas

O site sai também em `/en/`, `/es/`, `/de/`, `/fr/` e `/ja/`, com a mesma estrutura da raiz e um seletor no cabeçalho. **A versão em português é a de referência**, e a página Sobre de cada idioma diz isso. As páginas traduzidas não trazem aviso de tradução no topo, por decisão de 10/09/2026.

As versões não são traduções dos módulos Python: `build/idiomas.py` pega cada página em português **já gerada**, recorta os trechos de texto (parágrafo, item, célula, título, atributo visível) e substitui cada um pela entrada correspondente em `build/traducoes/<idioma>.json`. Duas consequências:

1. **Texto novo em português aparece sozinho como pendente** nos outros idiomas. Até ser traduzido, sai em português, marcado com `lang="pt-BR"`, e o gerador imprime a cobertura de cada idioma a cada rodada.
2. **Tradução não inventa número.** Antes de entrar na página, cada trecho passa por uma trava: o conjunto de números tem de ser o mesmo do original, lido no separador decimal do idioma (`1,125 mL` em português é `1.125 mL` em inglês e continua `1,125 mL` em alemão); as tags, os `href` e o conteúdo de `<code>` — as consultas do PubMed — têm de ser idênticos. Trecho reprovado não é publicado: fica em português e vai para `build/traducoes/rejeitados/`.

Para o inglês, as células de tabela têm uma camada automática (`en-fonte.json`): a fonte era em inglês, então a "tradução" da célula é o próprio original. O resto — e tudo nos outros idiomas — foi traduzido com IA a partir do português, seguindo `build/traducoes/INSTRUCOES.md`, sem revisão de tradutor humano.

Fluxo para traduzir o que estiver pendente:

```bash
python build/gerar.py                 # imprime a cobertura e grava build/traducoes/pendentes/<idioma>/parte-NN.json
# traduzir cada parte para build/traducoes/entregas/<idioma>/parte-NN.json (formato em INSTRUCOES.md)
python build/idiomas.py --incorporar  # valida e grava o que passou em <idioma>.json
python build/gerar.py                 # regera as seis versões
```

## Regenerar

```bash
python build/gerar.py
```

O gerador depende de `build/src/*.json`, a extração da fonte — que **não está versionada** (ver `.gitignore`). O repositório guarda o material autoral e a ferramenta, não uma cópia do site de origem. Para reconstruir do zero é preciso refazer a extração localmente.

## Rodar

```bash
python -m http.server 8231
```

Sem build, sem dependências, sem JavaScript de terceiros. As fontes moram em `assets/fontes/`; tudo é local.

---

## Direitos

Valores numéricos de protocolo são fatos e não são objeto de direito autoral. A organização, os textos em português e o projeto visual são autorais. A fonte está creditada com link em todas as páginas.

Site pessoal, sem publicidade, sem afiliação e sem finalidade comercial. Havendo pedido justificado do detentor dos direitos da fonte, o material sai do ar.

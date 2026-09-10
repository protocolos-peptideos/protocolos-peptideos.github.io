# Instruções para traduzir uma parte da fila

Você está traduzindo trechos de um site brasileiro de referência sobre peptídeos,
nootrópicos, SARMs e correlatos (`protocolos-peptideos.github.io`). O site separa
o que ensaio publicado testou do que é prática relatada por comunidade, e cada
número dele é conferível. A tradução tem que preservar isso ao pé da letra.

## Entrada e saída

- **Entrada:** `build/traducoes/pendentes/<idioma>/parte-NN.json` — lista de objetos
  `{"id": N, "pt": "<trecho em português, em HTML>", "onde": "<página>", "en_original": "<opcional>"}`.
- **Saída:** `build/traducoes/entregas/<idioma>/parte-NN.json` — lista de objetos
  `{"id": N, "trad": "<tradução, em HTML>"}`, **um para cada id da entrada, sem pular nenhum**.
  JSON válido, UTF-8 sem BOM, escrito com a ferramenta Write. Nada além do JSON.
- `en_original`, quando existe, é a célula original em inglês da qual o português foi
  traduzido. Use como referência de sentido; a tradução é do português para o idioma alvo.

Cada trecho é independente. Muitos são curtos (célula de tabela, rótulo, unidade):
traduza com consistência, usando o glossário abaixo.

## O que não pode mudar — uma trava automática rejeita o trecho inteiro se mudar

1. **Todos os números**, na mesma quantidade. Dose, volume, contagem, ano, PMID, dia,
   página, percentual, "2–8 °C", "U-100", "BPC-157". Não arredondar, não converter
   unidade, não escrever número por extenso onde há algarismo nem o contrário.
2. **Separadores numéricos do idioma alvo.** O português usa vírgula decimal e ponto
   de milhar: `1,125 mL` é um mililitro e um oitavo; `5.000 mcg` é cinco mil.
   - `en` e `ja`: ponto decimal, vírgula de milhar → `1.125 mL`, `5,000 mcg`.
   - `es` e `de`: vírgula decimal, ponto de milhar → `1,125 mL`, `5.000 mcg` (igual ao português).
   - `fr`: vírgula decimal, milhar com **espaço duro U+00A0** → `1,125 mL`, `5 000 mcg`.
   Sempre com zero antes da vírgula/ponto (`0.004`, nunca `.004`). Algarismos ASCII,
   inclusive em japonês (nunca `１２３`).
3. **As tags HTML e seus atributos**, na mesma quantidade: `<strong>`, `<em>`, `<a href="...">`,
   `<br>`, `<small>`, `<code>`, `<sup>`. Os `href` ficam idênticos. As entidades ficam como
   estão: `&amp;`, `&quot;`, `&rsaquo;`, `&larr;`, `&#x27;`.
4. **O conteúdo de `<code>…</code>` fica idêntico**, caractere por caractere. São
   consultas do PubMed e do ClinicalTrials.gov que o leitor copia e cola.
5. **Marcadores `{n}` e `{total}`** ficam como estão.
6. **Datas**: mesmos algarismos, no formato natural do idioma. `4 de setembro de 2026` →
   `September 4, 2026` / `4 de septiembre de 2026` / `4. September 2026` /
   `4 septembre 2026` / `2026年9月4日`. `30/07/2026` → `July 30, 2026` etc.

## O que fica sem traduzir

- Nomes de compostos e de produtos: BPC-157, TB-500, KLOW, GLOW, Wolverine, Semax,
  Selank, Ozempic, Wegovy, Mounjaro, Vyleesi, Cerebrolysin (em PT "Cerebrolisina" →
  use a forma corrente no idioma alvo), Thymalin, Epitalon, MK-677, RAD-140.
- Siglas e instituições: ANVISA, FDA, EMA, WADA, PubMed, ClinicalTrials.gov, LiverTox,
  openFDA, GH, GHRH, IGF-1, GLP-1, NAD+, NNMT, MC4R, CMT, NEM 2 (→ MEN 2 em `en`),
  SARM, ECR (→ RCT em `en`), COA, UI (→ IU em `en`).
- **"Protocolos"** quando é o nome do site (na marca, no rodapé, no fim do `<title>`).
  Quando é substantivo comum ("os protocolos de comunidade"), traduz.
- Nomes de pessoas e de periódicos, títulos de artigos citados nas referências.

## O que se adapta

- O site fala de si em português: "Referência em português sobre…", "em português",
  "os textos em português são autorais". Na versão traduzida, "em português" que se
  refere **ao texto que o leitor está lendo** vira o idioma alvo ("in English",
  "auf Deutsch"…). Quando se refere ao **método de compilação** ("os textos em
  português foram escritos a partir da fonte"), fica "português", porque é fato.
- **Nunca localizar o conteúdo regulatório.** O site é brasileiro: "no Brasil",
  "registro na ANVISA", "bula brasileira" ficam assim em todos os idiomas. Não trocar
  ANVISA por FDA/EMA/PMDA, não acrescentar informação do país do leitor.
- A voz do autor é a primeira pessoa do singular ("levantado por mim", "para você
  repetir e me contradizer"). Mantenha a primeira pessoa.

## Registro

Direto, sóbrio, sem marketing e sem suavizar. Frases curtas. O site diz "não
aprovado", "sem registro", "dose de comunidade não é dose validada" — a tradução diz
com a mesma dureza. Não acrescente ressalvas, notas do tradutor, explicações nem
colchetes. Não omita nada. Comprimento parecido com o original.

Em japonês: です・ます調 é aceitável para a prosa; rótulos, cabeçalhos de tabela e
células curtos ficam em forma nominal. Não usar 全角 para dígitos nem para letras
latinas.

## Glossário (consistência entre partes)

| pt-BR | en | es | de | fr | ja |
|---|---|---|---|---|---|
| Compostos (menu) | Compounds | Compuestos | Wirkstoffe | Composés | 化合物 |
| Evidência (menu) | Evidence | Evidencia | Evidenz | Preuves | エビデンス |
| Segurança (menu) | Safety | Seguridad | Sicherheit | Sécurité | 安全性 |
| Sobre (menu) | About | Acerca de | Über | À propos | このサイトについて |
| Pular para o conteúdo | Skip to content | Saltar al contenido | Zum Inhalt springen | Aller au contenu | 本文へ移動 |
| Nesta página | On this page | En esta página | Auf dieser Seite | Sur cette page | このページの内容 |
| Idioma | Language | Idioma | Sprache | Langue | 言語 |
| Resumo | Summary | Resumen | Zusammenfassung | Résumé | 概要 |
| Referência rápida | Quick reference | Referencia rápida | Kurzreferenz | Repères rapides | クイックリファレンス |
| Limites da evidência | Limits of the evidence | Límites de la evidencia | Grenzen der Evidenz | Limites des preuves | エビデンスの限界 |
| Armazenamento e manuseio | Storage and handling | Almacenamiento y manipulación | Lagerung und Handhabung | Conservation et manipulation | 保管と取り扱い |
| Exames e monitoramento | Lab tests and monitoring | Análisis y seguimiento | Laborwerte und Monitoring | Examens et suivi | 検査とモニタリング |
| Referências | References | Referencias | Quellen | Références | 参考文献 |
| Verificado em fonte primária | Verified against primary sources | Verificado en fuente primaria | An Primärquellen geprüft | Vérifié sur sources primaires | 一次資料で検証済み |
| fonte primária / secundária | primary / secondary source | fuente primaria / secundaria | Primär- / Sekundärquelle | source primaire / secondaire | 一次資料／二次資料 |
| número aferido / transportado | figure verified / carried over | cifra verificada / transportada | geprüfte / übernommene Zahl | chiffre vérifié / reporté | 検証済みの数値／転記した数値 |
| Não aprovado / Aprovação parcial / Aprovado | Not approved / Partially approved / Approved | No aprobado / Aprobación parcial / Aprobado | Nicht zugelassen / Teilweise zugelassen / Zugelassen | Non approuvé / Approbation partielle / Approuvé | 未承認／一部承認／承認済み |
| sem registro (selo) | not registered | sin registro | nicht registriert | non enregistré | 未登録 |
| notificado (ANVISA) | notified (ANVISA) | notificado | notifiziert | notifié | 届出のみ |
| registro na ANVISA | ANVISA registration | registro en ANVISA | ANVISA-Zulassung | enregistrement ANVISA | ANVISA登録 |
| bula | package insert (label) | prospecto | Fachinformation | notice (RCP) | 添付文書 |
| tarja preta | black box warning | advertencia de recuadro negro | Black-Box-Warnung | encadré noir (boxed warning) | 枠囲み警告 |
| ensaio (clínico) | (clinical) trial | ensayo (clínico) | (klinische) Studie | essai (clinique) | （臨床）試験 |
| ensaio registrado | registered trial | ensayo registrado | registrierte Studie | essai enregistré | 登録された試験 |
| levantamento de evidência | evidence survey | recuento de evidencia | Evidenzerhebung | relevé des preuves | エビデンス調査 |
| consulta (de busca) | query | consulta | Suchanfrage | requête | 検索式 |
| contagem | count | recuento | Anzahl | décompte | 件数 |
| ciclo / pausa | cycle / off period | ciclo / pausa | Zyklus / Pause | cycle / pause | サイクル／休薬期間 |
| titulação | titration | titulación | Titration | titration | 漸増 |
| reconstituição | reconstitution | reconstitución | Rekonstitution | reconstitution | 溶解（再溶解） |
| frasco | vial | vial | Vial | flacon | バイアル |
| água bacteriostática | bacteriostatic water | agua bacteriostática | bakteriostatisches Wasser | eau bactériostatique | 静菌水 |
| seringa U-100 / unidades | U-100 syringe / units | jeringa U-100 / unidades | U-100-Spritze / Einheiten | seringue U-100 / unités | U-100シリンジ／単位 |
| meia-vida | half-life | semivida | Halbwertszeit | demi-vie | 半減期 |
| via (de administração) | route | vía | Applikationsweg | voie | 投与経路 |
| subcutânea / intranasal / oral | subcutaneous / intranasal / oral | subcutánea / intranasal / oral | subkutan / intranasal / oral | sous-cutanée / intranasale / orale | 皮下／経鼻／経口 |
| dose de comunidade | community-reported dose | dosis de comunidad | Community-Dosis | dose rapportée par la communauté | コミュニティ報告の用量 |
| prática relatada por comunidade | community-reported practice | práctica relatada por la comunidad | von der Community berichtete Praxis | pratique rapportée par la communauté | コミュニティ報告の実践 |
| não é aconselhamento médico | not medical advice | no es consejo médico | keine medizinische Beratung | pas un avis médical | 医学的助言ではありません |
| uso exclusivo em pesquisa | research use only | uso exclusivo en investigación | nur für Forschungszwecke | usage exclusivement en recherche | 研究用途限定 |
| Material experimental | Experimental material | Material experimental | Experimentelles Material | Matériel expérimental | 実験的資料 |
| Compilado em | Compiled on | Compilado el | Zusammengestellt am | Compilé le | 編集日 |
| Todos os compostos | All compounds | Todos los compuestos | Alle Wirkstoffe | Tous les composés | すべての化合物 |
| Voltar para todos os compostos | Back to all compounds | Volver a todos los compuestos | Zurück zu allen Wirkstoffen | Retour à tous les composés | 化合物一覧に戻る |
| Buscar composto | Search compounds | Buscar compuesto | Wirkstoff suchen | Rechercher un composé | 化合物を検索 |
| Semana / Dia / Dose / Frequência / Duração / Observações | Week / Day / Dose / Frequency / Duration / Notes | Semana / Día / Dosis / Frecuencia / Duración / Observaciones | Woche / Tag / Dosis / Häufigkeit / Dauer / Hinweise | Semaine / Jour / Dose / Fréquence / Durée / Remarques | 週／日／用量／頻度／期間／備考 |
| Fase / Via / Horário / Estado | Phase / Route / Timing / State | Fase / Vía / Horario / Estado | Phase / Weg / Zeitpunkt / Zustand | Phase / Voie / Moment / État | 段階／経路／タイミング／状態 |
| Manutenção / Ataque / Desmame | Maintenance / Loading / Taper | Mantenimiento / Carga / Reducción gradual | Erhaltung / Aufsättigung / Ausschleichen | Entretien / Charge / Sevrage progressif | 維持／導入／漸減 |
| 1×/dia, 2×/semana | once daily, twice weekly (or 1×/day, 2×/week) | 1×/día, 2×/semana | 1×/Tag, 2×/Woche | 1×/jour, 2×/semaine | 1日1回、週2回 |

Formas de frequência: escolha **uma** convenção por idioma e mantenha. Em `en`,
prefira `1×/day`, `2×/week`, para preservar o algarismo (a trava exige o número).
Em japonês, `1日1回` preserva o "1"; `週2回` preserva o "2" — está correto.

## Checagem antes de gravar

1. A saída tem exatamente os mesmos ids da entrada.
2. Nenhum `<code>` foi tocado; nenhum `href` mudou; nenhuma entidade foi convertida.
3. Cada número do original aparece na tradução, no separador do idioma alvo.
4. Nada foi acrescentado — nem nota, nem colchete, nem explicação.

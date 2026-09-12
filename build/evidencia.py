# -*- coding: utf-8 -*-
"""Pagina de indice das paginas montadas de fonte primaria.

A data da rodada nova nao pode ser escrita a mao aqui: vem de datas.py, como
manda a trava. Por isso CORPO e uma f-string.
"""

from datas import DATA_NOVAS_CLASSES as _DT

CORPO = f"""
<h2>O que separa estas páginas do resto do site</h2>

<p>A maior parte deste site é tradução organizada de uma fonte secundária comercial. Está declarado em cada
página, e é a fraqueza estrutural do material: se a fonte errou, eu repito o erro.</p>

<p>As <strong>páginas listadas abaixo</strong> são diferentes. Cada número nelas foi levantado por mim
diretamente no <strong>PubMed</strong> e no <strong>ClinicalTrials.gov</strong>, com a consulta usada declarada
dentro da própria página, para que qualquer pessoa possa repetir e me contradizer. Cobrem
<strong>179 compostos distintos</strong>, mais <strong>106 substâncias e tratamentos</strong> levantados na rodada de {_DT}, nas nove páginas abertas naquele dia.</p>

<p>Não é uma seção de destaque por vaidade de método. É porque, das duas coisas que um site destes pode fazer —
listar dose ou dizer o que a dose vale —, só a segunda é difícil de achar em português.</p>

<h2 id="paginas">As páginas desta seção</h2>

<div class="tabela-env"><div class="tabela-rolagem"><table aria-labelledby="paginas">
<thead><tr><th scope="col">Página</th><th scope="col">Compostos</th><th scope="col">O achado central</th></tr></thead>
<tbody>
<tr>
  <td><a href="p/proprio_anvisa.html"><strong>O que existe no Brasil</strong></a></td>
  <td>44</td>
  <td><strong>40 dos 44 compostos deste site não têm nenhum medicamento registrado na ANVISA.</strong> Varredura
      do dado aberto oficial, 43.489 registros. O resultado agora aparece em cada página de composto</td>
</tr>
<tr>
  <td><a href="p/proprio_glp1_bula.html"><strong>Os GLP-1 contra a bula</strong></a></td>
  <td>6</td>
  <td>A única página deste site conferida contra <strong>gabarito oficial</strong>, e a única com duas fontes
      regulatórias. As escadas <strong>batem com a FDA e com a ANVISA</strong>, degrau por degrau. Faltava a
      <strong>tarja preta</strong>, faltava a dose de <strong>7,2 mg</strong> que só existe no Brasil, e as duas
      agências <strong>discordam</strong> sobre contraindicar a semaglutida</td>
</tr>
<tr>
  <td><a href="p/proprio_mazdutida.html"><strong>Mazdutida</strong></a></td>
  <td>1</td>
  <td>O composto com a <strong>evidência mais madura de todo o site</strong>, e o contrário do padrão daqui:
      <strong>12 ensaios de fase 3</strong>, com GLORY-1 no NEJM, GLORY-2 na JAMA e as duas DREAMS na Nature —
      e <strong>nenhum registro na FDA ou na ANVISA</strong>. Os 12 são de patrocinador e população
      <strong>chineses</strong>, e a meta-análise que reúne 2.292 participantes classifica a certeza em
      obesidade como <strong>muito baixa</strong> no mesmo texto em que reporta perda de peso de dois dígitos</td>
</tr>
<tr>
  <td><a href="p/proprio_exossomos.html"><strong>Exossomos</strong></a></td>
  <td>1</td>
  <td>A assimetria mais extrema do site: <strong>45.674 artigos no PubMed e 83 ensaios randomizados</strong>,
      menos de 0,2%. Dos 378 registros no ClinicalTrials.gov, <strong>142 são observacionais</strong> — medem
      exossomo como marcador, não tratam ninguém com ele. Abri os <strong>nove de fase 3</strong>: um é um
      estudo de PET/CT em câncer de próstata que entrou na busca por citar “exosome analysis”, e sete dos
      outros oito têm <strong>135 participantes ou menos</strong>. A FDA diz desde 2019 que <strong>não existe
      exossomo aprovado</strong>, com carta de advertência nova em fevereiro de 2026</td>
</tr>
<tr>
  <td><a href="p/proprio_anticorpos.html"><strong>Anticorpos monoclonais</strong></a></td>
  <td>3</td>
  <td>Os três que aparecem junto com os GLP-1 quando o assunto é massa magra, e a escala de evidência não
      acompanha a conversa: o <strong>trevogrumab tem 2 artigos no PubMed, nenhum deles ensaio</strong>, e um
      único estudo registrado. O único com rótulo aprovado pela FDA é o garetosmab, e não para peso — é para
      uma doença rara, em <strong>infusão venosa de 60 minutos a cada quatro semanas</strong>. A molécula pesa
      <strong>cerca de 146 kDa contra 4.113,58 g/mol da semaglutida</strong>, é produzida em cultura de células
      e não sintetizada: não existe aqui frasco para reconstituir</td>
</tr>
<tr>
  <td><a href="p/proprio_incretinas.html"><strong>Incretinas e amilinas de nova geração</strong></a></td>
  <td>13</td>
  <td>A inversão entre literatura e desenvolvimento. O <strong>HRS-9531 tem 0 artigos no PubMed e 9 ensaios de fase 3 registrados</strong>; a liraglutida, que serve de régua, tem 5.909. Quem julga estas moléculas pela contagem de artigo conclui que metade não existe. <strong>9 das 11 com DCI publicada não têm registro ativo na ANVISA</strong></td>
</tr>
<tr>
  <td><a href="p/proprio_eixo_gh.html"><strong>O eixo do GH fora do frasco de peptídeo</strong></a></td>
  <td>7</td>
  <td><strong>GHRP-2 e hexarelina têm zero estudos registrados no ClinicalTrials.gov</strong>, com 256 e 313 artigos no PubMed. A molécula foi estudada; o tratamento, não. Do outro lado, a somatropina tem 183 ensaios de fase 3 e 9 registros ativos na ANVISA</td>
</tr>
<tr>
  <td><a href="p/proprio_geroprotetores.html"><strong>Geroprotetores</strong></a></td>
  <td>17</td>
  <td><strong>6 das 17 linhas não têm nenhum ensaio de fase 3 registrado</strong>, entre elas o klotho recombinante e a troca plasmática. A rapamicina tem 259 — e nenhum dos que abri é sobre envelhecimento. Os <strong>2 ensaios de fase 3 de fisetina declaram inscrição de zero participantes</strong></td>
</tr>
<tr>
  <td><a href="p/proprio_figado_lipidio.html"><strong>Fígado e lipídio</strong></a></td>
  <td>13</td>
  <td>O contrário do padrão do site: literatura de dezenas de artigos e <strong>ensaios de desfecho de até 17.300 participantes</strong> — os quatro maiores somam 46.047. E, das treze, <strong>só a inclisirana tem registro ativo na ANVISA</strong></td>
</tr>
<tr>
  <td><a href="p/proprio_calvicie.html"><strong>Calvície — o antigo e o que está chegando</strong></a></td>
  <td>18</td>
  <td><strong>A clascoterona está registrada no Brasil na classe anti-acne, não para cabelo.</strong> O PP405, que já circula como pó de pesquisa, tem 1 artigo no PubMed e 0 ensaios de fase 3; o VDPHL01 tem o oposto — 0 artigos e 3 ensaios de fase 3 com mais de mil pessoas recrutadas</td>
</tr>
<tr>
  <td><a href="p/proprio_reparo_novos.html"><strong>Reparo além do BPC e do TB-500</strong></a></td>
  <td>5</td>
  <td><strong>A fase 3 da timosina β-4 é colírio para olho seco</strong> — 700 e 601 participantes, e não reparo de tendão. O AHK-Cu tem 1 artigo no PubMed. O único registro de fase 3 que a busca por polidesoxirribonucleotídeo devolve é de defibrotida em doença veno-oclusiva hepática</td>
</tr>
<tr>
  <td><a href="p/proprio_neuro_novos.html"><strong>Neuro e cognição — o bloco russo e o que tem bula</strong></a></td>
  <td>13</td>
  <td>Noopept, fenilpiracetam, bromantano e cortexina somam <strong>0 estudos registrados</strong> no ClinicalTrials.gov, apesar de somarem 435 artigos no PubMed. No mesmo levantamento, <strong>lecanemabe e donanemabe já têm registro ativo na ANVISA</strong></td>
</tr>
<tr>
  <td><a href="p/proprio_musculo_hpg.html"><strong>Músculo, osso, eixo HPG e imune</strong></a></td>
  <td>15</td>
  <td>O ensaio testou doença rara; o frasco promete recomposição. <strong>Os 6 ensaios de fase 3 de afamelanotida que abri são de protoporfiria eritropoiética</strong>, e os de setmelanotida, de obesidade por variante genética. <strong>8 das 14 buscas voltam vazias na ANVISA</strong></td>
</tr>
<tr>
  <td><a href="p/proprio_procedimentos.html"><strong>Tratamentos que não são substância</strong></a></td>
  <td>5</td>
  <td>O comparador que quase nunca aparece: a cirurgia bariátrica tem 36.916 artigos e 2.039 estudos registrados. Já a oxigenoterapia hiperbárica cruzada com envelhecimento tem <strong>1 ensaio de fase 3, com 30 participantes</strong></td>
</tr>
<tr>
  <td><a href="p/proprio_sarms.html"><strong>SARMs</strong></a></td>
  <td>16</td>
  <td><strong>Os dois únicos ensaios de fase 3 do campo nunca foram publicados</strong> — 651 pacientes que só
      existem como tabela no ClinicalTrials.gov, um deles postado com sete anos e meio de atraso. E antes da
      molécula vem a mercadoria: <strong>só 52% dos produtos continham algum SARM</strong>. Andarina, YK-11 e
      S-23: <strong>zero ensaios</strong></td>
</tr>
<tr>
  <td><a href="p/proprio_semax_evidencia.html"><strong>Semax — a evidência</strong></a></td>
  <td>1</td>
  <td>Os ensaios russos usaram <strong>6.000 a 18.000 mcg/dia</strong>; a comunidade usa 250 a 1.000. A faixa
      praticada <strong>nunca foi testada</strong>. Zero registros, e um dos quatro estudos é negativo</td>
</tr>
<tr>
  <td><a href="p/proprio_klow_evidencia.html"><strong>KLOW — a evidência</strong></a></td>
  <td>4</td>
  <td>A blend segue sem ensaio, mas <strong>BPC-157, TB-500 e GHK-Cu entraram em fase clínica em 2026</strong> —
      três estudos da Hudson Biotech recrutando. Deixou de ser só pré-clínico</td>
</tr>
<tr>
  <td><a href="p/proprio_nootropicos.html"><strong>Nootrópicos</strong></a></td>
  <td>44</td>
  <td>32 têm ensaio, <strong>12 não têm nenhum</strong>. Modafinil lidera com 425; <strong>noopept tem 115
      artigos e zero ensaios</strong>. Quatro contagens estavam infladas e foram refeitas</td>
</tr>
<tr>
  <td><a href="p/proprio_efeito.html"><strong>Tamanho de efeito</strong></a></td>
  <td>19</td>
  <td>A outra metade da página acima: <strong>o que os ensaios acharam</strong>, não quantos existem. Onde há
      efeito, ele fica entre <strong>SMD 0,2 e 0,4</strong>. <strong>Três compostos populares têm ensaio grande e
      negativo</strong> — oxiracetam (n=500), cerebrolisina (n=1779) e piracetam</td>
</tr>
<tr>
  <td><a href="p/proprio_bioreguladores.html"><strong>Bioreguladores de Khavinson</strong></a></td>
  <td>11</td>
  <td><strong>Zero ensaios registrados</strong> no ClinicalTrials.gov. Oito dos onze não têm nenhum artigo de
      ensaio clínico. Sete não têm nem sequência química indexada. Toda a literatura clínica da família se
      concentra em dois compostos</td>
</tr>
<tr>
  <td><a href="p/proprio_thymalin.html"><strong>Thymalin</strong></a></td>
  <td>1</td>
  <td>293 artigos e 13 ensaios — o outlier da família. Mas <strong>zero registros</strong>, e o estudo que
      sustenta toda a alegação de longevidade é assinado pelo próprio inventor</td>
</tr>
<tr>
  <td><a href="p/proprio_meldonium.html"><strong>Meldonium</strong></a></td>
  <td>1</td>
  <td>357 artigos, 35 ensaios, <strong>7 registros</strong>. O achado que decide o uso não é de eficácia: a
      janela de detecção urinária chega a <strong>117 dias</strong> após seis dias de uso</td>
</tr>
<tr>
  <td><a href="p/proprio_leste.html"><strong>Medicamentos do leste europeu</strong></a></td>
  <td>17</td>
  <td><strong>29 ensaios registrados</strong>, vários de fase 3 — o oposto dos bioreguladores. E um sinal
      esquecido: o hopantenato de cálcio tem <strong>47 casos e 11 mortes</strong> por encefalopatia relatados
      desde 1986 — com <strong>7 ensaios randomizados, vários em crianças</strong></td>
</tr>
<tr>
  <td><a href="p/proprio_suplementos.html"><strong>Suplementos de venda livre</strong></a></td>
  <td>43</td>
  <td>Contagem de ensaios item a item, com dose, <strong>nos 43</strong>. <strong>Resveratrol tem 391 ensaios e
      decepcionou</strong>; glicina, alpha-GPC, butirato, fisetina e o magnésio L-treonato têm entre 2 e 5 cada</td>
</tr>
<tr>
  <td><a href="p/proprio_fitoterapicos.html"><strong>Fitoterápicos e nootrópicos</strong></a></td>
  <td>18</td>
  <td><strong>Fadogia agrestis: zero.</strong> Nenhum ensaio, nenhum estudo humano — conferi os três artigos que
      o PubMed marca como humanos e nenhum é. Lion's Mane tem dois</td>
</tr>
<tr>
  <td><a href="p/proprio_tarja.html"><strong>Itens de tarja</strong></a></td>
  <td>12</td>
  <td>Medicamentos de prescrição que apareciam misturados a vitamina D e creatina numa lista de suplementos.
      <strong>Única página do site sem posologia</strong>, por decisão</td>
</tr>
</tbody>
</table></div></div>

<p class="nota"><strong>A coluna não soma 179.</strong> Duas páginas são segundo corte dos mesmos compostos,
não compostos novos: a de tamanho de efeito reanalisa 19 que já aparecem nas outras, e a de registro na ANVISA
varre os 44 compostos de protocolo do site, que não são contados como material de fonte primária.</p>

<h2>Três coisas que este levantamento ensinou</h2>

<h3>1. Muita literatura não é o mesmo que evidência</h3>
<p>Os onze bioreguladores de Khavinson somam quase duzentos artigos no PubMed e <strong>zero ensaios
registrados</strong>. Registro prévio é o que impede que um desfecho ruim vire outro desfecho na publicação —
sem ele, não há como saber quantos estudos ficaram na gaveta. Contagem de artigo mede atividade acadêmica,
não confiabilidade.</p>

<h3>2. Volume alto não é resultado favorável</h3>
<p>O resveratrol tem 391 ensaios randomizados e metanálises, e a promessa não se confirmou. O ginkgo tem 88 e
continua não recomendado para prevenir demência, porque os grandes ensaios deram negativo. O probiótico tem
5.248 — o maior número do site — e é o mais enganoso, porque o efeito é de cepa específica e não se transfere
para o frasco que você comprou.</p>

<h3>3. Buscar pelo nome comercial infla a conta</h3>
<p>Ao levantar os bioreguladores, um ensaio randomizado apareceu para o <em>Ovagen</em>. Fui ler: era um estudo
de superovulação em <strong>vacas</strong>, porque Ovagen também é marca de FSH veterinário. No bloco do leste
europeu, cocarboxilase e citocromo C aparecem com centenas de artigos que tratam de bioquímica do metabolismo
e de apoptose — não do injetável. <strong>Quando a molécula tem função biológica própria, a contagem mede a
biologia, não o remédio.</strong></p>

<p>Na página de nootrópicos o mesmo problema apareceu de outra forma: o PubMed expande a busca por
<em>armodafinil</em> para o termo MeSH <em>modafinil</em>, e devolve 2.437 contra 2.411 — quase o mesmo
conjunto. Restrito a título e resumo, armodafinil tem 260. E quatro contagens de suplemento estavam infladas
pela mesma razão: L-tirosina caiu de 199 para 14, uridina de 62 para 6, forskolina de 30 para 5 e a agmatina,
de 9 para <strong>zero</strong>.</p>

<h2>O que continua faltando</h2>

<ul>
  <li><strong>Li resumos e metadados, não artigos completos</strong>, salvo nos casos em que o achado dependia
      disso — o Fadogia e o hopantenato de cálcio, que abri e conferi um a um.</li>
  <li><strong>Contagem não é qualidade.</strong> Um número alto pode ser cem ensaios pequenos e mal feitos. É a
      limitação central do método usado aqui.</li>
  <li><strong>Não há mais item sem contagem.</strong> Os 27 que estavam em branco nas páginas de suplementos,
      fitoterápicos e leste europeu foram fechados, e os dois da página do KLOW também. Fechá-los corrigiu um
      número errado meu — Cortexin tinha 26 artigos declarados e tem 127 — e mostrou que cocarboxilase,
      citocromo C e Etoxidol não têm <strong>nenhum</strong> ensaio randomizado.</li>
  <li><strong>Literatura russa fora do PubMed não foi consultada.</strong> A escola de Khavinson publica muito em
      periódico não indexado — a ausência aqui não prova ausência absoluta.</li>
  <li><strong>As outras 57 páginas do site continuam dependendo da fonte secundária.</strong> Este método ainda
      não foi aplicado a elas.</li>
</ul>

<div class="nota"><strong>Como conferir o que está aqui.</strong> Toda página desta seção declara a consulta
que usei e a data. Abra o PubMed ou o ClinicalTrials.gov, repita a busca e compare. Se o número mudou, é porque
a literatura andou — e se estava errado, é erro meu, não da fonte.</div>
"""

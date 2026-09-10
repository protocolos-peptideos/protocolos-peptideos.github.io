# -*- coding: utf-8 -*-
"""Versoes do site em outros idiomas.

COMO FUNCIONA

O gerador continua produzindo o site em portugues exatamente como antes. Este
modulo entra DEPOIS: le cada pagina pronta, recorta os trechos de texto
(paragrafo, item de lista, celula, titulo, atributo visivel), procura cada um
numa memoria de traducao por idioma (build/traducoes/<idioma>.json) e grava a
pagina traduzida em /<idioma>/<mesmo caminho>.

Por que pos-processar o HTML e nao traduzir os modulos de conteudo:

  1. O conteudo em portugues mora em ~10 mil linhas de Python, com texto
     dentro de f-string e de dicionario. Traduzir na origem seria refatorar
     tudo isso em catalogo de mensagens -- num repositorio que outras sessoes
     editam ao mesmo tempo.
  2. Todo texto novo em portugues aparece automaticamente como PENDENTE nos
     outros idiomas, sem que ninguem precise lembrar de nada. A pagina sai
     com o trecho em portugues marcado com lang="pt-BR", e o relatorio diz.
  3. A traducao nunca pode inventar numero. Cada trecho traduzido passa por
     uma trava antes de entrar na pagina: o conjunto de numeros tem que ser
     o mesmo do original (respeitando o separador decimal de cada idioma),
     as tags HTML e os href tem que ser os mesmos, e o que esta em <code>
     -- as consultas do PubMed -- tem que ser identico. Trecho que nao passa
     nao e publicado: fica em portugues e vai para o relatorio de rejeitados.

A versao em portugues e a de referencia. As paginas traduzidas nao trazem
aviso de traducao no topo -- decisao do Fernando em 10/09/2026; o metodo e
o limite da traducao estao na pagina Sobre de cada idioma.

USO

  Chamado por gerar.py ao fim de cada build. Tambem roda sozinho:

    python build/idiomas.py --pendentes     reescreve a fila build/traducoes/pendentes/<idioma>/parte-NN.json
                                            (recusa se houver entrega ainda nao incorporada)
    python build/idiomas.py --gerar         so regera /<idioma>/, sem tocar na fila
    python build/idiomas.py --incorporar    le build/traducoes/entregas/<idioma>/*.json, valida e
                                            grava o que passou em build/traducoes/<idioma>.json
"""
import html
import json
import os
import re
import sys
from collections import Counter
from html.parser import HTMLParser

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = 'https://protocolos-peptideos.github.io'
PASTA = os.path.join(RAIZ, 'build', 'traducoes')

# Separadores numericos por idioma. E o que a trava usa para ler "1,125 mL"
# como um e um oitavo em portugues e "1.125 mL" como a mesma coisa em ingles.
# Para o frances, o milhar aceita so espaco duro (U+00A0, U+202F): espaco
# comum juntaria "fase 2 100 mg" num numero que nao existe.
IDIOMAS = {
    'en': dict(nome='English',  decimal='.', milhar=',',
               aviso='Translated from the Portuguese original with AI assistance. Numbers, doses, '
                     'dates and references were checked mechanically, but the text was not reviewed '
                     'by a human translator. <a href="{pt}" hreflang="pt-BR" lang="pt-BR">The Portuguese '
                     'version is the reference.</a>'),
    'es': dict(nome='Español',  decimal=',', milhar='.',
               aviso='Traducido del original en portugués con ayuda de IA. Los números, dosis, fechas '
                     'y referencias se verificaron mecánicamente, pero el texto no fue revisado por un '
                     'traductor humano. <a href="{pt}" hreflang="pt-BR" lang="pt-BR">La versión en '
                     'portugués es la de referencia.</a>'),
    'de': dict(nome='Deutsch',  decimal=',', milhar='.',
               aviso='Mit KI-Unterstützung aus dem portugiesischen Original übersetzt. Zahlen, Dosen, '
                     'Daten und Quellenangaben wurden maschinell geprüft, der Text jedoch nicht von einem '
                     'menschlichen Übersetzer durchgesehen. <a href="{pt}" hreflang="pt-BR" lang="pt-BR">'
                     'Die portugiesische Fassung ist maßgeblich.</a>'),
    'fr': dict(nome='Français', decimal=',', milhar='  ',
               aviso='Traduit de l’original en portugais avec l’aide d’une IA. Les nombres, doses, dates '
                     'et références ont été vérifiés mécaniquement, mais le texte n’a pas été relu par un '
                     'traducteur humain. <a href="{pt}" hreflang="pt-BR" lang="pt-BR">La version '
                     'portugaise fait foi.</a>'),
    'ja': dict(nome='日本語',     decimal='.', milhar=',',
               aviso='ポルトガル語の原文からAIの支援で翻訳しました。数値・用量・日付・参考文献は機械的に照合しましたが、'
                     '人間の翻訳者による校閲は行っていません。<a href="{pt}" hreflang="pt-BR" lang="pt-BR">'
                     'ポルトガル語版が正となります。</a>'),
}
PT = dict(nome='Português', decimal=',', milhar='.')
ORDEM = ['pt-BR'] + list(IDIOMAS)

# Cada idioma ganha uma pasta com a mesma estrutura da raiz.
PAGINAS_RAIZ = ['index.html', 'evidencia.html', 'seguranca.html', 'sobre.html']

# ANVISA so em portugues, por decisao do Fernando em 10/09/2026. A pagina
# abaixo nao existe nas outras versoes (nem no seletor, nem no sitemap), e todo
# trecho que cita a ANVISA passa pela camada build/traducoes/sem-anvisa/, que
# reescreve o trecho sem a agencia ou o retira da pagina.
SO_PT = {'p/proprio_anvisa.html'}

# Unicas correcoes de numero aceitas na camada sem ANVISA: a contagem de
# paginas do indice cai um quando a pagina da ANVISA sai.
AJUSTES_PERMITIDOS = {('76', '75'), ('19', '18')}


# ------------------------------------------------------------------ trava
_FULLWIDTH = {ord(c): str(i) for i, c in enumerate('０１２３４５６７８９')}


_SECAO = re.compile(r'\d+\.\d{1,2}(?!\d)')


def _rx_numeros(decimal, milhar):
    d = re.escape(decimal)
    m = '[' + ''.join(re.escape(c) for c in milhar) + ']'
    # Nos idiomas de virgula decimal, "8.7" nao pode ser decimal nem milhar:
    # e numero de secao de bula ("secao 8.7"), versao, item de lista. Fica um
    # token so, lido como 8,7, que e como o ingles vai le-lo. "1.125" continua
    # sendo mil cento e vinte e cinco -- sao tres digitos, e e essa a
    # diferenca que a trava existe para pegar.
    secao = r'\d+\.\d{1,2}(?!\d)|' if decimal == ',' else ''
    return re.compile(secao + r'\d{1,3}(?:%s\d{3})+(?:%s\d+)?|\d+(?:%s\d+)?' % (m, d, d))


_DOI = re.compile(r'10\.\d{4,9}/[^\s<]+')


def numeros(txt, conv):
    """Multiconjunto dos valores numericos do texto, lidos na convencao dada.

    DOI fica de fora: "10.7326/M20-3555" nao e numero, e cada idioma o leria
    com seu separador. Ele segue protegido pela comparacao de href."""
    txt = _DOI.sub(' ', txt.translate(_FULLWIDTH))
    # data alema "22.04.2026": tres numeros, nao um decimal seguido de ano
    b = chr(92)
    txt = re.sub('(?<![' + b + 'd.])(' + b + 'd{1,2})' + b + '.(' + b + 'd{1,2})' + b + '.(' + b + 'd{4})(?![' + b + 'd])', b + '1 ' + b + '2 ' + b + '3', txt)
    # japones: o "1日" de "1日2回" e "por dia", nao um numero do original
    # tambem em faixa e com teto: "1日1-3回", "1日最大3回"
    d = chr(92) + 'd+'
    txt = re.sub('1日(?=(?:最大)?' + d + '(?:[-–~〜]' + d + ')?回)', '日', txt)
    rx = _rx_numeros(conv['decimal'], conv['milhar'])
    vals = Counter()
    for tok in rx.findall(txt):
        if conv['decimal'] == ',' and _SECAO.fullmatch(tok):
            vals[round(float(tok), 9)] += 1
            continue
        t = re.sub('[' + ''.join(re.escape(c) for c in conv['milhar']) + ']', '', tok)
        t = t.replace(conv['decimal'], '.')
        vals[round(float(t), 9)] += 1
    return vals


# Nomes de mes por idioma: a unica perda de numero que a trava tolera e a
# do mes de uma data numerica ("14/03/2024") que virou nome ("March 14, 2024").
MESES = {
    'en': 'january february march april may june july august september october november december'.split(),
    'es': 'enero febrero marzo abril mayo junio julio agosto septiembre setiembre octubre noviembre diciembre'.split(),
    'de': 'januar februar märz april mai juni juli august september oktober november dezember'.split(),
    'fr': 'janvier février mars avril mai juin juillet août septembre octobre novembre décembre'.split(),
    'ja': [],
}
MESES_PT = ('janeiro fevereiro março abril maio junho julho agosto setembro outubro novembro dezembro '
            'jan fev mar abr mai jun jul ago set out nov dez '
            # o proprio pt tem residuo em ingles vindo da fonte ('November 2023')
            'january february march april june july august september october november december').split()

_TAG = re.compile(r'<(/?)([a-zA-Z][\w-]*)([^>]*)>')
_HREF = re.compile(r'href="([^"]*)"')
_CODE = re.compile(r'<code>(.*?)</code>', re.S)
_CHAVES = re.compile(r'\{[a-z_]+\}')


def _tags(s):
    out = Counter()
    for fecha, nome, attrs in _TAG.findall(s):
        h = _HREF.search(attrs)
        out[(bool(fecha), nome.lower(), h.group(1) if h else '')] += 1
    return out


def _excecoes():
    """Trechos conferidos a mao e dispensados da trava de numeros.

    build/traducoes/excecoes.json: {idioma: [chave, ...]}. Existe para o caso
    que a trava nao tem como ler: "seção 8.7" da bula e um numero de secao,
    que em portugues a trava le como 8 e 7 e em ingles como 8,7. So entra aqui
    trecho que alguem leu e aprovou -- e o arquivo diz qual."""
    return _le_json(os.path.join(PASTA, 'excecoes.json'))


_MILHAR_PT = re.compile(r'(?<![\d,.])\d{1,3}(?:\.\d{3})+(?![\d])')


def _conserta_milhar_fr(chave, trad):
    """Troca espaco comum por U+00A0 nos milhares que o proprio original tem.

    Tradutor escreve "7 646" com espaco comum com frequencia. A trava nao pode
    aceitar espaco comum como milhar em geral ("fase 2 100 mg" viraria 2100),
    mas aqui a troca e guiada pelo original: so os numeros que o portugues
    escreve com ponto de milhar sao procurados, na forma exata com espaco."""
    for tok in set(_MILHAR_PT.findall(chave)):
        grupos = tok.split('.')
        comum = ' '.join(grupos)
        duro = ' '.join(grupos)
        trad = re.sub(r'(?<![\d])' + re.escape(comum) + r'(?![\d])', duro, trad)
    return trad


def valida(chave, trad, idioma):
    """Lista de problemas; vazia quando a traducao pode entrar na pagina."""
    probs = []
    if not isinstance(trad, str) or not trad.strip():
        return ['vazia']
    if trad.strip() == chave.strip():
        # identico ao portugues: aceito (nome proprio, sigla, unidade)
        return []
    a, b = numeros(chave, PT), numeros(trad, IDIOMAS[idioma])
    if chave in _excecoes().get(idioma, []):
        a = b
    if a != b:
        falta = sorted((a - b).elements())
        sobra = sorted((b - a).elements())
        # Unica perda tolerada: o mes de uma data numerica ("14/03/2024")
        # virou nome de mes ("March 14, 2024"). So passa se os valores que
        # sumiram sao inteiros de 1 a 12, nada sobrou, e ha nome de mes na
        # traducao em quantidade suficiente para explicar cada um.
        meses = sum(len(re.findall(chr(92)+'b'+m+chr(92)+'b', trad, re.I)) for m in MESES[idioma])
        so_mes = (not sobra and falta
                  and all(v == int(v) and 1 <= v <= 12 for v in falta)
                  and meses >= len(falta))
        # O caminho inverso, do japones: "14 de marco de 2024" vira
        # "2024年3月14日", e o mes que era nome vira numero. Aceito so quando
        # o que sobrou sao inteiros de 1 a 12, em quantidade coberta pelos
        # nomes de mes do original em portugues.
        meses_pt = sum(len(re.findall(chr(92) + 'b' + m + chr(92) + 'b', chave, re.I)) for m in MESES_PT)
        so_mes_ja = (idioma == 'ja' and not falta and sobra
                     and all(v == int(v) and 1 <= v <= 12 for v in sobra)
                     and meses_pt >= len(sobra))
        if not (so_mes or so_mes_ja):
            probs.append('numeros: faltam %s, sobram %s' % (falta, sobra))
    if _tags(chave) != _tags(trad):
        probs.append('tags/href diferentes')
    if Counter(_CODE.findall(chave)) != Counter(_CODE.findall(trad)):
        probs.append('conteudo de <code> alterado')
    if Counter(_CHAVES.findall(chave)) != Counter(_CHAVES.findall(trad)):
        probs.append('marcadores {x} diferentes')
    if any('０' <= c <= '９' for c in trad):
        probs.append('digito de largura inteira')
    return probs


def valida_sem(chave, orig, nova, idioma, ajuste=None):
    """Trava da camada sem ANVISA.

    A versao nova so pode TIRAR coisas da traducao que ja passou na trava
    principal: nenhum numero, tag, href ou <code> que ela nao tivesse. A unica
    troca de numero aceita e a de AJUSTES_PERMITIDOS, declarada no arquivo."""
    probs = []
    base = orig if orig else chave
    conv = IDIOMAS[idioma] if orig else PT
    if re.search('anvisa|アンビサ', nova, re.I):
        probs.append('ainda cita a ANVISA')
    if 'proprio_anvisa' in nova:
        probs.append('link para a pagina da ANVISA')
    a = numeros(base, conv)
    for k, v in (ajuste or {}).items():
        if (str(k), str(v)) not in AJUSTES_PERMITIDOS:
            probs.append('ajuste de numero nao permitido: %s -> %s' % (k, v))
            continue
        kf, vf = float(k), float(v)
        if a[kf]:
            a[vf] += a[kf]
            del a[kf]
    sobra = numeros(nova, IDIOMAS[idioma]) - a
    if sobra:
        probs.append('numero que a traducao nao tinha: %s' % sorted(sobra.elements()))
    if _tags(nova) - _tags(base):
        probs.append('tag ou href novo')
    abre = Counter(n for f, n, h in _tags(nova).elements() if not f)
    fecha = Counter(n for f, n, h in _tags(nova).elements() if f)
    for n in set(abre) | set(fecha):
        if n not in VAZIO and abre[n] != fecha[n]:
            probs.append('tag <%s> desbalanceada' % n)
    if Counter(_CODE.findall(nova)) - Counter(_CODE.findall(base)):
        probs.append('<code> alterado')
    return probs


def carrega_sem_anvisa(idioma):
    """{trecho pt: (versao sem ANVISA, ajuste)} de sem-anvisa/<idioma>*.json."""
    pasta = os.path.join(PASTA, 'sem-anvisa')
    out = {}
    if not os.path.isdir(pasta):
        return out
    for f in sorted(os.listdir(pasta)):
        if not re.fullmatch(re.escape(idioma) + r'(-[\w-]+)?\.json', f):
            continue
        for it in _le_json(os.path.join(pasta, f)):
            chave = _norm(it['pt'])
            nova = _norm(it.get('trad') or '')
            if idioma == 'fr' and nova:
                nova = _conserta_milhar_fr(chave, nova)
            # A linha "No Brasil: ..." de cada composto e so dado da ANVISA:
            # sai em todos os idiomas, qualquer que seja a reescrita entregue.
            if chave.startswith('<strong>No Brasil:'):
                nova = ''
            out[chave] = (nova, it.get('ajuste') or {})
    return out


def _remocao(fonte, ini, fim, tipo, no):
    """Faixa a apagar quando o trecho sem ANVISA fica vazio."""
    if no.tag in ('td', 'th'):
        return (ini, fim, '—') if tipo == 'inner' else (ini, fim, '')
    if tipo == 'attr' and no.tag in ('meta', 'form', 'title'):
        return (ini, fim, '')
    alvo = no
    # sobe enquanto o pai so contem este elemento: <li> com um link so, etc.
    while (alvo.pai is not None and alvo.pai.tag in ('li', 'p', 'small', 'strong', 'em')
           and alvo.pai.fim is not None and len(alvo.pai.filhos) == 1 and not alvo.pai.texto):
        alvo = alvo.pai
    a, b = alvo.ini, alvo.fim
    while a > 0 and fonte[a - 1] in ' \t':
        a -= 1
    if b < len(fonte) and fonte[b] == '\n' and (a == 0 or fonte[a - 1] == '\n'):
        b += 1
    return (a, b, '')


_EXTRAS_BUSCA = (' anvisa registro brasil registrado', ' sem registro anvisa importacao manipulado',
                 ' notificado anvisa baixo risco')


def _limpa_so_pt(s):
    """Tira das versoes traduzidas o que so existe em portugues."""
    removidos_prim = 0
    for pag in SO_PT:
        nome = re.escape(pag.split('/')[-1])

        def tira_card(m):
            nonlocal removidos_prim
            if 'data-cat="primaria"' in m.group(0):
                removidos_prim += 1
            return ''
        s = re.sub(r'[ \t]*<a class="card[^"]*" href="(?:\.\./)*p/' + nome + r'".*?</a>\n?', tira_card, s, flags=re.S)
        s = re.sub(r'[ \t]*<tr>(?:(?!</tr>).)*?href="[^"]*' + nome + r'"(?:(?!</tr>).)*?</tr>\n?', '', s, flags=re.S)
        s = re.sub(r'[ \t]*<li>(?:(?!</li>).)*?href="[^"]*' + nome + r'"(?:(?!</li>).)*?</li>\n?', '', s, flags=re.S)
        s = re.sub(r'<a [^>]*href="[^"]*' + nome + r'"[^>]*>(.*?)</a>', r'\1', s, flags=re.S)
    # referencia cujo link leva ao site da ANVISA (bulario, consultas): o texto
    # nem sempre nomeia a agencia, mas o destino e ela
    # (anvisa.gov.br e gov.br/anvisa: o padrao pega os dois)
    s = re.sub(r'[ \t]*<li[^>]*>(?:(?!</li>).)*?href="[^"]*anvisa[^"]*"(?:(?!</li>).)*?</li>\n?', '', s,
               flags=re.S | re.I)
    s = re.sub(r'<a [^>]*href="[^"]*anvisa[^"]*"[^>]*>(.*?)</a>', r'\1', s, flags=re.S | re.I)
    # Referencias que ficaram vazias (a unica fonte era da ANVISA): sai o bloco
    # inteiro -- titulo, nota e lista -- e o item dele no indice lateral.
    s2 = re.sub(r'[ \t]*<h2 id="refs">.*?</h2>\s*<div class="nota">.*?</div>\s*<ol[^>]*>\s*</ol>\n?', '', s, flags=re.S)
    if s2 != s:
        s = re.sub(r'[ \t]*<li><a href="#refs">.*?</a></li>\n?', '', s2)
    # selos, filtro e campo de registro brasileiro do indice
    s = re.sub(r'<span class="selo selo-anv-[^"]*"[^>]*>.*?</span>', '', s, flags=re.S)
    s = re.sub(r'[ \t]*<div class="filtros filtros-anvisa".*?</div>\n?', '', s, flags=re.S)
    s = re.sub(r'[ \t]*<input type="hidden" id="par-anv"[^>]*>\n?', '', s)
    s = re.sub(r' data-anv="[^"]*"', '', s)
    for extra in _EXTRAS_BUSCA:
        s = s.replace(extra, '')
    if removidos_prim:
        s = re.sub(r'(<div class="proc-lado proc-aferida">\s*<b>)(\d+)(</b>)',
                   lambda m: m.group(1) + str(int(m.group(2)) - removidos_prim) + m.group(3), s, count=1)
    return s


def resto_anvisa(s):
    """Quantas vezes a ANVISA ainda aparece na pagina, fora do CSS."""
    return len(re.findall('anvisa', re.sub(r'<style>.*?</style>', '', s, flags=re.S), re.I))


# --------------------------------------------------------------- extracao
BLOCO = set('''p li h1 h2 h3 h4 h5 h6 th td dt dd div section main aside nav header footer
               ul ol table thead tbody tr dl form button label title blockquote noscript
               body html head details summary figure figcaption caption'''.split())
VAZIO = set('meta link br input img hr area base col embed source track wbr'.split())
PULA = set('script style svg code template'.split())
ATTRS = set('title aria-label placeholder alt tooldescription toolparamdescription '
            'data-frase-nenhum data-frase-todos data-frase-parte'.split())
_LETRA = re.compile(r'[^\W\d_]', re.UNICODE)
_ATTR = re.compile(r'\s([a-zA-Z:][\w:.-]*)="([^"]*)"')


class _No:
    __slots__ = ('tag', 'attrs', 'ini', 'fim_abertura', 'ini_fecho', 'fim',
                 'filhos', 'texto', 'pai', 'tag_txt')

    def __init__(self, tag, attrs, ini, fim_abertura, tag_txt, pai):
        self.tag, self.attrs, self.ini, self.fim_abertura = tag, attrs, ini, fim_abertura
        self.tag_txt, self.pai = tag_txt, pai
        self.ini_fecho = self.fim = None
        self.filhos, self.texto = [], False


class _Arvore(HTMLParser):
    def __init__(self, fonte):
        super().__init__(convert_charrefs=False)
        self.fonte = fonte
        self.linhas = [0]
        for m in re.finditer('\n', fonte):
            self.linhas.append(m.end())
        self.raiz = _No('#raiz', {}, 0, 0, '', None)
        self.pilha = [self.raiz]

    def _abs(self):
        l, c = self.getpos()
        return self.linhas[l - 1] + c

    def handle_starttag(self, tag, attrs):
        ini = self._abs()
        txt = self.get_starttag_text()
        no = _No(tag, dict(attrs), ini, ini + len(txt), txt, self.pilha[-1])
        self.pilha[-1].filhos.append(no)
        if tag in VAZIO:
            no.ini_fecho = no.fim = no.fim_abertura
        else:
            self.pilha.append(no)

    def handle_startendtag(self, tag, attrs):
        ini = self._abs()
        txt = self.get_starttag_text()
        no = _No(tag, dict(attrs), ini, ini + len(txt), txt, self.pilha[-1])
        no.ini_fecho = no.fim = no.fim_abertura
        self.pilha[-1].filhos.append(no)

    def handle_endtag(self, tag):
        ini = self._abs()
        fim = self.fonte.index('>', ini) + 1
        for k in range(len(self.pilha) - 1, 0, -1):
            if self.pilha[k].tag == tag:
                for no in self.pilha[k:]:
                    if no.fim is None:
                        no.ini_fecho, no.fim = ini, fim
                del self.pilha[k:]
                return

    def _texto(self, s):
        if s.strip():
            self.pilha[-1].texto = True

    def handle_data(self, d):
        self._texto(d)

    def handle_entityref(self, n):
        self._texto('&' + n + ';')

    def handle_charref(self, n):
        self._texto('&#' + n + ';')


def _norm(s):
    # so espaco ASCII: o \s do regex pegaria o U+00A0 que o frances usa como milhar
    return re.sub('[ \t\r\n]+', ' ', s).strip()


def _traduzivel(s):
    return len(s) > 1 and bool(_LETRA.search(html.unescape(re.sub(r'<[^>]+>', '', s))))


def segmentos(fonte):
    """Trechos traduziveis da pagina: (ini, fim, chave, tipo, no).

    tipo 'inner': o innerHTML de um elemento folha (ou folha-de-bloco).
    tipo 'attr' : o valor de um atributo visivel.
    """
    arv = _Arvore(fonte)
    arv.feed(fonte)
    arv.close()
    out = []

    def attrs_de(no):
        if 'hreflang' in no.attrs:      # seletor de idioma: endonimos nao se traduzem
            return
        for m in _ATTR.finditer(no.tag_txt):
            nome, val = m.group(1), m.group(2)
            ok = nome in ATTRS or (
                no.tag == 'meta' and nome == 'content' and (
                    no.attrs.get('name') == 'description'
                    or no.attrs.get('property') in ('og:title', 'og:description')))
            if not ok:
                continue
            chave = _norm(html.unescape(val))
            if not _traduzivel(chave):
                continue
            out.append((no.ini + m.start(2), no.ini + m.end(2), chave, 'attr', no))

    def visita(no):
        if no.tag in PULA:
            return
        if no.tag != '#raiz':
            attrs_de(no)
        if no.fim is None or no.tag in VAZIO or no.tag == '#raiz':
            for f in no.filhos:
                visita(f)
            return
        elems = [f for f in no.filhos]
        if not elems:
            if no.texto:
                inner = fonte[no.fim_abertura:no.ini_fecho]
                chave = _norm(inner)
                if _traduzivel(chave):
                    out.append((no.fim_abertura, no.ini_fecho, chave, 'inner', no))
            return
        if no.texto:
            if any(f.tag in BLOCO for f in elems):
                # texto solto misturado com bloco: nao acontece neste site;
                # se um dia acontecer, os filhos sao traduzidos e o texto
                # solto fica em portugues -- e o relatorio avisa
                sys.stderr.write('idiomas: texto solto entre blocos em <%s %s>\n'
                                 % (no.tag, no.attrs.get('class', '')))
                for f in elems:
                    visita(f)
                return
            inner = fonte[no.fim_abertura:no.ini_fecho]
            chave = _norm(inner)
            if _traduzivel(chave):
                out.append((no.fim_abertura, no.ini_fecho, chave, 'inner', no))
            return
        for f in elems:
            visita(f)

    visita(arv.raiz)
    return out


# ------------------------------------------------------------ memoria
def _le_json(caminho):
    if not os.path.exists(caminho):
        return {}
    with open(caminho, encoding='utf-8') as f:
        return json.load(f)


def _grava_json(caminho, dados):
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    with open(caminho, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(dados, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write('\n')


# Pares (celula PT, celula EN original) que o gerador registra ao traduzir as
# tabelas da fonte. Para o ingles a "traducao" da tabela e o proprio original:
# nao ha o que inventar. Persistido em en-fonte.json para nao depender do
# build/src, que nao e versionado.
MEMORIA_EN = {}


def registra_en(pt, en):
    # mesmo escape que gerar.esc(): a chave e o innerHTML da celula, nao o texto
    pt, en = _norm(html.escape(str(pt), quote=True)), _norm(html.escape(str(en), quote=True))
    if pt and en and _traduzivel(pt):
        MEMORIA_EN.setdefault(pt, en)


def carrega_memorias():
    mem = {}
    for idi in IDIOMAS:
        mem[idi] = _le_json(os.path.join(PASTA, idi + '.json'))
    # o ingles ganha a camada automatica por baixo da explicita
    auto = _le_json(os.path.join(PASTA, 'en-fonte.json'))
    auto.update(MEMORIA_EN)
    if auto:
        _grava_json(os.path.join(PASTA, 'en-fonte.json'), auto)
    for k, v in auto.items():
        mem['en'].setdefault(k, v)
    return mem


# ------------------------------------------------------------- pagina
_LD = re.compile(r'<script type="application/ld\+json">\n(.*?)\n</script>', re.S)
_TITULO = re.compile(r'<title>(.*?)</title>', re.S)
_DESCR = re.compile(r'<meta name="description" content="([^"]*)">')
_CANON = re.compile(r'<link rel="canonical" href="%s([^"]*)">' % re.escape(BASE))
_CARD = re.compile(r'(<a class="card[^"]*" href="p/[^"]+"[^>]*data-busca=")([^"]*)(">)(.*?)(</a>)', re.S)
_TXT = re.compile(r'<[^>]+>')


def traduz_pagina(fonte, rel, idioma, mem, relat, sem=None):
    """Devolve o HTML de `rel` no idioma dado, usando a memoria `mem`.

    `sem`: camada sem ANVISA ({trecho pt: (versao, ajuste)}), aplicada antes
    da memoria. Versao vazia, ou reprovada na trava, tira o elemento."""
    conv = IDIOMAS[idioma]
    segs = segmentos(fonte)
    sem = sem or {}
    trocas = []     # (ini, fim, texto)
    for ini, fim, chave, tipo, no in segs:
        if chave in sem:
            nova, ajuste = sem[chave]
            probs = valida_sem(chave, mem.get(chave), nova, idioma, ajuste) if nova else []
            if probs:
                relat['rejeitados'][chave] = ['sem-anvisa: ' + p for p in probs]
                nova = ''
            if nova == '':
                trocas.append(_remocao(fonte, ini, fim, tipo, no))
            elif tipo == 'attr':
                trocas.append((ini, fim, html.escape(nova, quote=True)))
            else:
                trocas.append((ini, fim, nova))
            relat['traduzidos'].add(chave)
            continue
        if re.search('anvisa', chave, re.I):
            # trecho com ANVISA sem versao na camada: nao pode ir para a pagina
            relat['sem_versao'][chave] = rel
            trocas.append(_remocao(fonte, ini, fim, tipo, no))
            continue
        trad = mem.get(chave)
        if trad is None:
            relat['pendentes'][chave] = relat['pendentes'].get(chave) or rel
            if tipo == 'inner' and 'lang' not in no.attrs and no.tag != 'title':
                trocas.append((no.fim_abertura - 1, no.fim_abertura - 1, ' lang="pt-BR"'))
            continue
        probs = valida(chave, trad, idioma)
        if probs:
            # rejeitado volta para a fila: a camada automatica do ingles
            # (celula original) as vezes diz "weekly" onde o portugues diz
            # "1x/semana", e ai e um tradutor que resolve, nao a trava
            relat['rejeitados'][chave] = probs
            relat['pendentes'][chave] = relat['pendentes'].get(chave) or rel
            if tipo == 'inner' and 'lang' not in no.attrs and no.tag != 'title':
                trocas.append((no.fim_abertura - 1, no.fim_abertura - 1, ' lang="pt-BR"'))
            continue
        relat['traduzidos'].add(chave)
        if tipo == 'attr':
            trocas.append((ini, fim, html.escape(trad, quote=True)))
        else:
            trocas.append((ini, fim, trad))
    # remocao de um elemento inteiro vem antes dos trechos que ficam dentro dele
    trocas.sort(key=lambda t: (t[0], -t[1]))
    partes, pos = [], 0
    for ini, fim, txt in trocas:
        if ini < pos:
            if fim <= pos:
                continue    # dentro de um elemento ja retirado
            raise RuntimeError('trechos sobrepostos em %s @%d' % (rel, ini))
        partes.append(fonte[pos:ini])
        partes.append(txt)
        pos = fim
    partes.append(fonte[pos:])
    s = ''.join(partes)

    # idioma do documento, canonical, seletor
    s = s.replace('<html lang="pt-BR">', '<html lang="%s">' % idioma, 1)
    s = _CANON.sub(lambda m: '<link rel="canonical" href="%s/%s%s">' % (BASE, idioma, m.group(1)), s, 1)
    s = re.sub(r'(<nav class="idiomas".*?</nav>)',
               lambda m: m.group(1).replace(' aria-current="true"', '')
               .replace('hreflang="%s" lang="%s"' % (idioma, idioma),
                        'hreflang="%s" lang="%s" aria-current="true"' % (idioma, idioma)),
               s, count=1, flags=re.S)

    # os assets ficam um nivel acima
    s = re.sub(r'((?:href|src)=")((?:\.\./)*)assets/', r'\1../\2assets/', s)
    s = re.sub(r'(url\()((?:\.\./)*)assets/', r'\1../\2assets/', s)

    # JSON-LD: idioma, url e os dois textos que ja foram traduzidos acima
    def ld(m):
        d = json.loads(m.group(1).replace('<\\/', '</'))
        d['inLanguage'] = idioma
        d['url'] = '%s/%s/%s' % (BASE, idioma, rel.replace(os.sep, '/'))
        t = _TITULO.search(s)
        if t:
            d['name'] = html.unescape(t.group(1))
        de = _DESCR.search(s)
        if de:
            d['description'] = html.unescape(de.group(1))
        txt = json.dumps(d, ensure_ascii=False, indent=2).replace('</', '<\\/')
        return '<script type="application/ld+json">\n%s\n</script>' % txt
    s = _LD.sub(ld, s, count=1)

    # busca do indice: os termos traduzidos entram ao lado dos originais
    def card(m):
        corpo = m.group(4)
        achados = re.findall(r'<h3>(.*?)</h3>|<p>(.*?)</p>|<span class="selo selo-cat">(.*?)</span>', corpo)
        termos = ' '.join(html.unescape(_TXT.sub(' ', t)) for grupo in achados for t in grupo if t)
        return (m.group(1) + m.group(2) + ' ' + html.escape(_norm(termos).lower(), quote=True)
                + m.group(3) + corpo + m.group(5))
    s = _CARD.sub(card, s)

    # Sem aviso de traducao no topo, por decisao de 10/09/2026. Os textos do
    # aviso continuam em IDIOMAS[...]['aviso'] caso ele volte.

    # ANVISA so em portugues (10/09/2026)
    s = _limpa_so_pt(s)
    n = resto_anvisa(s)
    if n:
        relat['resto_anvisa'][rel.replace(os.sep, '/')] = n
    return s


# ------------------------------------------------------------- build
def _entregas_abertas():
    """Idiomas com entrega gravada e ainda nao incorporada."""
    out = []
    for idioma in IDIOMAS:
        pasta = os.path.join(PASTA, 'entregas', idioma)
        if os.path.isdir(pasta) and any(f.endswith('.json') for f in os.listdir(pasta)):
            out.append(idioma)
    return out


def gerar(paginas, log=print, fila=False):
    """`paginas`: caminhos relativos a raiz, ja gravados em portugues.

    Devolve {idioma: relatorio}. Grava /<idioma>/... e, so com fila=True, a
    fila de pendentes. A fila NAO e reescrita em todo build de proposito: os
    ids de cada parte sao a unica ligacao entre a entrada e a entrega de um
    tradutor, e reescrever a fila com uma entrega em andamento trocaria o
    sentido dos ids. Ver --pendentes.
    """
    if fila:
        abertas = _entregas_abertas()
        if abertas:
            raise SystemExit('idiomas: ha entregas nao incorporadas em %s. Rode --incorporar '
                             'antes de reescrever a fila.' % ', '.join(abertas))
    mem = carrega_memorias()
    paginas = [p for p in paginas if p.replace(os.sep, '/') not in SO_PT]
    saida = {}
    for idioma in IDIOMAS:
        relat = dict(traduzidos=set(), pendentes={}, rejeitados={}, sem_versao={}, resto_anvisa={})
        sem = carrega_sem_anvisa(idioma)
        for pag in SO_PT:   # versao traduzida antiga, de antes da decisao
            velho = os.path.join(RAIZ, idioma, pag)
            if os.path.exists(velho):
                os.remove(velho)
        for rel in paginas:
            with open(os.path.join(RAIZ, rel), encoding='utf-8') as f:
                fonte = f.read()
            dest = os.path.join(RAIZ, idioma, rel)
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            with open(dest, 'w', encoding='utf-8', newline='\n') as f:
                f.write(traduz_pagina(fonte, rel, idioma, mem[idioma], relat, sem))
        saida[idioma] = relat
        if relat['sem_versao'] or relat['resto_anvisa']:
            log('idioma %s: %d trecho(s) com ANVISA sem versao na camada (retirados); ANVISA ainda em %d pagina(s)'
                % (idioma, len(relat['sem_versao']), len(relat['resto_anvisa'])))
        _grava_json(os.path.join(PASTA, 'rejeitados', idioma + '.json'), relat['rejeitados'])
    if fila:
        _grava_pendentes(saida, mem)
    for idioma, r in saida.items():
        tot = len(r['traduzidos']) + len(r['pendentes'])
        log('idioma %s: %d de %d trechos traduzidos (%.1f%%), %d pendentes, dos quais %d rejeitados pela trava'
            % (idioma, len(r['traduzidos']), tot, 100.0 * len(r['traduzidos']) / max(tot, 1),
               len(r['pendentes']), len(r['rejeitados'])))
    return saida


def _palavras(s):
    return len(_TXT.sub(' ', s).split())


def _grava_pendentes(saida, mem, alvo_palavras=7000):
    """Fila de trabalho por idioma, em partes de ~alvo_palavras palavras."""
    en_auto = _le_json(os.path.join(PASTA, 'en-fonte.json'))
    for idioma, r in saida.items():
        pasta = os.path.join(PASTA, 'pendentes', idioma)
        if os.path.isdir(pasta):
            for f in os.listdir(pasta):
                os.remove(os.path.join(pasta, f))
        itens = sorted(r['pendentes'].items(), key=lambda kv: (kv[1], kv[0]))
        partes, atual, soma = [], [], 0
        for k, (chave, onde) in enumerate(itens):
            it = {'id': k, 'pt': chave, 'onde': onde}
            if chave in en_auto and idioma != 'en':
                it['en_original'] = en_auto[chave]
            atual.append(it)
            soma += _palavras(chave)
            if soma >= alvo_palavras:
                partes.append(atual)
                atual, soma = [], 0
        if atual:
            partes.append(atual)
        for n, p in enumerate(partes, 1):
            _grava_json(os.path.join(pasta, 'parte-%02d.json' % n), p)


def incorporar(log=print):
    """Le build/traducoes/entregas/<idioma>/*.json e guarda o que passa na trava."""
    for idioma in IDIOMAS:
        pasta = os.path.join(PASTA, 'entregas', idioma)
        if not os.path.isdir(pasta):
            continue
        mem = _le_json(os.path.join(PASTA, idioma + '.json'))
        # id -> chave, pelas partes pendentes correspondentes
        chaves = {}
        pend = os.path.join(PASTA, 'pendentes', idioma)
        if os.path.isdir(pend):
            for f in os.listdir(pend):
                for it in _le_json(os.path.join(pend, f)):
                    chaves[it['id']] = it['pt']
        ok = rej = 0
        rejeitados = {}
        feitos = os.path.join(pasta, 'incorporado')
        lidos = []
        for f in sorted(os.listdir(pasta)):
            if not f.endswith('.json'):
                continue
            # a entrega tem que ser posterior a fila que ela responde: se a
            # parte foi reescrita depois, os ids ja nao querem dizer o mesmo
            parte = os.path.join(pend, f)
            if os.path.exists(parte) and os.path.getmtime(parte) > os.path.getmtime(os.path.join(pasta, f)):
                log('incorporar %s: %s IGNORADA -- a fila foi reescrita depois da entrega' % (idioma, f))
                continue
            # Arquivo ilegivel quase sempre e entrega sendo gravada agora
            # (tradutor escrevendo em blocos). Pula sem mover: na proxima
            # rodada, ja completo, entra.
            try:
                entrega = _le_json(os.path.join(pasta, f))
            except (ValueError, UnicodeDecodeError) as erro:
                log('incorporar %s: %s PULADA -- JSON ilegivel (%s)' % (idioma, f, erro))
                continue
            itens = entrega if isinstance(entrega, list) else [
                {'pt': k, 'trad': v} for k, v in entrega.items()]
            for it in itens:
                chave = it.get('pt') if it.get('pt') is not None else chaves.get(it.get('id'))
                trad = it.get('trad')
                if chave is None:
                    continue
                chave = _norm(chave)
                if trad is not None and idioma == 'fr':
                    trad = _conserta_milhar_fr(chave, trad)
                probs = valida(chave, trad if trad is None else _norm(trad), idioma)
                if probs:
                    rejeitados[chave] = {'trad': trad, 'motivo': probs, 'arquivo': f}
                    rej += 1
                else:
                    mem[chave] = _norm(trad)
                    ok += 1
            # So move depois de gravar a memoria (abaixo). Mover aqui e cair
            # antes de gravar perdeu uma entrega inteira em 10/09/2026.
            lidos.append(f)
        # rejeitado de rodada anterior que passou a valer (trava afrouxada,
        # excecao registrada): entra sem precisar de nova entrega
        antigos = _le_json(os.path.join(PASTA, 'rejeitados', idioma + '-entregas.json'))
        for chave, it in antigos.items():
            if chave in mem or not isinstance(it, dict):
                continue
            trad = it.get('trad')
            if trad and idioma == 'fr':
                trad = _conserta_milhar_fr(chave, trad)
            if trad and not valida(chave, _norm(trad), idioma):
                mem[chave] = _norm(trad)
                ok += 1
            else:
                rejeitados.setdefault(chave, it)
        _grava_json(os.path.join(PASTA, idioma + '.json'), mem)
        os.makedirs(feitos, exist_ok=True)
        for f in lidos:
            os.replace(os.path.join(pasta, f), os.path.join(feitos, f))
        _grava_json(os.path.join(PASTA, 'rejeitados', idioma + '-entregas.json'), rejeitados)
        log('incorporar %s: %d aceitos, %d rejeitados (motivos em rejeitados/%s-entregas.json)'
            % (idioma, ok, rej, idioma))


def paginas_existentes():
    pags = [p for p in PAGINAS_RAIZ if os.path.exists(os.path.join(RAIZ, p))]
    pasta = os.path.join(RAIZ, 'p')
    if os.path.isdir(pasta):
        pags += [os.path.join('p', f) for f in sorted(os.listdir(pasta)) if f.endswith('.html')]
    return pags


if __name__ == '__main__':
    if '--incorporar' in sys.argv:
        incorporar()
    elif '--pendentes' in sys.argv:
        gerar(paginas_existentes(), fila=True)
    elif '--gerar' in sys.argv:
        gerar(paginas_existentes())
    else:
        print(__doc__)

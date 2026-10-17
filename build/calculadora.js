/* Calculadora de reconstituição.
 *
 * Faz só a aritmética de diluição, e nada além dela:
 *
 *     concentração = massa no frasco ÷ água adicionada
 *     volume       = dose ÷ concentração
 *     unidades     = volume × 100        (seringa U-100: 100 unidades = 1 mL)
 *
 * Não sugere dose, não preenche dose a partir do composto escolhido e não
 * guarda nada: o estado vive só no endereço da página, para que uma conta
 * possa ser conferida por outra pessoa abrindo o mesmo link.
 *
 * Todo texto que o leitor vê mora no HTML (#calc-frases), e não aqui, para
 * que as versões em outros idiomas o traduzam como qualquer outro trecho da
 * página. Os números saem no separador do idioma do documento.
 */
(function () {
  var raiz = document.getElementById('calc');
  if (!raiz) return;
  raiz.hidden = false;

  var lang = document.documentElement.lang || 'pt-BR';
  var $ = function (id) { return document.getElementById(id); };

  var campos = {
    dose: $('calc-dose'),
    un: $('calc-dose-un'),
    frasco: $('calc-frasco'),
    agua: $('calc-agua'),
    comp: $('calc-comp')
  };

  function frase(chave, vars) {
    var no = document.querySelector('#calc-frases [data-f="' + chave + '"]');
    var t = no ? no.innerHTML : chave;
    Object.keys(vars || {}).forEach(function (k) {
      t = t.split('{' + k + '}').join(vars[k]);
    });
    return t;
  }

  function fmt(n, casas, min) {
    return new Intl.NumberFormat(lang, {
      maximumFractionDigits: casas,
      minimumFractionDigits: min || 0
    }).format(n);
  }

  // Aceita "0,25" e "0.25". Com vírgula, a vírgula é o decimal e o ponto,
  // milhar; sem vírgula, o ponto é o decimal. Campo vazio ou não numérico
  // devolve NaN, e a conta não sai.
  function le(campo) {
    var s = String(campo.value).trim().replace(/\s/g, '');
    if (!s) return NaN;
    if (s.indexOf(',') !== -1) s = s.replace(/\./g, '').replace(',', '.');
    if (!/^\d*\.?\d+$|^\d+\.$/.test(s)) return NaN;
    return parseFloat(s);
  }

  // Sem separador de milhar: "1,000" em inglês voltaria pelo le() como 1.
  function escreve(campo, v) {
    campo.value = new Intl.NumberFormat(lang, {
      maximumFractionDigits: 4, useGrouping: false
    }).format(v);
  }

  // ---------------------------------------------------------- chips
  // Os valores de atalho moram em data-valores; o rótulo é formatado aqui,
  // no idioma da página. Sem JavaScript não há chip, e a página já diz isso.
  Array.prototype.forEach.call(raiz.querySelectorAll('[data-valores]'), function (grupo) {
    var alvo = $(grupo.getAttribute('data-alvo'));
    var unidade = grupo.getAttribute('data-unidade');
    grupo.getAttribute('data-valores').split(' ').forEach(function (v) {
      var b = document.createElement('button');
      b.type = 'button';
      b.className = 'filtro';
      b.setAttribute('data-v', v);
      b.setAttribute('aria-pressed', 'false');
      b.textContent = fmt(parseFloat(v), 4) + ' ' + unidade;
      b.addEventListener('click', function () {
        escreve(alvo, parseFloat(v));
        if (grupo.getAttribute('data-alvo') === 'calc-dose') campos.un.value = 'mg';
        calcula();
        alvo.focus();
      });
      grupo.appendChild(b);
    });
  });

  function marcaChips() {
    Array.prototype.forEach.call(raiz.querySelectorAll('[data-valores]'), function (grupo) {
      var alvo = $(grupo.getAttribute('data-alvo'));
      var v = le(alvo);
      var emMg = !(grupo.getAttribute('data-alvo') === 'calc-dose' && campos.un.value === 'mcg');
      Array.prototype.forEach.call(grupo.querySelectorAll('button'), function (b) {
        var igual = emMg && Math.abs(parseFloat(b.getAttribute('data-v')) - v) < 1e-9;
        b.setAttribute('aria-pressed', igual ? 'true' : 'false');
      });
    });
  }

  // -------------------------------------------------------- seringa
  var SVG = 'http://www.w3.org/2000/svg';
  var X0 = 20, X1 = 560;           // 0 e a capacidade, no corpo da seringa
  // Capacidade em unidades U-100: 30 (0,3 mL), 50 (0,5 mL) ou 100 (1 mL).
  // A escala é sempre U-100; o que muda é até onde ela vai.
  var cap = 100;

  function desenhaEscala() {
    var g = $('calc-escala');
    while (g.firstChild) g.removeChild(g.firstChild);
    var passo = cap === 100 ? 2 : 1, rotulo = cap === 100 ? 10 : 5;
    for (var u = 0; u <= cap; u += passo) {
      var x = X0 + (X1 - X0) * u / cap;
      var alto = u % rotulo === 0 ? 22 : 12;
      var l = document.createElementNS(SVG, 'line');
      l.setAttribute('x1', x); l.setAttribute('x2', x);
      l.setAttribute('y1', 26); l.setAttribute('y2', 26 + alto);
      g.appendChild(l);
      if (u % rotulo === 0) {
        var t = document.createElementNS(SVG, 'text');
        t.setAttribute('x', x); t.setAttribute('y', 90);
        t.textContent = String(u);
        g.appendChild(t);
      }
    }
  }

  function seringa(unid) {
    var cheio = $('calc-liquido');
    var embolo = $('calc-embolo');
    var passou = unid > cap;
    var u = Math.max(0, Math.min(cap, unid || 0));
    var x = X0 + (X1 - X0) * u / cap;
    cheio.setAttribute('width', Math.max(0, x - X0));
    cheio.setAttribute('class', passou ? 'calc-liq calc-liq-passou' : 'calc-liq');
    embolo.setAttribute('transform', 'translate(' + (x - X0) + ',0)');
  }

  // ----------------------------------------------------------- conta
  function alerta(tipo, html) {
    return '<div class="' + (tipo === 'grave' ? 'aviso-linha calc-grave' : 'nota') + '">' + html + '</div>';
  }

  // "1 unidade", "7,5 unidades": o número já sai com a palavra concordando
  function unid_txt(n, casas) {
    return fmt(n, casas) + ' ' + frase(Math.abs(n - 1) < 1e-9 ? 'unidade' : 'unidades');
  }

  function massa(mg) {
    // a dose aparece na unidade em que o leitor a digitou
    return campos.un.value === 'mcg'
      ? fmt(mg * 1000, 1) + ' mcg'
      : fmt(mg, 4) + ' mg';
  }

  function limpa(msg) {
    ['r-unid', 'r-conc', 'r-conc-mcg', 'r-vol', 'r-doses', 'r-doses-exato'].forEach(function (id) {
      $(id).textContent = '—';
    });
    $('r-dose-eq').textContent = '';
    $('r-un-rot').textContent = frase('unidades');
    $('calc-alertas').innerHTML = msg ? alerta('nota', msg) : '';
    $('calc-status').textContent = '';
    seringa(0);
  }

  function calcula() {
    marcaChips();
    sincronizaUrl();
    var doseBruta = le(campos.dose);
    var frasco = le(campos.frasco);
    var agua = le(campos.agua);
    if (!(frasco > 0) || !(agua > 0)) {
      limpa(frase('incompleto'));
      semDose();     // a conta inversa não precisa da água: é ela que calcula
      return;
    }
    if (!(doseBruta > 0)) {
      // frasco e água bastam para a concentração; o resto pede a dose
      limpa(frase('falta-dose'));
      $('r-conc').textContent = fmt(frasco / agua, 3) + ' mg/mL';
      $('r-conc-mcg').textContent = fmt(frasco / agua * 1000, 1) + ' mcg/mL';
      semDose();
      return;
    }
    var dose = campos.un.value === 'mcg' ? doseBruta / 1000 : doseBruta;   // mg
    var conc = frasco / agua;             // mg/mL
    var vol = dose / conc;                // mL
    var unid = vol * 100;                 // unidades U-100
    var exato = frasco / dose;
    var doses = Math.floor(exato + 1e-9);

    $('r-unid').textContent = fmt(unid, 1);
    $('r-un-rot').textContent = frase(Math.abs(unid - 1) < 1e-9 ? 'unidade' : 'unidades');
    $('r-dose-eq').textContent = campos.un.value === 'mcg'
      ? '= ' + fmt(dose, 4) + ' mg'
      : '= ' + fmt(dose * 1000, 1) + ' mcg';
    $('r-conc').textContent = fmt(conc, 3) + ' mg/mL';
    $('r-conc-mcg').textContent = fmt(conc * 1000, 1) + ' mcg/mL';
    $('r-vol').textContent = fmt(vol, 3) + ' mL';
    $('r-doses').textContent = fmt(doses, 0);
    $('r-doses-exato').textContent = frase('exato', { x: fmt(exato, 2) });
    seringa(unid);

    var al = [];
    if (dose > frasco) {
      al.push(alerta('grave', frase('maior-que-frasco')));
    }
    if (unid > cap) {
      al.push(alerta('grave', frase('passa-seringa', {
        u: unid_txt(unid, 1), ml: fmt(cap / 100, 1), cap: fmt(cap, 0)
      })));
    }
    if (unid < 5) {
      al.push(alerta('grave', frase('pouco-volume', { u: unid_txt(unid, 1), pct: fmt(100 / unid, 0) })));
    }
    // A seringa se lê por traço inteiro. Quando a conta cai entre dois
    // traços, a dose entregue não é a digitada: é a de um dos vizinhos.
    var baixo = Math.floor(unid + 1e-9), alto = Math.ceil(unid - 1e-9);
    if (unid <= cap && alto - baixo === 1 && baixo >= 1) {
      al.push(alerta('nota', frase('entre-tracos', {
        u: unid_txt(unid, 1),
        a: unid_txt(baixo, 0), da: massa(baixo / 100 * conc),
        b: unid_txt(alto, 0), db: massa(alto / 100 * conc)
      })));
    }
    $('calc-alertas').innerHTML = al.join('');
    $('calc-status').textContent = frase('status', {
      u: unid_txt(unid, 1), v: fmt(vol, 3), c: fmt(conc, 3)
    });
    inverso(frasco, dose);
  }

  // ------------------------------------------------------ conta inversa
  // A mesma conta, de trás para a frente: quem quer que a dose ocupe N
  // unidades descobre quanta água pôr no frasco.
  //     unidades = dose × água × 100 ÷ massa   →   água = unidades × massa ÷ (100 × dose)
  // Não escolhe dose: parte da que já foi digitada.
  var ultimaAgua = NaN;
  function inverso(frasco, dose) {
    var saida = $('calc-inv-saida');
    var usar = $('calc-inv-usar');
    var alvo = le($('calc-alvo'));
    ultimaAgua = NaN;
    usar.hidden = true;
    if (!(alvo > 0)) { saida.innerHTML = ''; return; }
    if (!(frasco > 0) || !(dose > 0)) { saida.innerHTML = frase('inv-falta'); return; }
    var agua = alvo * frasco / (100 * dose);
    ultimaAgua = agua;
    var t = frase('inv-resultado', { u: unid_txt(alvo, 1), d: massa(dose), a: fmt(agua, 2) });
    if (alvo > cap) t += ' ' + frase('inv-passa', { cap: fmt(cap, 0) });
    saida.innerHTML = t;
    usar.hidden = false;
  }

  function semDose() {
    var frasco = le(campos.frasco), d = le(campos.dose);
    inverso(frasco, campos.un.value === 'mcg' ? d / 1000 : d);
  }

  // ------------------------------------------------- composto escolhido
  // Escolher o composto NÃO preenche dose nem frasco: só aponta para a
  // tabela de reconstituição da página dele, onde a procedência do número
  // está dita. Dose não sai de uma lista de opções.
  function mostraComposto() {
    var op = campos.comp.options[campos.comp.selectedIndex];
    var href = op && op.getAttribute('data-href');
    var caixa = $('calc-comp-link');
    if (!href) { caixa.hidden = true; return; }
    var a = caixa.querySelector('a');
    a.setAttribute('href', href);
    a.querySelector('span').textContent = op.textContent;
    caixa.hidden = false;
  }

  // ------------------------------------------------------------ URL
  var PARAMS = { d: campos.dose, f: campos.frasco, a: campos.agua, t: $('calc-alvo') };

  function sincronizaUrl() {
    if (!window.history || !history.replaceState) return;
    var q = [];
    Object.keys(PARAMS).forEach(function (k) {
      var v = le(PARAMS[k]);
      if (v > 0) q.push(k + '=' + encodeURIComponent(String(v)));
    });
    if (campos.un.value === 'mcg') q.push('u=mcg');
    if (cap !== 100) q.push('s=' + cap);
    if (campos.comp.value) q.push('c=' + encodeURIComponent(campos.comp.value));
    history.replaceState(null, '', location.pathname + (q.length ? '?' + q.join('&') : ''));
  }

  function leUrl() {
    var p = {};
    location.search.replace(/^\?/, '').split('&').forEach(function (par) {
      var kv = par.split('=');
      if (kv[0]) p[kv[0]] = decodeURIComponent(kv[1] || '');
    });
    Object.keys(PARAMS).forEach(function (k) {
      var v = parseFloat(p[k]);
      if (v > 0 && isFinite(v)) escreve(PARAMS[k], v);
    });
    if (p.u === 'mcg') campos.un.value = 'mcg';
    if (p.s === '30' || p.s === '50') cap = parseInt(p.s, 10);
    if (p.c) {
      for (var i = 0; i < campos.comp.options.length; i++) {
        if (campos.comp.options[i].value === p.c) campos.comp.selectedIndex = i;
      }
    }
  }

  $('calc-copiar').addEventListener('click', function () {
    var aviso = $('calc-copiado');
    var ok = function () { aviso.innerHTML = frase('copiado'); };
    var falha = function () { aviso.innerHTML = frase('nao-copiou'); };
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(location.href).then(ok, falha);
    } else {
      falha();
    }
  });

  $('calc-limpar').addEventListener('click', function () {
    campos.dose.value = ''; campos.frasco.value = ''; campos.agua.value = '';
    $('calc-alvo').value = '';
    campos.un.value = 'mg'; campos.comp.selectedIndex = 0;
    cap = 100; marcaSeringa(); desenhaEscala();
    $('calc-copiado').textContent = '';
    mostraComposto();
    calcula();
    campos.frasco.focus();
  });

  // ------------------------------------------------- tamanho da seringa
  var botoesCap = Array.prototype.slice.call(document.querySelectorAll('#calc-seringas button'));
  function marcaSeringa() {
    botoesCap.forEach(function (b) {
      b.setAttribute('aria-pressed', parseInt(b.getAttribute('data-cap'), 10) === cap ? 'true' : 'false');
    });
  }
  botoesCap.forEach(function (b) {
    b.addEventListener('click', function () {
      cap = parseInt(b.getAttribute('data-cap'), 10);
      marcaSeringa(); desenhaEscala(); calcula();
    });
  });

  $('calc-inv-usar').addEventListener('click', function () {
    if (!(ultimaAgua > 0)) return;
    // o mesmo arredondamento do texto (2 casas), para o campo bater com ele
    var a = Math.round(ultimaAgua * 100) / 100;
    escreve(campos.agua, a > 0 ? a : ultimaAgua);
    calcula();
    campos.agua.focus();
  });

  [campos.dose, campos.frasco, campos.agua, $('calc-alvo')].forEach(function (c) {
    c.addEventListener('input', calcula);
  });
  campos.un.addEventListener('change', calcula);
  campos.comp.addEventListener('change', function () { mostraComposto(); sincronizaUrl(); });

  leUrl();
  marcaSeringa();
  desenhaEscala();
  mostraComposto();
  calcula();
})();
